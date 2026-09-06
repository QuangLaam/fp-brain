#!/usr/bin/env python3
"""Bounded FP native acceptance runner; branching and verdicts belong to reviewers.

Preparation: `hash --candidate skills/fp`, `self-test` (no native sessions).
After PACKAGE_VALIDATED: `init --run NAME --candidate skills/fp
  --package-validated TREE_SHA --review-gate 'review evidence reference'`.
Then `start --run NAME --slot N01`; read all raw evidence, and record
`provenance --run NAME --decision PASS --observed-entry 'path from actual trace'
  --evidence 'paths/content/context evidence'`.
No other session starts until this first-case provenance gate passes.
`followup --run NAME --slot N01 --branch 1 --reason 'actual question matches ...'`
sends only the exact selected frozen response. Branch indices are one-based;
the reviewer may choose any unused eligible branch matching the actual question.
`stop --run NAME --slot N01 --status AMBIGUOUS_FIXTURE --reason 'exact question'`
or `--status OBSERVED` ends a case without inventing a continuation or verdict.
`status --run NAME` reports slots and remaining budgets. `batch --run NAME
  --candidate skills/fp --package-validated TREE_SHA --review-gate REF
  --repair-note REF --host-recovery` opens the final permitted second batch
under host-recovery-v1.md, retaining the first. No runtime repair/third batch.

One invocation executes at most one model turn. A timeout/error consumes the
session slot and cannot be retried. Up to two CLI processes may run concurrently.
Never pass rubric, fixture predicates, reviewer decisions or plans to the model.
The ordinary slot O01 sees the same discoverable package but no explicit skill
request/body. Package presence alone does not establish selection or provenance.
"""

import argparse
import contextlib
import datetime as dt
import fcntl
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import signal
import subprocess
import sys
import tempfile
import uuid

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "evals/rebuild-v1"
EVIDENCE = ROOT / "evals/evidence"
CLI = Path("/Users/quanglaam/.local/bin/codex")
RECOVERY_CLI = Path("/Applications/ChatGPT.app/Contents/Resources/codex")
CLI_PINS = {
    str(CLI): ("codex-cli 0.151.0", "98491713ffb196061003ee148636e743997cc31d76144ba7c53462269896891d"),
    str(RECOVERY_CLI): ("codex-cli 0.153.4", "a30ec314bbd0e3721632234d07db7c99855db3b9f1e32dbe8c791947f07e7629"),
}
RECOVERY_CANDIDATE = "c79d1e0425c914c87800bfe2ad91d0e89f94565be7a97bf788fd4939833ad843"
MODEL = "gpt-6-astra"
FREEZE_SHA = "dba2c0e32f70ecc48238cbea2673a6f4ee596c9d001fbb0d286c798356a96284"
RUN_PREFIX = "2026-09-06-fp-rebuild-native-"


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def create_json(path, data):
    with path.open("x") as stream:
        json.dump(data, stream, ensure_ascii=False, indent=2)
        stream.write("\n")


def tree(path):
    require(path.is_dir(), f"Missing candidate: {path}")
    require(not path.is_symlink(), "Candidate root must not be a symlink")
    files = {}
    for item in sorted(path.rglob("*")):
        require(not item.is_symlink(), f"Candidate contains symlink: {item}")
        if item.is_file():
            files[item.relative_to(path).as_posix()] = sha(item)
    require("SKILL.md" in files, "Candidate must contain SKILL.md")
    encoded = json.dumps(files, sort_keys=True, separators=(",", ":")).encode()
    return {"sha256": hashlib.sha256(encoded).hexdigest(), "files": files}


def fixtures():
    require(sha(FIXTURES / "freeze.json") == FREEZE_SHA, "Frozen manifest changed")
    for name, expected in read(FIXTURES / "freeze.json")["files"].items():
        require(sha(FIXTURES / name) == expected, f"Frozen input changed: {name}")
    data = read(FIXTURES / "cases.json")
    require(data["budget"] == {"sessions_per_batch": 26, "max_batches": 2,
            "max_sessions": 52, "max_parallel": 2, "runtime_repairs": 1}, "Budget drift")
    return data


def slots(data):
    result = {case["id"]: case for case in data["cases"]}
    result.update({case + "-repeat": result[case] for case in data["repeat"]})
    result["O01"] = data["ordinary"]
    return result


