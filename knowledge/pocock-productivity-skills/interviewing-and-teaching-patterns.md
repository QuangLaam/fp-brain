---
id: "interviewing-and-teaching-patterns"
title: "Interviewing and teaching patterns in Matt Pocock's productivity skills"
object_type: "concept"
domain: "agent-skills"
description: "How the grilling, to-questionnaire and teach skills interview a user and ground teaching, as stated in their own instructions."
when:
  - "designing how an agent skill interviews a user before acting"
  - "designing how an agent skill grounds and paces teaching"
trust_tier: "draft"
version: "1.0.0"
source_attribution:
  - uri: "_evidence/pocock-productivity-261118/sources/grilling.txt"
    sha256: "3e36fb03e17564daf0e08ca84d04800beffa3077d5ef2a8773af0a9c14c3d249"
  - uri: "_evidence/pocock-productivity-261118/sources/to-questionnaire.txt"
    sha256: "a897f12696142e6d5eb2bca4ebbc41f1518a627cfec6acc25668990f96d53029"
  - uri: "_evidence/pocock-productivity-261118/sources/teach.txt"
    sha256: "e2afd1eb3b32df76e6324233e465ac823df26c51211f0eddcbb436084ef2c678"
  - uri: "_evidence/pocock-productivity-261118/sources/teach-mission-format.txt"
    sha256: "746d59a79f007c484e0e61987766991d2f492c88685779b3eb6220a39a7793a9"
  - uri: "_evidence/pocock-productivity-261118/sources/teach-learning-record-format.txt"
    sha256: "d7fe13eaa812734fd5fe86fa35aa5b3da31f1c311d4e7f66342772ca56669330"
  - uri: "_evidence/pocock-productivity-261118/sources/teach-glossary-format.txt"
    sha256: "18d6740c8da7e792bb5b113c0cef3715207aa086e8fa616fe3e383f89543553a"
  - uri: "_evidence/pocock-productivity-261118/sources/teach-resources-format.txt"
    sha256: "79197f2e5ab824aef0b3f21317bca61451913c5e6b7dfbf3444edc368f5c7615"
link_types:
  - link_type: "cites"
    target_id: "grilling-interviews-until-shared-understanding"
  - link_type: "cites"
    target_id: "frontier-is-decisions-with-settled-prerequisites"
  - link_type: "cites"
    target_id: "ask-whole-frontier-with-recommended-answers"
  - link_type: "cites"
    target_id: "yes-accepts-the-recommendation"
  - link_type: "cites"
    target_id: "finding-facts-is-the-agents-job"
  - link_type: "cites"
    target_id: "decisions-belong-to-the-user"
  - link_type: "cites"
    target_id: "done-when-frontier-is-empty"
  - link_type: "cites"
    target_id: "no-action-before-user-confirms"
  - link_type: "cites"
    target_id: "questionnaire-interviews-only-about-the-send"
  - link_type: "cites"
    target_id: "one-idea-per-question"
  - link_type: "cites"
    target_id: "most-important-questions-first"
  - link_type: "cites"
    target_id: "teach-is-stateful-across-sessions"
  - link_type: "cites"
    target_id: "interview-before-writing-a-vague-mission"
  - link_type: "cites"
    target_id: "confirm-before-changing-mission"
  - link_type: "cites"
    target_id: "challenge-just-enough"
  - link_type: "cites"
    target_id: "lessons-are-short"
  - link_type: "cites"
    target_id: "difficulty-is-the-enemy-of-knowledge"
  - link_type: "cites"
    target_id: "difficulty-is-the-tool-for-skill"
  - link_type: "cites"
    target_id: "feedback-loop-as-tight-as-possible"
  - link_type: "cites"
    target_id: "record-prior-knowledge-to-avoid-reteaching"
  - link_type: "cites"
    target_id: "glossary-records-compressed-knowledge"
  - link_type: "cites"
    target_id: "knowledge-from-resources-not-parametric-guesses"
  - link_type: "cites"
    target_id: "no-mission-means-ungrounded-knowledge"
  - link_type: "cites"
    target_id: "bad-mission-worse-than-none"
  - link_type: "cites"
    target_id: "fluency-gives-illusory-mastery"
  - link_type: "cites"
    target_id: "coverage-is-not-learning"
  - link_type: "cites"
    target_id: "user-unclear-on-mission-question-the-why"
  - link_type: "cites"
    target_id: "teach-uses-directory-as-workspace"
---

## Purpose

