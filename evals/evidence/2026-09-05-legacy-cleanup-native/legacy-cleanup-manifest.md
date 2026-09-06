# FP global legacy cleanup manifest

Date: 2026-09-05  
Scope: the eight exact targets authorized by the user. No backup of these
targets was created.

## Preconditions

- Repository: `/Users/quanglaam/fp-brain`
- Branch text: `main`
- Commit: none; `git rev-parse HEAD` failed because this repository has no
  commit yet.
- Baseline working tree: all repository files were already untracked.
- All eight targets were real directories, not symlinks.
- No symlink existed anywhere inside any of the eight targets.
- The seven public target directories each contained only one `SKILL.md`.
- `_fp-brain-runtime` contained 32 files and four child directories.

## Target identity before deletion

The directory digest is SHA-256 over the sorted output of `shasum -a 256` for
every regular file below that exact target. It is an identity digest, not a
claim that directory metadata is content-addressed.

| Exact target | Identity observed | File/content SHA-256 | Directory digest |
|---|---|---|---|
| `/Users/quanglaam/.agents/skills/fp-ask` | Legacy global pointer to missing rebuild paths `FP_KERNEL.md` and `commands/ask.md`; one file | `35df1cb4995568a613443e2927acc8fea0ef4edc67d01adcb6395b70058d65c2` | `8ed17688a826813d574d5c63ab7769aaa479bd4d9cde2bd36e4cabec18f0acb7` |
| `/Users/quanglaam/.agents/skills/fp-brainstorm` | Legacy global pointer to missing rebuild paths `FP_KERNEL.md` and `commands/brainstorm.md`; one file | `ad214fe7a565dd8f9e94e545902d8d726e1e3d1c494be9a9e71b8b48d9ef3f61` | `d6a171c1994254c96384e6a3f6af5e22f7f691cd372ba1728e47edbe2e7b8a03` |
| `/Users/quanglaam/.agents/skills/fp-decide` | Legacy global pointer to missing rebuild paths `FP_KERNEL.md` and `commands/decide.md`; one file | `7855e0e72975c7c041269123fbdcac7585b9e6c3dbb98caa652c93caf7605654` | `4542c5fe626dc7849c057d3e98d5676af8e4e4fa4370139fd67d3ac2592e8167` |
| `/Users/quanglaam/.agents/skills/fp-learn` | Legacy global pointer to missing rebuild paths `FP_KERNEL.md` and `commands/learn.md`; one file | `bbcdafb66d38fb6bf1e4874aa666db8517024af5057bd5f600ebd5edd1c15ac1` | `30aff849bb45e3b2c896dc1c590197c037921205f456acf4483f192a61dbaeed` |
| `/Users/quanglaam/.agents/skills/fp-debug` | Retired legacy global pointer to missing rebuild paths `FP_KERNEL.md` and `commands/debug.md`; one file | `fd18302d238f3c369092a24207beb7caad6015c66c7fbcc97c972acb03f57425` | `d92e683e89b0f93d464a215e684affc140bbab56f52c07ff61cc44345fe7971c` |
| `/Users/quanglaam/.agents/skills/fp-execute` | Retired legacy global pointer to missing rebuild paths `FP_KERNEL.md` and `commands/execute.md`; one file | `32b92c083eceb2a3593a757c197ff7c38488ead9fb267c22fdf9c62a39d9f1d9` | `75bedd744a13ef88fa994da9f65dec077a593e747cebfd3994d22eba08736cab` |
| `/Users/quanglaam/.agents/skills/fp-grill` | Retired legacy global pointer to missing rebuild paths `FP_KERNEL.md` and `commands/grill.md`; one file | `487f1fe58956cb17f80c1798e64fa7e816a01223564cb2f41a4c0cdea24280eb` | `2459b2f73988f1cddab2b340646236bb93b6fdf8c520ceeae8ce7576106f037f` |
| `/Users/quanglaam/.agents/skills/_fp-brain-runtime` | Legacy kernel/commands/workflows runtime loaded by the prior Learn probe; 32 files | root kernel `e9bb5a7526a57990f6ab05eedc6f546162fe6d9fd386317f1f7fe4ae1b4acb88` | `6e12e866b80516b580fe91da8ee26a64cd40a94309ed114223d731476caf7675` |

## Rebuild source baseline

```text
a8755c07fd8e3526b8d04ec476b44dbcd10ef2511b82cc6a84b1f218a4e86485  /Users/quanglaam/fp-brain/method/CORE.md
a694b44cef91701a13c452b8ecff4a53552ae8fbaf4fdf8cec886da49da597e2  /Users/quanglaam/fp-brain/.agents/skills/fp-ask/SKILL.md
9538c06c59a3b31da9700835454b1059c4e672142bef01b16391b4d119bcc38d  /Users/quanglaam/fp-brain/.agents/skills/fp-brainstorm/SKILL.md
e2408f76b4320ddf7278f9ed125f5536c669b1dd1cbe529c36663c24755d8d75  /Users/quanglaam/fp-brain/.agents/skills/fp-decide/SKILL.md
c37af668e14546c18a698e00ba68c7fa7b16cab504ab4f62027c248fe8c37905  /Users/quanglaam/fp-brain/.agents/skills/fp-learn/SKILL.md
```

## Completion verification

All eight exact targets were absent after deletion and remained absent after
the native runs. No backup was created. The four protected roots listed in the
task remained present. All nine files under `method/` and `.agents/skills/`
retained their exact baseline hashes after cleanup and testing.