def run_path(name):
    require(name.startswith(RUN_PREFIX) and Path(name).name == name,
            f"Run name must start with {RUN_PREFIX} and contain no slashes")
    return EVIDENCE / name


@contextlib.contextmanager
def locked(run):
    with (run / ".lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        yield


def journal(run, event, **data):
    with (run / "ledger.jsonl").open("a") as stream:
        stream.write(json.dumps({"at": now(), "event": event, **data}, ensure_ascii=False) + "\n")
        stream.flush()
        os.fsync(stream.fileno())


def events(path):
    if not path.exists():
        return []
    result = []
    for line in path.read_text(errors="replace").splitlines():
        try:
            result.append(json.loads(line))
        except ValueError:
            pass  # Original malformed/non-JSON lines remain in raw evidence.
    return result


def batches(run):
    return sorted(run.glob("batch-*/batch.json"))


def current(run):
    require(batches(run), "Initialize a validated batch first")
    path = batches(run)[-1].parent
    return path, read(path / "batch.json")


def latest_states(batch):
    states = {}
    for event in events(batch.parent / "ledger.jsonl"):
        if event.get("batch") == batch.name and event.get("slot") and "state" in event:
            states[event["slot"]] = event["state"]
    return states


def all_started(run):
    return [event for event in events(run / "ledger.jsonl") if event["event"] == "SESSION_RESERVED"]


def configuration(case_id, session_id=None, cli=CLI):
    # Root --search and explicit config agree; preserve the same settings on resume.
    argv = [str(cli)] + (["--search"] if case_id == "N14" else []) + ["exec"]
    if session_id:
        argv += ["resume", session_id]
    argv += ["--ignore-user-config", "--skip-git-repo-check",
             "--enable", "skip_host_skill_discovery", "--disable", "plugins",
             "--disable", "memories", "-m", MODEL,
             "-c", 'model_reasoning_effort="high"',
             "-c", 'sandbox_mode="read-only"', "-c", 'approval_policy="never"',
             "-c", 'web_search="live"' if case_id == "N14" else 'web_search="disabled"',
             "--json", "-"]
    return argv


def verify_cli(meta):
    require(meta["cli"] in CLI_PINS, "Executable is outside the approved host pins")
    expected_version, expected_sha = CLI_PINS[meta["cli"]]
    require((meta["cli_version"], meta["cli_sha256"]) == (expected_version, expected_sha),
            "Stored executable pins changed")
    require(sha(Path(meta["cli"])) == expected_sha, "Pinned executable content changed; stop")
    version = subprocess.check_output([meta["cli"], "--version"], text=True).strip()
    require(version == expected_version, "Pinned executable version changed; stop")


def no_model_output(rows):
    for event in rows:
        payload = event.get("payload", {})
        if event.get("type") == "response_item" and (
                payload.get("role") == "assistant" or payload.get("type") in
                ("function_call", "custom_tool_call", "web_search_call", "local_shell_call", "reasoning")):
            return False
        if event.get("type") == "event_msg" and payload.get("type") in (
                "agent_message", "agent_reasoning", "exec_command_begin", "mcp_tool_call_begin", "web_search_begin"):
            return False
    return True


def host_recovery_preconditions(run, snapshot):
    require(len(batches(run)) == 1, "Host recovery is allowed only for batch 2")
    previous_batch, previous_meta = current(run)
    require(previous_meta["cli"] == str(CLI) and previous_meta["cli_version"] == "codex-cli 0.151.0",
            "Unexpected blocked first host")
    require(snapshot == previous_meta["candidate"] and snapshot["sha256"] == RECOVERY_CANDIDATE,
            "Host-only recovery requires the identical approved candidate")
    reserved = all_started(run)
    require(len(reserved) == 1 and reserved[0]["slot"] == "N01" and reserved[0]["batch"] == "batch-1",
            "Host recovery requires exactly the one consumed first N01 attempt")
    require(latest_states(previous_batch) == {"N01": "EXECUTION_ERROR"}, "Unexpected first-batch state")
    turn = previous_batch / "N01/turn-01"
    result = read(turn / "result.json")
    require(result["raw_rollout_captured"] and not result["turn_completed"] and result["returncode"] == 1,
            "First attempt must have preserved failed-turn evidence")
    rows = events(turn / "session-rollout.jsonl")
    require(rows and no_model_output(rows), "Host recovery cannot be used after model output/tool activity")
    message = "The 'gpt-6-astra' model requires a newer version of Codex."
    require(any(message in json.dumps(row) for row in rows), "Missing recorded host/model compatibility error")


def initialize_batch(args, run, data):
    candidate = Path(args.candidate).resolve()
    snapshot = tree(candidate)
    require(snapshot["sha256"] == args.package_validated, "Package validation hash does not match candidate")
    require(args.review_gate.strip(), "Explicit package review gate evidence is required")
    previous = batches(run)
    require(len(previous) < 2, "Two-batch limit reached")
    if previous:
        require(getattr(args, "host_recovery", False), "Only the explicitly authorized host-only recovery is permitted")
        require(args.repair_note and args.repair_note.strip(), "Host recovery requires bounded repair evidence")
        host_recovery_preconditions(run, snapshot)
    cli = RECOVERY_CLI if previous else CLI
    version, executable_sha = CLI_PINS[str(cli)]
    pins = {"cli": str(cli), "cli_version": version, "cli_sha256": executable_sha}
    verify_cli(pins)
    batch = run / f"batch-{len(previous) + 1}"
    batch.mkdir()
    shutil.copytree(candidate, batch / "candidate")
    require(tree(batch / "candidate") == snapshot, "Candidate copy mismatch")
    meta = {"at": now(), "candidate": snapshot, "source": str(candidate),
            "package_validated": args.package_validated, "review_gate": args.review_gate,
            "repair_note": getattr(args, "repair_note", None), "model": MODEL, "reasoning": "high",
            **pins,
            "host_recovery": bool(previous),
            "host_recovery_amendment_sha256": sha(FIXTURES / "host-recovery-v1.md") if previous else None,
            "repair_opportunity_consumed": bool(previous),
            "runtime_repair_permitted": False, "third_batch_permitted": False,
            "host": platform.platform(), "python": sys.version,
            "freeze_sha256": FREEZE_SHA, "fixture_version": data["version"],
            "budget": data["budget"], "source_commit": subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()}
    create_json(batch / "batch.json", meta)
    journal(run, "BATCH_INITIALIZED", batch=batch.name, candidate=snapshot["sha256"])
    print(json.dumps(meta, ensure_ascii=False, indent=2))


def stage_case(batch, slot, case):
    folder = batch / slot
    folder.mkdir()
    temporary = Path(tempfile.mkdtemp(prefix="fp-native-"))
    cwd, codex_home = temporary / "workspace", temporary / "codex-home"
    cwd.mkdir()
    codex_home.mkdir(mode=0o700)
    auth = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "auth.json"
    require(auth.is_file(), "Native auth.json unavailable; no session launched")
    # Authentication only. Never copy global config, skills, memories, or instructions.
    shutil.copyfile(auth, codex_home / "auth.json")
    (codex_home / "auth.json").chmod(0o600)
    shutil.copytree(batch / "candidate", cwd / ".agents/skills/fp")
    case_id = case["id"]
    if case_id == "N13":
        shutil.copytree(FIXTURES / "data/project", cwd, dirs_exist_ok=True)
    elif case_id == "N20":
        shutil.copyfile(FIXTURES / "data/injection/source.md", cwd / "source.md")
    require(not (cwd / "inaccessible-source.md").exists(), "N16 controlled source must remain absent")
    supplied = {str(p.relative_to(cwd)): sha(p) for p in sorted(cwd.rglob("*")) if p.is_file()}
    entry = cwd / ".agents/skills/fp/SKILL.md"
    meta = {"slot": slot, "case_id": case_id, "cwd": str(cwd), "cwd_resolved": str(cwd.resolve()),
            "codex_home": str(codex_home), "codex_home_resolved": str(codex_home.resolve()),
            "temporary_root": str(temporary), "staged_files": supplied,
            "expected_entry": str(entry), "expected_entry_resolved": str(entry.resolve()),
            "path_comparison": "Compare observed paths after Path.resolve(); /var and /private/var may identify the same file.",
            "context_description": case.get("context", []),
            "source_absent_before": not (cwd / "inaccessible-source.md").exists(),
            "auth": "Copied auth.json only; content never included in evidence"}
    create_json(folder / "case.json", meta)
    return folder, meta


def initial_prompt(case):
    prompt = case["initial_user"]
    if case["id"] == "N18":
        prompt += "\n\n<older-fixture-context source=\"data/profile.md\">\n"
        prompt += (FIXTURES / "data/profile.md").read_text()
        prompt += "</older-fixture-context>"
    return prompt


def compare_entry(meta, observed):
    path = Path(observed)
    if not path.is_absolute():
        path = Path(meta["cwd"]) / path
    expected = Path(meta["expected_entry"])
    return {"observed_entry": observed, "observed_entry_resolved": str(path.resolve()),
            "expected_entry": str(expected), "expected_entry_resolved": str(expected.resolve()),
            "same_resolved_entry": path.resolve() == expected.resolve()}


def select_branch(case, used, turn_index, branch_index, reason):
    require(1 <= branch_index <= len(case.get("followups", [])), "Unknown frozen branch")
    require(branch_index not in used, "Branch already consumed; no repeats/rescues")
    require(turn_index <= case["max_user_turns"], "Per-case turn budget exhausted")
    require(reason.strip(), "Reviewer semantic-match or scheduled-steering rationale required")
    return case["followups"][branch_index - 1]


def cleanup_auth(meta):
    # Session evidence contains no auth; remove the private temporary copy once
    # the case cannot resume. Retain staged source and host logs for inspection.
    auth = Path(meta["codex_home"]) / "auth.json"
    if auth.exists():
        auth.unlink()


def subprocess_turn(argv, prompt, cwd, env, out, err, timeout):
    with out.open("xb") as stdout, err.open("xb") as stderr:
        process = subprocess.Popen(argv, cwd=cwd, env=env, stdin=subprocess.PIPE,
                                   stdout=stdout, stderr=stderr, start_new_session=True)
        try:
            process.communicate(prompt.encode(), timeout=timeout)
            return process.returncode, False
        except (subprocess.TimeoutExpired, KeyboardInterrupt):
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.communicate(timeout=5)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.communicate()
            return 124, True


def capture_rollout(codex_home, thread, turn):
    pattern = f"**/*{thread}.jsonl" if thread else "**/*.jsonl"
    matches = list((codex_home / "sessions").glob(pattern))
    record = {"session_id": thread, "matches": [str(p) for p in matches],
              "matches_resolved": [str(p.resolve()) for p in matches]}
    if len(matches) == 1:
        shutil.copyfile(matches[0], turn / "session-rollout.jsonl")
        record["sha256"] = sha(turn / "session-rollout.jsonl")
        with (turn / "transcript.txt").open("x") as output:
            for n, raw in enumerate(matches[0].read_text(errors="replace").splitlines(), 1):
                try:
                    payload = json.dumps(json.loads(raw), ensure_ascii=False, indent=2)
                except ValueError:
                    payload = raw
                output.write(f"RAW LINE {n}\n{payload}\n\n")
    create_json(turn / "rollout-capture.json", record)
    return len(matches) == 1


def execute_turn(run, batch, folder, meta, case, prompt, turn_index, timeout, session=None):
    turn = folder / f"turn-{turn_index:02d}"
    turn.mkdir()
    batch_meta = read(batch / "batch.json")
    argv = configuration(case["id"], session, batch_meta["cli"])
    (turn / "prompt.txt").write_text(prompt)
    env = {key: os.environ[key] for key in ("PATH", "HOME", "TMPDIR", "LANG", "LC_ALL",
           "SSL_CERT_FILE", "SSL_CERT_DIR") if key in os.environ}
    env["CODEX_HOME"] = meta["codex_home"]
    create_json(turn / "invocation.json", {"argv": argv, "stdin": "prompt.txt", "cwd": meta["cwd"],
                "environment_keys": sorted(env), "CODEX_HOME": meta["codex_home"],
                "started": now(), "timeout_seconds": timeout})
    error = None
    try:
        verify_cli(batch_meta)
        rc, timed_out = subprocess_turn(argv, prompt, meta["cwd"], env,
                                       turn / "stdout.jsonl", turn / "stderr.txt", timeout)
    except Exception as exc:
        rc, timed_out, error = -1, False, repr(exc)
    stream = events(turn / "stdout.jsonl")
    thread = session or next((e["thread_id"] for e in stream if e.get("type") == "thread.started"), None)
    complete = any(e.get("type") == "turn.completed" for e in stream)
    captured = capture_rollout(Path(meta["codex_home"]), thread, turn)
    expected = read(batch / "batch.json")["candidate"]
    unchanged = tree(Path(meta["cwd"]) / ".agents/skills/fp") == expected
    current_files = {str(p.relative_to(Path(meta["cwd"]))): sha(p)
                     for p in sorted(Path(meta["cwd"]).rglob("*")) if p.is_file()}
    if timed_out:
        state = "TIMEOUT"
    elif error or rc or not complete or not thread:
        state = "EXECUTION_ERROR"
    elif not captured or not unchanged:
        state = "UNVERIFIED"
    elif turn_index < case["max_user_turns"]:
        state = "AWAIT_BRANCH"
    else:
        state = "OBSERVED"
    result = {"finished": now(), "returncode": rc, "timeout": timed_out, "error": error,
              "session_id": thread, "turn_completed": complete, "raw_rollout_captured": captured,
              "candidate_unchanged": unchanged, "workspace_files_after": current_files,
              "workspace_files_changed": current_files != meta["staged_files"], "state": state,
              "verdict": "NOT_GRADED"}
    create_json(turn / "result.json", result)
    if state != "AWAIT_BRANCH":
        cleanup_auth(meta)
    with locked(run):
        journal(run, "TURN_FINISHED", batch=batch.name, slot=meta["slot"], turn=turn_index, **result)
    for event in stream:
        item = event.get("item", {})
        if item.get("type") == "agent_message":
            print(item.get("text", ""), flush=True)
    print(json.dumps({"evidence": str(turn), **result}, ensure_ascii=False, indent=2))


def start_or_followup(args, run, data):
    case = slots(data).get(args.slot)
    require(case is not None, "Not an authorized slot")
    with locked(run):
        batch, batch_meta = current(run)
        verify_cli(batch_meta)
        require(tree(batch / "candidate") == batch_meta["candidate"], "Frozen candidate changed")
        states = latest_states(batch)
        running = sum(state == "RUNNING" for b in batches(run) for state in latest_states(b.parent).values())
        require(running < 2, "Two-concurrent-session limit reached")
        if states or args.command == "followup":
            provenance = events(run / "ledger.jsonl")
            require(any(e["event"] == "PROVENANCE" and e.get("batch") == batch.name and
                        e.get("decision") == "PASS" for e in provenance),
                    "First-session provenance gate not passed; no new session or followup permitted")
        if args.command == "start":
            require(args.slot not in states and not (batch / args.slot).exists(), "Slot already consumed/prepared; never overwrite or rerun")
            require(len(all_started(run)) < 52 and len(states) < 26, "Session budget exhausted")
            if not states:
                require(args.slot == "N01", "N01 is the first-session discovery gate")
            folder, meta = stage_case(batch, args.slot, case)
            prompt, index, session = initial_prompt(case), 1, None
            journal(run, "SESSION_RESERVED", batch=batch.name, slot=args.slot, state="RUNNING",
                    candidate=batch_meta["candidate"]["sha256"], case_id=case["id"])
        else:
            require(states.get(args.slot) == "AWAIT_BRANCH", "Case not eligible for a followup")
            folder = batch / args.slot
            meta = read(folder / "case.json")
            prior_turns = sorted(folder.glob("turn-*/result.json"))
            index = len(prior_turns) + 1
            used = {int(p.stem.split("-")[1]) for p in folder.glob("branch-*.json")}
            branch = select_branch(case, used, index, args.branch, args.reason)
            session = read(prior_turns[-1])["session_id"]
            prompt = branch["user"]
            create_json(folder / f"branch-{args.branch:02d}.json",
                        {"at": now(), "turn": index, "predicate": branch["when"], "reason": args.reason, "exact_user": prompt})
            journal(run, "FOLLOWUP_RESERVED", batch=batch.name, slot=args.slot, state="RUNNING", turn=index)
    execute_turn(run, batch, folder, meta, case, prompt, index, args.timeout, session)


def self_test():
    """Harness-only fake child and capture test: zero Codex/model invocations."""
    with tempfile.TemporaryDirectory(prefix="fp-harness-test-") as name:
        temp = Path(name)
        out, err = temp / "stdout.jsonl", temp / "stderr.txt"
        fake = "import sys,json; print(json.dumps({'type':'thread.started','thread_id':'fake'})); print(json.dumps({'type':'turn.completed'})); sys.stdin.read()"
        rc, timed_out = subprocess_turn([sys.executable, "-c", fake], "fixture", temp, os.environ.copy(), out, err, 5)
        require(rc == 0 and not timed_out and len(events(out)) == 2, "Fake subprocess logging failed")
        try:
            subprocess_turn([sys.executable, "-c", fake], "fixture", temp, os.environ.copy(), out, err, 5)
        except FileExistsError:
            pass
        else:
            raise RuntimeError("Overwrite protection failed")
        initial, resume = configuration("N14"), configuration("N14", str(uuid.uuid4()))
        for argv in (initial, resume):
            for required in ('sandbox_mode="read-only"', 'approval_policy="never"',
                             'model_reasoning_effort="high"', MODEL, "--ignore-user-config",
                             "skip_host_skill_discovery", "--search", 'web_search="live"'):
                require(required in argv, f"Missing configuration {required}")
        for session in (None, str(uuid.uuid4())):
            recovery = configuration("N14", session, RECOVERY_CLI)
            require(recovery[0] == str(RECOVERY_CLI), "Resume did not use the batch executable")
            require('model_reasoning_effort="high"' in recovery and MODEL in recovery,
                    "Host recovery changed model or reasoning")
        require(no_model_output([{"type": "response_item", "payload": {"role": "user"}}]), "User input mistaken for model output")
        for payload in ({"role": "assistant"}, {"type": "function_call"}, {"type": "reasoning"}):
            require(not no_model_output([{"type": "response_item", "payload": payload}]), "Model activity missed")
        source = temp / "sessions/rollout-fake.jsonl"
        source.parent.mkdir()
        source.write_text(json.dumps({"type": "session_meta", "payload": {"id": "fake"}}) + "\n")
        capture = temp / "capture"
        capture.mkdir()
        require(capture_rollout(temp, "fake", capture), "Rollout capture failed")
        require(sha(source) == sha(capture / "session-rollout.jsonl"), "Raw trace copy changed")
        alias = temp / "alias"
        alias.symlink_to(capture, target_is_directory=True)
        comparison = compare_entry({"cwd": str(temp), "expected_entry": str(capture / "session-rollout.jsonl")},
                                   str(alias / "session-rollout.jsonl"))
        require(comparison["same_resolved_entry"], "Filesystem alias normalization failed")
        slow = [sys.executable, "-c", "import time; time.sleep(20)"]
        rc, timed_out = subprocess_turn(slow, "", temp, os.environ.copy(), temp / "slow.out", temp / "slow.err", 0.05)
        require(rc == 124 and timed_out, "Timeout handling failed")
        blocked_run = temp / "blocked-followup"
        blocked_batch = blocked_run / "batch-1"
        (blocked_batch / "candidate").mkdir(parents=True)
        (blocked_batch / "candidate/SKILL.md").write_text("harness-only fixture")
        create_json(blocked_batch / "batch.json", {"candidate": tree(blocked_batch / "candidate")})
        journal(blocked_run, "TURN_FINISHED", batch="batch-1", slot="N01", state="AWAIT_BRANCH")
        before = (blocked_run / "ledger.jsonl").read_bytes()
        original_verify, original_execute = verify_cli, execute_turn
        invoked = []
        try:
            globals()["verify_cli"] = lambda meta: None
            globals()["execute_turn"] = lambda *args: invoked.append(True)
            args = argparse.Namespace(command="followup", slot="N01", branch=1,
                                      reason="scheduled steering", timeout=180)
            try:
                start_or_followup(args, blocked_run, fixtures())
            except RuntimeError as exc:
                require("provenance gate" in str(exc), "Followup blocked for the wrong reason")
            else:
                raise RuntimeError("Unreleased N01 followup was permitted")
        finally:
            globals()["verify_cli"], globals()["execute_turn"] = original_verify, original_execute
        require(not invoked and (blocked_run / "ledger.jsonl").read_bytes() == before,
                "Unreleased followup reserved a turn or invoked execution")
    data = fixtures()
    require(len(slots(data)) == 26, "Incorrect slot budget")
    require(initial_prompt(data["ordinary"]) == data["ordinary"]["initial_user"], "Ordinary prompt contamination")
    case = slots(data)["N04"]
    require(select_branch(case, set(), 2, 2, "evidence question") == case["followups"][1], "Flexible branch selection failed")
    require(select_branch(case, {2}, 3, 1, "meaning question") == case["followups"][0], "Unused branch selection failed")
    for used, turn, branch, reason in (({2}, 3, 2, "repeat"), (set(), 4, 1, "extra turn"),
                                     (set(), 2, 3, "unknown"), (set(), 2, 1, "")):
        try:
            select_branch(case, used, turn, branch, reason)
        except RuntimeError:
            pass
        else:
            raise RuntimeError("Invalid branch accepted")
    print("HARNESS_ONLY PASS: fake subprocess/logging, exclusive outputs, raw capture, initial/resume config, timeout, frozen inputs, 26 slots. No native session consumed.")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("self-test")
    commands.add_parser("hash").add_argument("--candidate", required=True)
    for command in ("init", "batch", "start", "followup", "stop", "provenance", "status"):
        p = commands.add_parser(command)
        p.add_argument("--run", required=True)
        if command in ("init", "batch"):
            for flag in ("candidate", "package-validated", "review-gate"):
                p.add_argument("--" + flag, required=True)
            p.add_argument("--repair-note")
            if command == "batch":
                p.add_argument("--host-recovery", action="store_true")
        if command in ("start", "followup", "stop"):
            p.add_argument("--slot", required=True)
        if command in ("start", "followup"):
            p.add_argument("--timeout", type=int, default=180)
        if command == "followup":
            p.add_argument("--branch", type=int, required=True)
        if command in ("followup", "stop"):
            p.add_argument("--reason", required=True)
        if command == "stop":
            p.add_argument("--status", choices=("OBSERVED", "AMBIGUOUS_FIXTURE", "BLOCKED"), required=True)
        if command == "provenance":
            p.add_argument("--decision", choices=("PASS", "BLOCKED", "UNVERIFIED"), required=True)
            p.add_argument("--observed-entry")
            p.add_argument("--evidence", required=True)
    args = parser.parse_args()
    if args.command == "self-test":
        return self_test()
    if args.command == "hash":
        return print(json.dumps(tree(Path(args.candidate).resolve()), indent=2))
    data = fixtures()
    run = run_path(args.run)
    if args.command == "init":
        # One campaign ledger controls BOTH batches; prevent a second run silently resetting budget.
        existing = [p for p in EVIDENCE.glob(RUN_PREFIX + "*") if (p / "ledger.jsonl").exists()]
        require(not existing, f"Campaign already exists: {existing}; use its bounded second batch")
        run.mkdir()
    require(run.is_dir(), "Run does not exist")
    if args.command in ("init", "batch"):
        with locked(run):
            return initialize_batch(args, run, data)
    if args.command in ("start", "followup"):
        require(1 <= args.timeout <= 180, "Timeout must be bounded to 1..180 seconds")
        return start_or_followup(args, run, data)
    with locked(run):
        batch, meta = current(run)
        states = latest_states(batch)
        if args.command == "provenance":
            require(states.get("N01") and states["N01"] != "RUNNING", "First native turn not available")
            require(not any(e["event"] == "PROVENANCE" and e.get("batch") == batch.name
                            for e in events(run / "ledger.jsonl")), "Provenance decision is immutable")
            require(args.evidence.strip(), "Trace paths/content/config evidence is required")
            comparison = compare_entry(read(batch / "N01/case.json"), args.observed_entry) if args.observed_entry else {}
            if args.decision == "PASS":
                require(comparison.get("same_resolved_entry"), "PASS requires the actual observed entry resolving to the staged candidate")
            journal(run, "PROVENANCE", batch=batch.name, decision=args.decision, evidence=args.evidence, **comparison)
        elif args.command == "stop":
            require(states.get(args.slot) == "AWAIT_BRANCH", "Only a case awaiting a branch can be stopped")
            journal(run, "CASE_STOPPED", batch=batch.name, slot=args.slot, state=args.status, reason=args.reason)
            cleanup_auth(read(batch / args.slot / "case.json"))
        else:
            print(json.dumps({"batch": batch.name, "candidate": meta["candidate"]["sha256"],
                  "global_sessions_consumed": len(all_started(run)), "global_sessions_remaining": 52 - len(all_started(run)),
                  "slots": {slot: states.get(slot, "NOT_RUN") for slot in slots(data)}}, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, OSError, ValueError) as exc:
        print(f"BLOCKED: {exc}", file=sys.stderr)
        sys.exit(2)
