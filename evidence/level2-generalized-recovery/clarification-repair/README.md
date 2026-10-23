# Local clarification and Falsifier coverage repair

This directory supersedes the earlier checkpoint for current-source claims while preserving that checkpoint unchanged. All work remains local, unstaged and uncommitted. No GitHub PR was modified.

## Why another correction was needed

Failures B `20261022T223807-7d3afde8` and C `20261022T224051-03e24342` stopped at source ingestion with no model/tool/Builder calls. The early guard rejected both concatenated source and the requested JSON answer. A pending question was not persisted or resumed across `You>` turns. [Historical observations](failures-b-c-summary.json) retain those boundaries without publishing raw traces/databases.

The production repair preserves original request/hash/ledger, proposes source-grounded line boundaries without authorizing inferred bytes, accepts an ordinary confirmation or validated JSON answer, persists partial answers, rejects conflicts/changed filenames/line-count violations and resumes normal context/impact execution. Extra JSON-tail instructions are rejected rather than silently discarded. The parser supports bounded instruction aliases, including informal English and ordinary Arabic word order; this is not general semantic language understanding.

The ten-file coverage gap is corrected: after model probes, missing current literal Falsifier reads use guarded `run_file`, retain failure evidence, count actual tool work and produce per-artifact receipts. Model budgets and command restrictions remain unchanged. This mechanism is distinct from claiming the model itself independently chose every read.

## Controlled functional and regression evidence

- [Four actual CLI conversations](controlled-cli/json-resumption-inspection.json): original plus ordinary confirmation, original plus next-turn JSON, structured two-file input, and Level 1. Providers and host setup are scripted; actual `main`, `You>` input loop, context/impact gates, tools, filesystem, Falsifier, final routes and transactions execute. The two-turn cases record `clarification_required` then `done`, preserving original provenance and one accepted answer.
- [Current scale matrix](controlled-matrix.json): 1, 2, 3, 4, 5, 8 and 10 artifacts pass independent exact-byte, native proof, every-artifact Falsifier, route, post-state and transaction inspection.
- [Source-pinned offline results](offline/results.json): nine clarification lifecycle tests, twenty generalized tests and ten Level 1 tests pass. Additional lifecycle/impact/context/applicability/authority/experiment/adaptive/project/model/requirement suites pass separately. The known live-calling requirement case remains explicitly excluded.
- Verification-policy remains failed with two missing-fixture errors. Recovery remains failed: 186 tests, 24 failure records, two errors, three skips, matching the unchanged-base failure/error identities. No full-suite green claim or overlapping-suite total is made.
- [Development counterexample](development-ten-file-missing-coverage.log) preserves the initial stronger ten-file assertion failure before correcting the cleared-active-contract lookup. It is not a current passing result.
- [Review counterexamples](development-clarification-projection-and-count.log) preserve two initial failures: standard Source Contract answers were not projected from accepted state, and a partial reply could waive file count without numbered file blocks. Both have dedicated passing assertions in the final nine-test lifecycle suite. Final source preserves explicit file count as well as line count and named obligations.

## Genuine Ollama attempts

See [live outcomes](live-outcomes-summary.json) and the individual records under `live-cli/`. These are actual local `gemma4:e4b` CLI processes with real host preflight and auto routing; no provider functions are patched. Each uses a fresh workspace and a 720-second outer wall interruption limit; application budgets are unchanged. Failed preflight, provider failures and incomplete executions remain failures/unverified, regardless of controlled success. The earlier successful run `20261022T020137-6b8c1201` validates an earlier source and is not a PASS of this repair.

The first new cohort precedes the final answer-projection/file-count corrections. Its structured two-file PASS (`20261022T225748-a38c9d71`) and Level 1 PASS (`20261022T230703-c63e9980`) retain their exact pre-review pins and independent inspections. They validate those unchanged execution paths at that checkpoint; their hashes are not relabeled as final. The two clarification cases have at most one bounded retry each under final source pins. These mixed attempts/source checkpoints are not a reliability denominator.

**Final-source live verdict: not yet a complete Level 2 PASS.** Ordinary confirmation was accepted in `20261022T231710-80240587`; recursive execution reached child-1 Builder, then the 720-second outer limit interrupted the process. No completed application metrics were saved for that turn. Its raw driver record contains the preceding clarification turn's metrics (`20261022T231710-a834c0f2`); the derived summary explicitly separates latest trace identity from last completed metrics. The driver now labels this scope for future interrupted replays.

JSON resumption `20261022T232911-4d8ce697` accepted one answer without reasking, then failed on a local Ollama Specifier timeout: two model calls, zero tools, root false, 181.22 seconds. Its persisted standard Source Contract answer fields contain the accepted answer. Both failures remain failures/unverified completion, despite the controlled successes. There were no further retries. Provider responsiveness and practical recursive-path completion need investigation under stable conditions; neither bypassed preflight nor larger budgets were used.

## Reproduce locally

```powershell
.\.venv\Scripts\python.exe -B -X utf8 mini.py --no-bootstrap
# Paste the original request at You>, then answer its preview with yes or corrected contents.

.\.venv\Scripts\python.exe -B -X utf8 scripts/level2_clarification_replay.py --output-dir output/new-cli-controlled
.\.venv\Scripts\python.exe -B -X utf8 scripts/level2_recovery_replay.py --artifacts 10 --output-dir output/new-ten
.\.venv\Scripts\python.exe -B -X utf8 scripts/inspect_level2_replay.py --run-dir output/new-ten --output-file output/new-ten-inspection.json
.\.venv\Scripts\python.exe -B -X utf8 scripts/verify_level2_offline.py --output-dir output/new-offline
# Only when live testing is authorized and host/model resources are stable:
.\.venv\Scripts\python.exe -B -X utf8 scripts/level2_clarification_replay.py --live --output-dir output/new-cli-live
# Select a bounded subset without rerunning completed cases:
.\.venv\Scripts\python.exe -B -X utf8 scripts/level2_clarification_replay.py --live --cases original-confirmation json-resumption --output-dir output/new-clarification-live
```

Output directories/files must not already exist. The offline command exits nonzero for disclosed historical failures. Keep raw output private. [Source pins](source-pins.json), [manifest](manifest.json) and [preservation summary](preservation-summary.json) distinguish raw source hashes, canonical sanitized derivatives and untouched originals. No staged-blob integrity check is claimed because staging is prohibited.

Exported contracts and provenance are evidence, not reusable runtime authorization.

## Remaining boundaries

Unsupported language/ambiguous byte boundaries still require clarification; missing values are not invented. Confirmation accepts only the shown preview; JSON replies must agree with original filenames and line counts and cannot silently change previously accepted content. Existing user-owned files are not automatically authorized for overwrite. Progress proofs remain transaction/attempt-local. Higher-level application behavior and live reliability are unproven. Earlier public Git history is unchanged.