Record, in the skills' own words, how three of Matt Pocock's productivity skills (grilling, to-questionnaire, teach) interview a user and ground teaching, as reference material for the FP skill's interview and learning-context design.

## When to Use / When NOT

Use it as a reference for what these skills instruct. It describes their instructions at one pinned commit; it does not evaluate whether the patterns work.

Do not treat it as a list of things to import into FP: this repository's rules keep file-writing behaviour out of FP. The teach skill treats the current directory as a teaching workspace.
<!-- ease:claim id=teach-uses-directory-as-workspace -->

## Core Knowledge Content

### Interviewing: the grilling skill

The grilling skill interviews the user relentlessly until a shared understanding is reached.
<!-- ease:claim id=grilling-interviews-until-shared-understanding -->

It works from a frontier: every decision whose prerequisites are already settled.
<!-- ease:claim id=frontier-is-decisions-with-settled-prerequisites -->

The whole frontier is asked in one round, with each question numbered and given a recommended answer.
<!-- ease:claim id=ask-whole-frontier-with-recommended-answers -->

Each question is worded so that "yes" accepts the recommendation.
<!-- ease:claim id=yes-accepts-the-recommendation -->

Finding facts is the agent's job, never the user's.
<!-- ease:claim id=finding-facts-is-the-agents-job -->

Decisions are the user's: each one is put to them and the agent waits.
<!-- ease:claim id=decisions-belong-to-the-user -->

The session is done when the frontier is empty, with every branch visited and nothing left silently assumed.
<!-- ease:claim id=done-when-frontier-is-empty -->

The agent does not act until the user confirms that a shared understanding has been reached.
<!-- ease:claim id=no-action-before-user-confirms -->

### Interviewing: the to-questionnaire skill

The to-questionnaire skill interviews the user only about the send: who it goes to and what they need back.
<!-- ease:claim id=questionnaire-interviews-only-about-the-send -->

Every question in the questionnaire is one idea, never compound.
<!-- ease:claim id=one-idea-per-question -->

Questions are ordered most-important-first, because an async questionnaire may get only one pass.
<!-- ease:claim id=most-important-questions-first -->

### Teaching: the mission

The teach skill treats a request as stateful: the user intends to learn over multiple sessions.
<!-- ease:claim id=teach-is-stateful-across-sessions -->

If the user is unclear about the mission, or `MISSION.md` is not populated, the first job is to question the user on why they want to learn this.
<!-- ease:claim id=user-unclear-on-mission-question-the-why -->

If the user cannot articulate why, the agent interviews them before writing anything.
<!-- ease:claim id=interview-before-writing-a-vague-mission -->

The agent confirms with the user before changing the mission.
<!-- ease:claim id=confirm-before-changing-mission -->

### Teaching: difficulty and pacing

In each lesson the user should feel challenged "just enough".
<!-- ease:claim id=challenge-just-enough -->

A lesson should be short and completable very quickly.
<!-- ease:claim id=lessons-are-short -->

Difficulty is treated differently for knowledge and for skill. For acquiring knowledge, difficulty is the enemy.
<!-- ease:claim id=difficulty-is-the-enemy-of-knowledge -->

For skill acquisition, difficulty is the tool.
<!-- ease:claim id=difficulty-is-the-tool-for-skill -->

The feedback loop should be as tight as possible, giving feedback immediately and ideally automatically.
<!-- ease:claim id=feedback-loop-as-tight-as-possible -->

### Teaching: what gets recorded

Disclosed prior knowledge is recorded so that future sessions do not re-teach it.
<!-- ease:claim id=record-prior-knowledge-to-avoid-reteaching -->

The glossary is a record of compressed knowledge, not a dictionary the user reads to learn.
<!-- ease:claim id=glossary-records-compressed-knowledge -->

Knowledge for explainers is drawn from `RESOURCES.md`, not from parametric guesses.
<!-- ease:claim id=knowledge-from-resources-not-parametric-guesses -->

## Failure Modes (Mandatory)

Teaching without the mission: failing to understand it means knowledge acquisition is not grounded in real-world goals.
<!-- ease:claim id=no-mission-means-ungrounded-knowledge -->

Writing a poor mission anyway: a bad mission is worse than no mission.
<!-- ease:claim id=bad-mission-worse-than-none -->

Mistaking fluency for mastery: fluency can give an illusory sense of mastery, while storage strength is the real goal.
<!-- ease:claim id=fluency-gives-illusory-mastery -->

Recording exposure as learning: merely covered material does not qualify for a learning record. Coverage is not learning; wait for evidence.
<!-- ease:claim id=coverage-is-not-learning -->
