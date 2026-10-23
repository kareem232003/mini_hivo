# Project-12 clarification repair — local candidate, incomplete live verification

23 October 2026, Africa/Cairo. No publication is authorized. This packet supersedes earlier **current-state conclusions**, while preserving their original files and source pins. See [R_UPDATE_003](../../../updates/R_UPDATE_003.md).

## What was established

The four stored user inputs are reproduced verbatim in [manual-inputs.json](manual-inputs.json). All four historical runs stopped at source ingestion with no model/Builder execution. The pre-edit [investigation](INVESTIGATION.md) explains the concrete parser/routing defects. Previous fixes were active: their six production source pins matched the checkout, including the mini.py hash in every project-12 run. No evidence supports stale source or cross-workspace leakage. Eight original project-12 files and the private ZIP remain hash-identical.

Structured blocks now compile exact file obligations. JSON maps may have introductory/trailing prose or appear inline. A JSON-looking file body remains literal data. Workspace-bound task identities/history distinguish independent tasks from answers. Partial answers retain the original file count and record supplied data; conflicts retain the original newline/count policy. Concatenated boundaries remain proposals requiring confirmation. The bounded literal scope is at most ten files, not unrestricted language interpretation.

## Functional evidence versus regression

[Four controlled CLI cases](controlled/) pass: concatenated original followed by the actual prose-wrapped JSON answer; the actual structured two-file input without clarification; the independent inventory task; Level 1. Each passes all thirteen independent trace/filesystem/database checks: exact bytes, context before mutation, impact authorization, Builder native proofs, every Falsifier read, required routes, impact comparison, transaction commit and verified completion. The two-file outputs are 47 and 63 bytes; Level 1 is 15 bytes. Host setup and model responses are scripted. These are **controlled functional**, not live-model successes. All seven production hashes match the final checkout at inspection.

The [controlled scale matrix](scale/) separately passes all independent checks at 1/2/3/4/5/8/10 artifacts with the final production pins. These scale requests use explicit canonical literal clauses; block syntax at those counts is covered separately by parser regression. Source spans describe the parsed input; original requests and actual clarification responses are retained separately to distinguish their provenance.

[Nine new regression tests](../../../tests/test_project12_clarification.py) exercise actual main, interactive input acquisition (scripted user device), persistent separate CLI invocations, the four-turn order, copied-state workspace isolation, partial/conflicting answers, inline JSON, literal JSON bodies and 1/2/3/4/5/8/10 block parsing. The interactive test invokes real handlers and gates, with only provider/environment/user input scripted. The four-turn replay differs legitimately from history: turn one now completes; replaying its answer at turn three is accepted but existing-file impact authorization blocks implicit overwrites. This is disclosed, not converted to a passing execution claim.

[Offline results](offline/results.json) preserve suite-level outcomes and source pins. Level 1 10, generalized recovery 20, prior clarification 9, new clarification 9, greenfield lifecycle 17, impact 27, context 9, applicability 15, authority 23, experiment 122, architecture 90, project understanding 32, model policy 4, requirement clarification 49 all pass separately. Counts are not summed across suites. One known live-provider test is explicitly excluded. Verification-policy: 8 executed, 2 errors from missing benchmark prompt. Recovery: 186 executed, 24 failure records, 2 errors, 3 skips. Failure/error identities match the preserved unchanged-base result. Old envelopes lack required evidence fields; downstream checks fail or dereference absent stage5b. Two tests require a historical absolute developer path. These baseline fixture/compatibility issues are retained, not patched to manufacture success; recovery production code is unchanged by this repair.

## Genuine local Ollama results

- First JSON continuation: host preflight `CRITICAL_MEMORY_HEADROOM`, one of three canaries; no task run ID.
- Inventory `20261023T000915-20404da5`: real host preflight passed, structured ingestion succeeded without clarification, then Specifier timed out after a recorded 120-second request. `failed`, `root_verified=false`, two model calls, zero tools/Falsifier/impact authorizations, 167.35 run seconds. Its source pins precede the final policy/JSON-body negative-case corrections. No output files were produced. Timeout establishes the provider boundary, not its internal cause.
- Level 1: host preflight `CRITICAL_MEMORY_HEADROOM`, zero canaries; no task run ID.
- One final reviewed-source JSON-continuation attempt: host preflight `CRITICAL_MEMORY_HEADROOM`, zero canaries; no task run ID. No further live retries.

See [live records](live/). Sanitized results retain separate source pins and actual outcomes. Host inventories are intentionally omitted; raw timing/resource evidence remains private. A process exit of zero is not a task PASS. Earlier successful runs `20261022T225748-a38c9d71` and `20261022T230703-c63e9980` remain historical checkpoint successes only.

**Verdict:** controlled repair verified within the documented bounded scope; final-source genuine Level 2 completion remains **UNVERIFIED / INCOMPLETE**. Stable host/provider operation and a successful final-source live workflow are required before claiming Level 2 PASS or advancing to Level 3. Replaying an already completed task still requires appropriate existing-file authority. Broad semantic interpretation and complex application reliability are unproven.

## Reproduce locally

Run from the repository root, using fresh output directories:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/verify_level2_offline.py --output-dir audit_runs/local-offline-new
.\.venv\Scripts\python.exe -B -X utf8 scripts/level2_clarification_replay.py --output-dir audit_runs/local-controlled-new --cases json-resumption structured-blocks inventory level1
```

The offline runner exits 1 while the disclosed baseline failures remain. Live execution is costly; after host qualification, the same replay command with `--live` uses real Ollama and unchanged security/resource gates. Do not rerun historical cohorts. `mini.py --no-bootstrap --workspace <workspace> --conversation-file <turns.json>` accepts a UTF-8 JSON array of complete multiline user turns through the normal controller, Specifier and execution gates; it does not confer authorization or bypass verification. Normal interactive usage remains supported.

[Manifest](manifest.json) validates 54 raw-source/sanitized-derivative pairs, with UTF-8/LF canonical derivatives. Originals, SQLite databases, raw conversations, backups and host inventories remain private. README and compact boundary summaries are authored metadata. Integrity, current source pins and the scoped path/credential privacy scan pass; diagnostic matches to JSON escapes were reviewed as harmless task text. Eight project-12 originals, its ZIP and the nine earlier project-10/11 originals rehash unchanged. Files remain unstaged/uncommitted; staged-blob validation is not applicable. Previously published raw Git history is not erased.
