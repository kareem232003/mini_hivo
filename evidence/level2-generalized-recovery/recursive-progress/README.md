# Recursive completed-context progress — incomplete local repair

23 October 2026, Africa/Cairo. [Chronological R_UPDATE_003](../../../updates/R_UPDATE_003.md) contains twelve numbered sections and appendices, retaining the previous report in full. No publication or Level 3 work is authorized.

## Confirmed cause and bounded repair

The default `execute_agent_task` context branch rebuilt the conversation and broke before generic artifact stall observation. `_context_tool_projection` kept offering the completed check. Stored JSON repeatedly says sufficient/MUTATION_ALLOWED with the same anchor; authorization/schema loss is unsupported. Internal model reasoning is unknown. Optional constrained-policy progress did not protect the default path. Model-driven baseline/recursive fit decisions are unchanged; no artifact-count routing workaround is added.

Production changes are confined to `mini.py`: remove the completed check from offered tools, preserve its result in the transcript, guide the next authorized action, and stop persistent out-of-schema repeats with `EXECUTION_STALLED`. No write is forced and no authorization proof is fabricated or cached. Existing constrained-policy classification is retained. This is a bounded safe-stop repair; it does not yet establish the requested general recovery, changed-evidence revalidation and full recursive acceptance matrix.

## Actual observations

- Project-15 `20261023T002611-991b46bd`: provider timeout, failed/root false, zero tools.
- Project-17: host-only OLLAMA_UNAVAILABLE/connection refused, zero canaries; no task run ID found.
- Project-18 `20261023T004235-79109aeb`: actual manual baseline PASS, nine model/seven tool calls, 385.02 seconds. Exact current files match 47/63-byte source oracles. Read-only inspection of retained trace/database and an isolated evidence copy passes native proofs, every Falsifier read, routes, impact comparison and transaction commit. Historical source identity is retained; this is not new-source completion. The host record is shared workspace state, not unique per-run session proof.
- Project-18 `20261023T005124-a828f3dd`: actual recursive failure, 28 successful context calls without mutation, then child budget exhaustion; later provider timeouts. Same workspace is proven; one OS/CLI session is not independently established. Provider-resource causation from the first child's delay is not proven.
- New genuine replay `20261023T012433-0023e35a`: host qualification passed, then Specifier timed out before Builder. Failed/root false, two model calls, zero tools/Falsifier/authorizations, 201.75 run seconds / 240.66 wall seconds. Pins precede the final constrained-policy compatibility correction. No further expensive live retries under the same boundary; no final reviewed-source live PASS claimed.

Exact retained requests/metrics are in [run-registry.json](run-registry.json). Private raw originals, their sixteen-file manifest/ZIP, full model traces and databases remain under `audit_runs/20261021-workspace-audit/level2-recursive-progress/`. All sixteen original files and the ZIP rehash unchanged.

## Tests and limits

Focused cohort: **66 tests, OK**, including new production Worker-loop repeat regression and existing context negatives, Level 1/Level 2, CLI and impact lifecycle tests. The repeated-provider regression proves a bounded classified stop and retained proof, not ROOT decomposition success. Ten tests in its file include nine inherited context cases; do not add overlapping counts as unique coverage.

The broader pre-compatibility run disclosed two new failures. The guard initially intercepted the constrained policy; it now defers to that policy. The adaptive test assumed the first tool message was a mutation result; it now selects the non-context result and retains the full MUTATION_RECOVERY assertion. **104 targeted compatibility tests pass** after these corrections; the earlier failed logs are preserved. The complete broad suite was not rerun after those corrections, so its old failure record is not relabeled all-pass. Baseline verification-policy 2 errors and recovery 24 failure records/2 errors/3 skips remain unchanged in the broad cohort.

Four final reviewed-source **controlled baseline CLI** runs pass all independent inspection checks: JSON continuation, structured two-file task, inventory and Level 1. Exact actual files, context-before-write, authorized impact, Builder proofs, every Falsifier read, routes, comparison and transaction commit pass. Their seven production source pins match this checkpoint. Provider/environment responses are scripted. These do not prove recursive scheduling or live reliability.

**Remaining closure work:** actual ROOT-decomposition repeated-check regression; complete recursive 1/2/3/4/5/8/10/dependency/partial-failure matrix; material-change proof invalidation; alternating-action progress; same-session recursive continuation; final-source baseline and distinct recursive live successes. These are unverified, not completed requirements. Level 2 remains INCOMPLETE.

## Integrity and reproduction

[Manifest](manifest.json) distinguishes private source hashes and sanitized derivative hashes; canonical copies are UTF-8/LF. Registry/observations/README are authored summaries. Raw runtime state and machine details are excluded. Existing historical evidence packets are not regenerated.

Run `.\.venv\Scripts\python.exe -B -X utf8 scripts/verify_level2_offline.py --output-dir <fresh-directory>` from the root; it excludes a known live-provider test and retains baseline errors. Focused regression file: [test_context_completed_progress.py](../../../tests/test_context_completed_progress.py). Live replay is costly and requires retained source pins, host qualification and independent actual artifact inspection. Current publication remains unauthorized; no staging, commits, pushes, branch-ref or PR changes occur.
