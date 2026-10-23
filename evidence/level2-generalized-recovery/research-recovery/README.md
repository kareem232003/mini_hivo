# Research-informed recovery — LOCAL, INCOMPLETE

See [R_UPDATE_003 research phase A–J](../../../updates/R_UPDATE_003.md#research-informed-recursive-execution-and-recovery-investigation) for the three-paper review, source-level findings, engineering comparison, implementation, test commands and issue register. Earlier phases and originals are preserved.

The adopted adaptation is bounded controller feedback about a real completed prerequisite, combined with dependency-bound revocation and child source-scope filtering. It adds no model/framework dependency and does not choose or perform a write. Literature motivates the design; only our tests establish its behavior.

## Latest controlled outcomes

[Final reviewed child-scope cohort](offline-child-scope-final/results.json) records exact test/production hashes:

| Suite | Executed | Outcome |
|---|---:|---|
| Context completed progress | 11 | All pass; includes inherited context cases, persistent repeats and external dependency drift |
| Context recovery functional | 4 | **3 pass, 1 fails** at parent integration |
| Dependency scheduler | 9 | All pass; injected leaf results are distinguished from real leaf tests |
| Level 1 / generalized Level 2 | 10 / 20 | Each suite passes |
| Prior clarification / project-12 clarification | 9 / 9 | Each suite passes |
| Greenfield lifecycle / impact / context / applicability | 17 / 27 / 9 / 15 | Each suite passes |
| Authority / experiment / architecture | 23 / 122 / 90 | Each suite passes |
| Project understanding / model policy / requirement clarification | 32 / 4 / 49 | Each suite passes; known live-provider case excluded |
| Verification-policy | 8 | 2 missing-fixture errors |
| V26 recovery | 186 | 24 failure records, 2 errors, 3 skips |

Counts are per suite, not summed; inherited/overlapping coverage exists. Full runner exits 1. Baseline failure identities are compared with retained results, not manufactured fixtures. **One new parent integration acceptance failure remains.** It is not marked expected/skipped or counted as a success.

The baseline recovery case actually creates exact files, verifies them natively, runs Falsifier and completes transaction/impact gates at 1/2/3/4/5/8/10 artifacts. Model responses are scripted to choose a legal write after one redundant prerequisite; this establishes controller recovery when a valid next proposal arrives, not live-model reliability.

The persistent-provider recursive test exercises real `_execute_children`, real leaf execution and gate handling, and cannot mark ROOT done after failed required work. The productive recursive test independently checks three child files/statuses before asserting parent completion. Child literal postconditions are now scoped, and all three children finish; **parent integration fails with IMPACT_CONTRACT_INCOMPLETE because its existing artifacts lack an appropriate integration contract**. That is the next blocking implementation boundary. No existing-file authorization restriction is relaxed to obtain a pass.

Material dependency drift is detected before a tool dispatch, revoking permission with a specific stale-proof summary. The current action is a safe stop requiring refreshed node validation; automatic in-place revalidation and successful general recovery after arbitrary changes are unfinished. Full ROOT decomposition and dependent-artifact matrices, alternating-action progress and same-session recursive continuity remain unverified.

## Genuine provider evaluation

The selected reviewed-source two-file baseline attempt failed host preflight: `CANARY_PROVIDER_FAILURE`, zero of three canaries, no task run ID, no outputs. [Attempt record](live-final-reviewed/structured-blocks/result.json). Its pins precede the final child-scope correction. Current final-source live completion is **unverified**. Further expensive inventory/alternative recursive attempts were not started under the same provider blocker and known deterministic parent failure.

[Provider comparison](provider-comparison.json) retains timestamps/context sizes for the manual baseline, recursive failure and Specifier timeout. The timed-out Specifier used about 1350 estimated tokens and a 4096 context window; configured timeout remains 120 seconds. Exact per-request loading/memory telemetry is unavailable. The role-keyed extractor only retains the latest unmatched request per role; do not interpret that list as the total timeout count. Original traces and historical metrics remain authoritative.

## Preservation, scope and manual reproduction

Projects 19/20 contained three retained files; their original hashes and ZIP validate unchanged. New source/derivative [manifest](manifest.json) validates 26 pairs; public candidates omit raw databases, host inventories and machine paths. Research references and author metadata are in the report. Registry and change manifest are authored summaries. Prior evidence packets are not regenerated.

This phase changes `mini.py`, `hivo/context_sufficiency.py`, existing `tests/test_context_completed_progress.py`, new `tests/test_context_recovery_functional.py`, `scripts/verify_level2_offline.py`, `.gitignore`, the same R_UPDATE_003 and this evidence packet. No stage, commit, push, branch-ref/PR changes or Level 3 work.

From the repository root:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/verify_level2_offline.py --output-dir audit_runs/manual-offline-fresh
.\.venv\Scripts\python.exe -B -X utf8 mini.py --no-bootstrap
```

Use fresh workspaces. Exact original tasks are in the retained registry. Do not overwrite historical project-18. Wait for provider qualification and parent integration repair before interpreting another recursive live run as a readiness test. The offline command intentionally fails while the parent acceptance and baseline fixture failures remain.
