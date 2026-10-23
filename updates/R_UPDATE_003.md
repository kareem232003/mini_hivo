# R_UPDATE_003 — Chronological engineering investigation

Current publication checkpoint: [Latest manual evidence, comparison, current status and exit criteria](#publication-checkpoint--complete-current-state-phase-hi-and-review-boundary). This Draft checkpoint is authorized for publication; earlier LOCAL ONLY/unauthorized statements describe their historical phases. Level 2 remains INCOMPLETE.

Previous checkpoint: [Research-Informed Recursive Execution and Recovery Investigation](#research-informed-recursive-execution-and-recovery-investigation). Earlier current-state wording retains its checkpoint scope.

## 1. Executive Overview

23 October 2026, Africa/Cairo. **INCOMPLETE; LOCAL ONLY.** Level 2 evaluates source-grounded multi-artifact execution through context, impact authorization, native mutation, independent verification and final transaction gates in both baseline and recursive paths. Earlier controlled passes did not establish recursive live reliability. Manual two-file PASS and three-file FAIL are both retained. This phase implements completed-context tool projection, transcript preservation and a bounded safe stop; it does **not** establish general recursive recovery or Level 2 readiness. No R_UPDATE_004 or Level 3 work is created.

Navigation: sections 2–5 cover historical phases; 6–7 current investigation/repair; 8–9 tests; 10–12 comparison, issues and readiness. Appendices link detailed earlier A–M records, the run registry and private original traces.

## 2. Initial Baseline and Original Failure

`20261022T005130-de9aff61` (project-10) exhausted the tool budget after rejected shell verification, repeated writes/reads and no final Falsifier. Original rollback means current files cannot prove that historical output; retained database readbacks are separate evidence. The complete original request and initial observations remain in historical section B below. Later summaries must not replace its exact request or invent unavailable output bytes.

## 3. First Repair Phase

Historical sections D–G retain confirmed findings, source parsing/literal obligations, guarded native recovery, exact Windows writes, digest-bound progress and complete route/Falsifier coverage. Production modules: `mini.py`, `hivo/artifact_progress.py`, `hivo/requirements.py`, `hivo/pre_mutation_impact.py`, `hivo/verification_routing.py`. Controlled scale checks pass at their own pins; historical live successes are not current-source proof. Budgets and shell restrictions were not relaxed. Earlier ten-file partial coverage and its later controlled correction remain recorded separately.

## 4. Second Repair Phase: Manual Clarification Failures

Project-11 failures `20261022T223807-7d3afde8` and `20261022T224051-03e24342`, followed by project-12 `20261022T234739-c8d73cc5`, `20261022T234812-4819d2e2`, `20261022T235215-179d65fd`, `20261022T235253-8db69c4f`, exposed block grammar, prose-wrapped JSON and pending-task routing defects. Prior fixtures used accepted canonical/object-first forms. Shared `literal_source.py`, durable `literal_clarification.py` task association and actual CLI tests corrected those controlled paths. See the preserved project-12 checkpoint below and [its evidence](../evidence/level2-generalized-recovery/project12-repair/README.md). Provider-blocked runs and final-source limits remain disclosed. No cross-workspace leak was established.

## 5. Third Phase: Real Ollama Manual Validation

Model: local `gemma4:e4b`. Exact requests and metrics: [run registry](../evidence/level2-generalized-recovery/recursive-progress/run-registry.json).

| Attempt | Workspace / outcome | Boundary |
|---|---|---|
| `20261023T002611-991b46bd` | project-15, failed/root false, 2 model calls, 0 tools, 172.85 seconds | Provider timeout; no execution proof. |
| Project-17 host failure | No task run ID found | `OLLAMA_UNAVAILABLE`, connection refused, 0/3 canaries. Host timestamps identify the attempt, not a fabricated task ID. |
| `20261023T004235-79109aeb` | project-18, automatic baseline, done/root true, 9 model calls, 7 tools, Falsifier 1, 385.02 seconds | Structured exact two-file task succeeded. Current preserved student/course files independently match 47/63 expected UTF-8 bytes. |
| `20261023T005124-a828f3dd` | project-18, automatic recursive, failed/root false, 39 model calls, 28 tools, 1077.97 seconds | Three source requirements; three children; child 1 repeated sufficient context 28 times without mutation; later children timed out. No Falsifier. |

Both project-18 runs are in the same workspace ledger/database, with successive timestamps. This establishes workspace reuse, not conclusively one OS process or interactive session. Project mode/session causal effects are not proven. Prior task artifacts survive the failed task; no cross-workspace contamination is inferred. See original success trace (private local original: `list/project-18/.agent_runs/20261023T004235-79109aeb.jsonl`; see the linked curated phase summaries), failure trace (private local original: `list/project-18/.agent_runs/20261023T005124-a828f3dd.jsonl`; see the linked curated phase summaries) and private backups under the phase audit directory. Raw database/host records remain private.

## 6. Fourth Phase: Recursive No-Progress Investigation

`main`/request routing → `get_goal_contract`/literal compilation → project classification and automatic fit → recursive child scheduler → Worker mission → `execute_agent_task` → `_context_sufficiency_tool`/`ContextSufficiencyGate.evaluate` → impact activation → Builder continuation → verification/Falsifier/final transaction.

Confirmed production defects:

1. `_context_tool_projection` always inserted `context_sufficiency_check` even after mutation authorization. Only the optional `progress_constrained` path explicitly removed it.
2. In `execute_agent_task`, `if context_tool_call` rebuilt messages from the base mission and bounded feedback, then broke the tool loop. The complete tool response just appended to messages was discarded under the default path. The original mission's check-context instructions were reintroduced. Stored tool responses prove valid JSON, stable anchor hash and `mutation_allowed=true`; authorization loss/schema failure is unsupported.
3. That early break occurs **before** the generic `artifact_progress.observe` and duplicate-action guard. The optional Worker-progress policy was not the active default. Thus a successful but redundant prerequisite escaped the existing stall observer entirely. No repeated-failure hint activated because the checks succeeded.
4. Budget exhaustion reached diagnosis without an explicit stall event and was classified unknown/low confidence. The existing diagnosis function recognizes `execution_stalled` once emitted.

The trace proves repeated tool selection; it cannot prove the model's internal reason for doing so. Transcript loss/repeated schema exposure are controller defects, not proof that the model never understood any feedback. Baseline versus recursive is a route/mission/state difference, not evidence that a three-file threshold itself is defective. The unchanged model-driven mode selection is not replaced by a baseline workaround.

Children 2/3 have explicit provider timeout failure evidence before productive execution. Their `ENVIRONMENT_ERROR` classification is supported at that boundary. The first child's loop consumed time, but causal resource starvation of later children is unproven. No timeout is relabeled an orchestration loop or vice versa. Previous controlled tests scripted a useful next tool after the first successful check; they omitted an obstinate provider repeating the completed prerequisite on the default child path.

## 7. Fourth Phase: Implementation Changes

| Production function | Change / safety / coverage |
|---|---|
| `mini.py::_context_tool_projection` | Remove completed context check from offered tools while the actual gate reports mutation allowed; unsatisfied gates retain it. No approval is synthesized. Existing impact projection still applies. |
| `mini.py::execute_agent_task`, completed-context continuation | Preserve the actual tool result and append explicit next-step guidance instead of rebuilding the mission after a successful check. Reject persistent out-of-schema completed-check selection with bounded `EXECUTION_STALLED`. No mutation is forced. |
| Same function, identity/diagnostics | Observe anchor, working evidence, contradictions, approved inspection fingerprints, impact hash and execution contract for completed-check identity; emit a specific stall event. This is not reusable authorization caching. |

Tests: new `tests/test_context_completed_progress.py`, inherited context gate negative/positive cases, existing Level 1/Level 2/impact lifecycle tests. Offline runner includes the new file. **Limit:** broader changed-state revalidation, alternating-operation progress, recursive decomposition/dependency/child-integration coverage and successful generalized recovery are not established by this bounded safe-stop repair. They remain closure work, not completed architecture claims.

## 8. Controlled Regression Results

Fresh focused command and raw log: `audit_runs/20261021-workspace-audit/level2-recursive-progress/focused-results.log`. Python unittest discovery selects `test_context_completed_progress.py`, `test_level1_native_verification.py`, `test_level2_generalized_recovery.py`, `test_project12_clarification.py`, `test_greenfield_impact_lifecycle.py`, with fresh workspace-local temporary directories. **66 executed, OK**. Inherited context tests contribute repeated coverage; this is not a unique-coverage sum.

The new regression supplies 28 context-check responses with varied free-text reasons to the production Worker loop and real gate. It asserts fewer than 28 provider turns, failed status with explicit `EXECUTION_STALLED`, retained JSON proof in the next transcript, and no fabricated output. This demonstrates a safe stop, not recursive task success. It does not yet construct ROOT decomposition or prove successful recovery across children.

The broader pre-compatibility cohort exposed two new failures: constrained-policy failure classification was intercepted by the new guard, and a mutation-recovery test selected the first tool message (now a retained context proof). The guard now defers to the existing constrained policy; the test selects the actual non-context mutation result without weakening its recovery assertion. A targeted compatibility rerun passed 104 tests (overlapping inherited coverage); original failure logs remain. Four final-source controlled CLI cases pass independent inspection; they run baseline, not recursive ROOT decomposition. Broader offline command: `.\.venv\Scripts\python.exe -B -X utf8 scripts/verify_level2_offline.py --output-dir <fresh-directory>`. Final cohort is retained under the current phase audit directory. Historical baseline: verification-policy 2 fixture errors; V26 24 failure records, 2 errors, 3 skips. Missing fixtures and old envelope/path assumptions remain disclosed; do not infer full-suite success. Earlier controlled artifact-count 1/2/3/4/5/8/10 results have separate source pins and are not automatically refreshed by this phase.

## 9. Final-Source Real Ollama Results

One bounded genuine inventory replay used the production repair before the final constrained-policy compatibility correction, via the ordinary CLI and host qualification. It is not a final reviewed-source PASS. Record: `audit_runs/20261021-workspace-audit/level2-recursive-progress/live-final/inventory/result.json`, with source hashes, exact turns, task metrics and actual output oracle. Observed run `20261023T012433-0023e35a`: failed/root false after Specifier timeout, 2 model calls, 0 tools/Falsifier/impact authorizations, 201.75 run seconds / 240.66 wall seconds. No outputs. See phase README for source pins. No final-source PASS is asserted unless exact bytes, independent Falsifier, impact comparison and final transaction all succeed. Additional scenarios are not counted as executed merely because requested.

## 10. Comparative Analysis

Initial execution lacked source-bound native obligations; first repairs established them in controlled baseline paths. Manual clarification exposed missing source representations and task association; second repairs addressed those separately. Real two-file baseline then genuinely passed. Real three-file recursive execution exposed a different completed-prerequisite branch that bypassed stall observation. The new Worker test reaches that branch and proves bounded stopping with retained proof; **general recursive completion is still unverified**. Neither a controlled stop nor the older two-file PASS closes that gap.

## 11. Outstanding Problems and Risks

| ID | Severity/status | Evidence / next engineering action / closure test |
|---|---|---|
| RP-1 | High, confirmed incomplete | Default completed-check loop is bounded, but generalized authorized recovery requires actual ROOT/child CLI regressions, dependencies and partial child failure tests. |
| RP-2 | High, unverified | Material-state invalidation and alternating no-progress actions need dedicated tests before claiming a general progress architecture. No cached proof reuse was introduced. |
| RP-3 | High, confirmed historical | Provider timeouts and host availability block reliability; qualify provider and retain exact stage timings. Close with bounded final-source baseline and distinct recursive live runs. |
| RP-4 | Medium, baseline | Missing benchmark/live3 fixtures and obsolete recovery expectations; resolve separately with authentic portable fixtures, preserving historical failures. |
| RP-5 | Medium, unverified | Same-workspace sequential tasks and recursive child mission/authorization propagation need fuller controller coverage beyond existing baseline CLI tests. |

Engineering owner: local Mini Hivo maintainer/next repair checkpoint. None of these issues is silently marked closed.

## 12. Level 2 Readiness Decision

**INCOMPLETE.** Context gate and impact restrictions remain active; mutation grounding and independent verification existing regressions remain relevant. Bounded prerequisite-stall stopping has direct controlled evidence. Baseline has a genuine historical manual PASS. Final-source recursive completion, generalized progress/recovery, changed-state proof invalidation, multi-artifact recursive generality and provider reliability are not fully verified. Traceability is improved but the requested acceptance matrix is unfinished. No Level 3 or publication is authorized.

## Appendix A — Run Registry

[Workspace run registry](../evidence/level2-generalized-recovery/recursive-progress/run-registry.json) preserves exact retained requests/outcomes for projects 10–18. Host-only project-17 has no task run ID. Other historical audit cohorts and source versions remain linked in the earlier report below; no missing run ID is invented.

## Appendix B — Evidence Manifest

New originals: phase `original-hashes.json` and `originals.zip`, captured before edits for project-15/17/18. [Phase observations](../evidence/level2-generalized-recovery/recursive-progress/observations.json) record source hashes and independently checked current 47/63-byte outputs. Complete private traces/databases are retained. Selected local phase files and source pins are described in its README. Prior manifests remain immutable.

## Appendix C — Code and Test Change Manifest

This phase modifies production `mini.py`, adds `tests/test_context_completed_progress.py`, updates `scripts/verify_level2_offline.py`, `tests/test_adaptive_architecture.py` (message selection), `.gitignore`, the same candidate report and the new recursive-progress evidence packet. Earlier uncommitted parser, impact, routing, tests and evidence changes are preserved. No stage/commit/push/ref/PR changes occur.

## Appendix D — Reproduction and Historical Checkpoints

Run focused tests in a fresh checkout-local temporary directory; do not broad-discover live tests. Ordinary manual entry: `.\.venv\Scripts\python.exe -B -X utf8 mini.py --no-bootstrap`. Exact historical tasks are in the registry. For a fresh bounded replay, use `scripts/level2_clarification_replay.py --live --output-dir <fresh-output> --cases inventory`. Live calls are costly; do not repeat an unchanged resource/provider blocker. Preserve the resulting artifacts and independently inspect them, rather than trusting completion text.

The complete previous A–M report follows, retained as chronological checkpoint detail. Its “current” wording refers to its own recorded checkpoint and source pins, not this phase's final status.

---

# R_UPDATE_003 — Source-bound multi-artifact progress and deterministic recovery

## A. Update Identification

- **Date/timezone:** 23 October 2026; Africa/Cairo (earlier checkpoints retained below).
- **Status:** INCOMPLETE local candidate. The latest project-12 repair passes controlled CLI execution, persistent clarification and independent file verification. Genuine latest-source completion is unverified: host preflight blocks the critical continuation and Level 1; the three-file live attempt accepted structured input, then timed out in Specifier. Older successes and earlier-source controlled pins are not current live proof. See the latest project-12 addendum below.
- **Branch:** `codex/level2-generalized-recovery`.
- **Actual base:** `9957271c8e66d10bdfa5b408c74d26fcd7b78be2`, PR #6 head at branch creation. Local main remains `f842fb8`. PR #5/#6 were open/unmerged at the earlier preflight; this local-only repair does not recheck or modify GitHub state. No existing branch/PR was changed.
- **Source identity:** latest seven-production-file pins and test hashes in [project-12 offline results](../evidence/level2-generalized-recovery/project12-repair/offline/results.json); independent current-source checks in its controlled records. Earlier packets and live variants retain separate historical pins.
- **Containing commit/PR:** none; all new work is uncommitted and unstaged. Publication is not authorized for this update.
- **Scope:** source-bound literal artifacts, safe read-only command substitution, current-proof tracking, bounded stall handling, all-artifact Builder handoff and existing final gates. This does not implement unrestricted natural-language understanding or prove arbitrary application development.

## B. Original Problem

Original real run `20261022T005130-de9aff61`, model `gemma4:e4b`, attempted exactly two text files. The persisted request was:

```text
Create exactly two text files in the workspace.File 1:Name: student.txtContent:Name: SaraAge: 21Department: Computer ScienceFile 2:Name: course.txtContent:Course: Software EngineeringSemester: Fall 2026Status: ActiveVerify that both files exist and that each file contains exactly the specified three lines, in the correct order, without additional text.
```

Expected: both source-authorized files, independent exact-content checks, Falsifier, applicable post-state comparison and verified completion. Observed: 142 trace records; 28 SQLite tool events (17 refused commands, four writes, five reads, two context decisions); `budget_exhausted`, `root_verified=false`, 32 model calls, zero Falsifier calls, zero verification routes/comparisons and one execution-budget exhaustion. Saved execution time was 425.42 seconds.

The original workspace rolled back. Its final output bytes are unavailable; retained SQLite readbacks show three newline-separated fields. Whitespace-compacted failure summaries do not prove a one-line file, and readback text does not prove original LF versus CRLF bytes. No historical output was reconstructed or silently corrected. Originals and a private backup remain preserved with hashes.

The user explicitly confirmed the new byte oracle: UTF-8, LF between the three lines, no final newline. Student content is `Name: Sara\nAge: 21\nDepartment: Computer Science`; course content is `Course: Software Engineering\nSemester: Fall 2026\nStatus: Active`. Fresh real replays serialize those confirmed boundaries as JSON strings. They are clarified replays, not unchanged reruns of the ambiguous original text.

## C. Why the Update Was Necessary

Correct writes alone did not produce trustworthy completion. Level 1 recovery depended on a single recognized source-bound literal contract, while this request fell through to generic planning. The controller needed independent obligations, safe recovery and evidence-driven handoff for a bounded set of artifacts; increasing budgets or allowing shell commands would leave those mechanisms broken.

## D. Root Cause Analysis

**Latest investigation (project-12):** production `get_goal_contract` calls `LiteralClarifications.prepare` before the Specifier. The earlier `literal_requests` grammar accepted canonical clauses and `candidate_blocks` accepted concatenated `File N:Name:...Content:` previews, but neither recognized the supplied multiline `File N: filename / The exact content must be:` form. The old JSON decoder was invoked, but only at the beginning of the response; introductory prose prevented decoding, and the trailing whole-sentence whitelist separately rejected the actual equivalent policy prose. Independent decoding of the stored object succeeded. Pending state was correctly scoped and preserved; the new-task escape also depended on the narrow literal parser, so an independent inventory request was captured as an answer. These were parser/routing defects, not Ollama behavior. All four stored mini.py hashes matched the active previous fixes. Final provenance/count changes did not introduce the format restrictions. Prior tests used canonical single-line clauses, object-first JSON and approved suffixes, omitting the actual representations and turn sequence. Provider mocks did not cause this pre-provider failure. Full findings and preserved input hashes are in the [latest packet](../evidence/level2-generalized-recovery/project12-repair/README.md).

**New observed boundaries:** Failure B `20261022T223807-7d3afde8` and Failure C `20261022T224051-03e24342` both stopped at source ingestion with zero model/tool/Builder calls. The early literal-boundary guard ran before normal interpretation and only recognized the narrow clause grammar. It rejected a source-defined JSON filename/content map as well as the concatenated original request. No workspace-local pending question/answer state was persisted; `reset_run` and successive CLI turns therefore had no explicit linkage to the original task. Accepted clarification answers remained empty. This is a distinct ingestion/lifecycle defect, not an Ollama execution failure. Both original traces, ledger, host record and database are privately backed up and hash-preserved.

| Finding | Classification | Evidence / consequence |
|---|---|---|
| Concatenated exact source text became one source requirement; the generic impact candidate had 12 targets and no literal hashes. | Confirmed original execution/code path | [Original summary](../evidence/level2-generalized-recovery/original-summary.json). No independent source-byte oracle was compiled for either artifact. |
| Level 1 refusal recovery was conditional on accepted literal post-state hashes. | Confirmed production cause | Without hashes neither native hint nor three-refusal termination activated. The model repeated cat/ls/echo; allowlist rejection itself was correct. |
| Ordinary reads and successful writes were not formal proof coverage. Builder completion required further model cooperation. | Confirmed controller gap | No all-artifact current-proof transition existed before budget exhaustion; no Falsifier or final gates were reached. |
| Budget diagnosis lacked a stall signal/denial category and compacted evidence to a small window. | Confirmed diagnostic gap | Historical diagnosis remained unknown/low confidence; neutral budget exhaustion did not encode the repeated refusal mechanism. |
| Three-route truncation; inconsistent 700/800 versus 900-character anchor comparison; Windows LF-to-CRLF writes. | Additional defects reproduced by controlled cases | These blocked scale/byte invariants during investigation. They are not asserted as proven causes of the historical rollback. |
| Model lost task awareness. | Behavioral hypothesis only | Repeated proposals are observed; internal reasoning is unavailable and is not used as the fix. |

## E. What Changed

| File / functions | New correction |
|---|---|
| `hivo/literal_source.py`, `parse_literal_input` | Typed extraction of multiline file blocks and prose-wrapped/inline JSON maps, exact literal bodies/spans, policy and uncertainty reporting, case/duplicate/count/newline conflicts. JSON-looking block contents remain data. No inferred content or unconfirmed concatenated boundaries. |
| `hivo/literal_clarification.py`, routing/persistence | Separate syntax from task/answer routing, workspace-bound task IDs and append-only history, independent-task isolation, partial-answer retention, inherited original obligations and conflict diagnostics. A complete answer does not repeat the pending question. |
| `mini.py`, CLI input | Optional generic `--conversation-file` JSON array preserves complete multiline turns through normal controller/Specifier/gates. Original raw text, task identity, spans and policy provenance accompany canonical byte obligations. Interactive input remains supported. |
| `tests/test_project12_clarification.py`, fixture | Nine regressions using the four exact stored inputs, actual interactive/main orchestration and persistence, separate invocations/workspace binding, policy contradictions, inline maps and JSON-looking literal bodies. |
| [hivo/literal_clarification.py](../hivo/literal_clarification.py) | Workspace-local pending/resolved/cancelled clarification state; original request/hash/ledger and accepted answer provenance; validated exact JSON maps; partial/conflicting/invalid-answer handling; recovered File/Name/Content previews requiring ordinary confirmation. Original line-count constraints remain active. No inferred newline becomes authoritative without user confirmation. |
| `mini.py`, source ingestion | Resume a pending answer before the old guard; compile confirmed bytes into independent obligations, retain the original task/ledger and answer source separately, and record resolution metrics/events. Pending state survives run reset/process restart; old successful artifacts and raw evidence are untouched. |
| [hivo/artifact_progress.py](../hivo/artifact_progress.py) | Bounded independent literal parser with original spans; separate JSON string decoding; narrow instruction aliases; ambiguity detection; strict read-only command equivalence; attempt progress based on newly satisfied obligations. |
| [hivo/requirements.py](../hivo/requirements.py), deterministic candidates | Retain separate multi-artifact source records instead of merging them into one sentence. Exact content is compiled from original input, not whitespace-normalized prose. |
| [mini.py](../mini.py), goal/impact compilation | One targeted clarification for unsupported ambiguous exact multi-artifact boundaries; preserve original request; per-artifact paths/digests and requirement targets; raw-source fingerprint/spans; all-or-nothing rejection of invalid, metadata, existing or Windows-aliased target sets. |
| `mini.py`, write/tool boundary | Shared guarded writer preserves exact UTF-8 bytes for accepted literals on write_file, edit_file and edit_file_range. Same-byte writes are skipped only for files created in the current transaction, after normal guards; externally created/user-owned files cannot be adopted. Existing generic command allowlist is unchanged. |
| `mini.py`, Builder loop | Preserve refusal as failure, dispatch only a recognized native read equivalent through ordinary guards/offered tools, retain separate native evidence; cache failed/successful proofs under accepted contract/path/current digest; invalidate by content changes; deliver proof/remaining-coverage messages to Builder; normalize equivalent read identities, bound cumulative denials and cycles; automatic all-artifact handoff. |
| [hivo/pre_mutation_impact.py](../hivo/pre_mutation_impact.py) | Full canonical anchor fingerprints plus consistent bounded display comparisons. Visible goal drift cannot hide behind a stored hash; tail drift is detected. Legacy contracts retain bounded compatibility checks. |
| [hivo/verification_routing.py](../hivo/verification_routing.py) | Preserve every literal route within the existing impact bound; a newer identity-matched literal readback supersedes prior state while retaining historical failures. Final independent filesystem comparison remains mandatory. |
| `mini.py`, diagnosis | Explicit stalled execution becomes a high-confidence orchestration diagnosis. A historical budget outcome requires repeated refusal evidence, not one incidental denial, for that classification. |
| [tests/test_level2_generalized_recovery.py](../tests/test_level2_generalized_recovery.py) | Generalized system/negative/adversarial matrix, not filename-specific fixtures in production. |
| [tests/test_literal_clarification_lifecycle.py](../tests/test_literal_clarification_lifecycle.py) | Nine cases covering real main/You turns with JSON and ordinary confirmation; reset/resume and standard Source Contract provenance; partial, conflicting, invalid, wrong-line-count and unnamed-block file-count answers; informal/Arabic aliases and strict bytes. Host/provider setup alone is scripted in controlled CLI cases. |
| [scripts/level2_clarification_replay.py](../scripts/level2_clarification_replay.py) | Four persistent fresh CLI scenarios, controlled and genuine Ollama modes, exact artifacts, per-turn outcomes and source identities. |
| [tests/test_level1_native_verification.py](../tests/test_level1_native_verification.py), [Level 1 replay](../scripts/level1_native_verification_replay.py) | Update expected scripted ordering for deterministic Builder handoff; preserve wrong-byte and ignored-guidance negative oracles. Historical Level 1 reports/evidence remain unchanged. |
| [Level 2 replay](../scripts/level2_recovery_replay.py), [offline runner](../scripts/verify_level2_offline.py) | Persistent independently checked artifacts and explicit controlled/live modes; focused provider-blocked regressions with known live-calling case excluded explicitly. |
| Git configuration and new evidence/report | Scoped original-workspace exclusion and canonical LF for new sanitized derivatives. No staging, commit, push or prior PR edit. |

## F. How the Fix Works

1. Preserve the original source. Recognize only sufficiently delimited literal obligations, retaining spans/fingerprints and separate records; decode exact payloads without spelling/whitespace normalization. Ambiguous byte boundaries return clarification before mutation.
2. Compile all authorized artifact paths and independent expected digests. Invalid/aliased sets never receive partial authority. Current context and impact acceptance still precede mutation.
3. Keep shell restrictions intact. A refused single-path cat/type request may become guarded native readback (`run_file` only for accepted literal semantics, otherwise `read_file`); bare ls/dir may become guarded `list_files`. Composition, options, interpolation, redirection, echo and ambiguous Windows shell paths have no automatic equivalent.
4. Track actual bytes and current proofs. Same-content authorized writes are no-ops. Proof identities include contract, path and digest; changed content cannot reuse a proof for its previous bytes. Both failed and successful observations are retained.
5. Newly satisfied obligations earn progress. Repeated reads, unchanged writes, alternating wrong writes and alternating unsupported commands cannot indefinitely renew work. Three unrecovered denials or six non-progress observations produce explicit `EXECUTION_STALLED`; existing more specific recovery guards remain active. Nonliteral duplicate actions are also bounded without treating novel inspections as mutation progress.
6. When every required literal matches, end Builder work immediately and enter existing Falsifier/applicability/aggregation/post-state/transaction gates. Builder handoff is not Root success. Missing, wrong, unauthorized or stale outputs cannot bypass final verification.

No tool/model/time budget constant was increased. Automatic native proof work is bounded by the existing artifact/attempt limits and is counted in tool metrics. The replay wall cutoff is a separate interruption safeguard, not an execution-budget extension.

## G. Functional Verification

**Earlier controlled checkpoint, preserved:** model decisions were scripted; authorization, context, impact, tools, filesystem, Falsifier, final route aggregation and transaction gates were real. [Earlier scale results](../evidence/level2-generalized-recovery/controlled-matrix.json) cover 1, 2, 3, 4, 5, 8 and 10 artifacts. All had correct outputs/root completion, but the stronger ten-file inspection failed because only eight independent Falsifier reads existed. This failed checkpoint is retained unchanged. The new local correction fills missing literal Falsifier reads through guarded native tools after model probes; current independent inspections pass all seven sizes through ten without raising the eight-step model limit. See the local repair addendum for current evidence.

**Controlled adversarial integration:** the [targeted results](../evidence/level2-generalized-recovery/targeted-results.json) and [test source](../tests/test_level2_generalized_recovery.py) cover consecutive/alternating denials, safe/unsafe substitutions, partial work and unchanged-write avoidance, stale-proof invalidation after external byte change, alternating incorrect writes, deliberately incorrect output/rollback, out-of-scope paths, case aliases, overflow clarification, long/visible anchor drift and independent requirement mappings. A mixed Arabic/English case uses minor instruction typos, adjacent clauses and significant literal whitespace through actual final gates. These are not live-model language-reliability measurements.

**Level 1 compatibility:** the existing ten-test suite and fresh persistent [Level 1 controlled replay](../evidence/level2-generalized-recovery/level1-result.json) pass with exact 15-byte `Hello Mini Hivo`. The historical real Level 1 success is preserved, not counted as a fresh live run.

**Earlier-source live-model end-to-end — PASS:** auto-mode run `20261022T020137-6b8c1201`, actual local `gemma4:e4b`, passed three host canaries, context/impact authorization, two writes, two controller native proofs, real Falsifier `read_file` on each artifact, both required routes, impact post-state comparison and transaction commit. Metrics: `done`, `root_verified=true`, nine model calls, seven tool calls, one Falsifier call, one impact authorization/comparison, zero execution-budget exhaustions, 399.18 saved run seconds (428.15 wall seconds including startup). Independently inspected 59 trace records, seven database events and actual output bytes: student.txt 47 bytes, course.txt 63 bytes, each exactly two LF separators and no final newline. All 13 checks passed against that checkpoint's pins. [Earlier inspection](../evidence/level2-generalized-recovery/live/live-final-source-inspection.json) and [actual artifact copies](../evidence/level2-generalized-recovery/artifacts/student.txt) support that historical result. The later clarification/Falsifier repair changes production hashes; this earlier result is not presented as a fresh pass of that repair.

## H. Additional Successful Tests

Final reviewed-source checks pass Level 1 (10), generalized recovery (20), prior clarification lifecycle (9), new project-12 clarification (9), existing lifecycle (17), impact (27), context sufficiency (9), verification applicability (15), authority (23), experiment-focused (122), adaptive architecture (90), project understanding (32), model policy (4), and requirement clarification (49 with one known live-calling case explicitly excluded). Counts are per suite, not summed unique coverage. Direct functional oracles are distinct from regression passes. The generalized suite asserts every Falsifier read, and current independent scale inspections confirm coverage. Latest source/test pins are in the project-12 offline record; earlier packets retain their own pins.

## I. Regression and Compatibility

The verification-policy suite executes eight tests with six OK outcomes and two missing historical prompt-fixture errors. The broader recovery group executes 186 tests with 24 failure records, two errors and three skips. The same failure/error identities reproduce against unchanged base `9957271`, loaded from Git objects without switching or modifying the original checkout. [Baseline comparison](../evidence/level2-generalized-recovery/baseline-comparison.json) retains this boundary. These suites remain failed.

A separate approved-verification suite cannot initialize because its historical `revised_plan_source.json` fixture is absent (zero executed tests, one setup error). No fake fixture was supplied. Full discovery is not run; it has known live-provider and historical-fixture dependencies. Early development failures, the alternating-write counterexample and a sandbox temporary-directory permission failure are retained privately; they are not reported as final passes.

## J. Overall Impact

For the declared bounded literal-artifact scope, progress and transition now follow source-grounded current evidence rather than the model remembering prior actions. Native recovery remains read-only and guarded. Scale does not drop required artifacts after the third route. Incorrect bytes and failed final gates remain failures with rollback. Existing lifecycle, authorization and command-security checks remain active.

## K. Limitations and Remaining Issues

- Maximum ten independently compiled literal artifacts per request; overflow requires clarification. This uses the existing obligation bound rather than raising budgets. It is not an unbounded N-artifact guarantee.
- **Earlier scale boundary corrected locally:** after model probes, the controller fills missing current literal Falsifier readbacks through the existing guarded `run_file` boundary, retaining failures and per-artifact receipts. Independent controlled coverage now passes through ten. Model budgets are unchanged; this does not establish larger live workloads.
- Instruction aliases, explicit multiline blocks and filename/content JSON maps form a bounded grammar. Arbitrary informal prose, arbitrary typos, full Arabic fluency and automatic reconstruction of missing line boundaries are not established. The original concatenated ambiguous request intentionally asks for clarification; complete structured input does not.
- Cached progress is attempt-local. Existing user-owned/verified files are not automatically authorized for replacement; a new run does not inherit reusable runtime authorization. Transaction rollback is preserved, not converted into partial success.
- Safe substitutions cover only unambiguous read semantics. No automatic echo/shell-write interpretation, command execution fallback or arbitrary shell enablement.
- Live success establishes the clarified Level 2 scenario in the recorded run(s), not repeatability, larger live workloads, complex applications or universal correctness. Real Falsifier behavior is distinguished from scripted native Falsifier probes.
- Model inference remains slow; saved execution and total wall timings have different scopes. Baseline routing deliberately retains its pre-existing reduced Task Brain context scope.
- Existing fixture/recovery failures above remain unresolved outside this update's scope. Previously public raw Git history is unaffected by new sanitization.

## L. Evidence and Reproduction

See [evidence overview](../evidence/level2-generalized-recovery/README.md) and [provenance manifest](../evidence/level2-generalized-recovery/manifest.json). Original source hashes identify untouched raw observations; derivative hashes identify canonical-LF sanitized copies. No staged-blob validation is claimed because staging is prohibited.

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/verify_level2_offline.py --output-dir output/level2-new-offline
.\.venv\Scripts\python.exe -B -X utf8 scripts/level2_recovery_replay.py --output-dir output/level2-new-controlled
.\.venv\Scripts\python.exe -B -X utf8 scripts/level2_recovery_replay.py --artifacts 8 --output-dir output/level2-new-eight
.\.venv\Scripts\python.exe -B -X utf8 scripts/level1_native_verification_replay.py --output-dir output/level1-new-check
# Only with explicit live-experiment authorization:
.\.venv\Scripts\python.exe -B -X utf8 scripts/level2_recovery_replay.py --live --output-dir output/level2-new-live
```

Every output directory must be fresh/nonexisting. The offline runner exits nonzero while the disclosed historical suites fail; inspect its per-suite results rather than claiming a universal green result. Production/test source pins and individual test identities accompany the records.

Read-only independent inspection, without model calls:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/inspect_level2_replay.py --run-dir output/level2-new-controlled --output-file output/level2-new-inspection.json
```

All four original Level 2 source files and the private ZIP backup were rehashed successfully. Prior Level 1 successful trace, 15-byte output and original first metrics row remain intact. The project-9 database/whole ledger already contained a later failed run before this investigation; they do not match the older publication snapshot and were neither restored nor represented as unchanged copies. Raw workspaces/databases remain private. The curated manifest validates 52 derivative/source pairs against working-tree bytes; staged-blob checks are not applicable because the index remains empty.

### Explicit investigation answers

| Question | Answer |
|---|---|
| 1. Original failure? | Missing independent byte obligations left the controller in generic execution until budget exhaustion. |
| 2. Repeated prohibited commands? | Correct refusals did not trigger deterministic native recovery on that generic path. |
| 3. Why Level 1 did not generalize? | Its recovery depended on a recognized single literal hash contract. |
| 4. Repeated reads/writes? | Successful operations were not current formal obligation coverage; model awareness controlled further work. |
| 5. No verification handoff? | No deterministic all-artifact completion transition was present. |
| 6. No early loop detection? | No cumulative denial/obligation-progress signal covered alternating actions. |
| 7. Ineffective budget recovery? | It was a downstream budget outcome, without an evidence-directed native recovery or reserved transition. |
| 8. Unknown diagnosis? | Small compacted evidence and missing stall/denial classification obscured the repeated refusal cause. |
| 9. New protections? | Source hashes/spans, all-or-nothing authority, exact guarded writes, safe native substitution, digest-bound proofs, bounded progress, full routes and deterministic handoff. |
| 10. Scale evidence? | Current controlled 1/2/3/4/5/8/10 pass full independent inspection. The earlier ten-file partial result remains preserved. |
| 11. Remaining uncertainty? | Broader semantic language extraction, baseline failed suites, current-source live completion and live repeatability/complex workloads. |
| 12. Genuine Level 2 PASS? | Structured two-file execution genuinely passed at the pre-review checkpoint (20261022T225748-a38c9d71); the earlier run 20261022T020137-6b8c1201 is also preserved. The complete final-source clarification workflow is NOT a verified live PASS: one replay was interrupted, the JSON replay timed out after accepting its answer. |

## Historical local-only repair checkpoint — Failures B/C

The [current evidence package](../evidence/level2-generalized-recovery/clarification-repair/README.md) retains separate final-source and pre-review pins. New-source controlled results pass all 13 independent checks at 1/2/3/4/5/8/10 artifacts and four actual CLI conversations. Only provider/host setup is scripted in controlled CLI cases. The nine lifecycle tests additionally enforce standard Source Contract answer projection, original file count without numbered blocks, original line count, partial/conflicting-answer retention and raw provenance.

Pending state lives privately at workspace-relative `.hivo/literal-clarification.json`. It stores original text/hash/ledger, candidate source spans, accepted exact contents and answer provenance. A confirmation accepts the displayed preview; a validated JSON map supplies literal bytes directly. No filename/value is hardcoded in production. This is bounded source interpretation and durable task/answer association, not general conversational memory or unrestricted semantic parsing. Existing verified evidence and authorization are not inherited as reusable runtime authority across runs.

The first genuine four-case cohort used the main clarification/Falsifier repair before the last answer-projection/file-count corrections:

| Case | Actual run / boundary | Observed outcome |
|---|---|---|
| Original request then ordinary confirmation | No task run ID: host preflight stopped first | FAIL before execution: `CRITICAL_MEMORY_HEADROOM`. No gate was waived. |
| Original request then requested JSON answer | `20261022T225422-3d682d67` | Answer accepted and recorded; later local Ollama timeout in Specifier/Stage 2. `failed`, `root_verified=false`, two model calls, zero tools, 169.03 seconds. |
| Structured two-file request | `20261022T225748-a38c9d71` | PASS: independent exact 47/63-byte outputs, Builder native proofs, both Falsifier reads, routes, impact comparison and transaction commit. Nine model calls, seven tools, one Falsifier, zero budget exhaustions, 518.12 run seconds / 555.86 wall seconds. |
| Level 1 regression | `20261022T230703-c63e9980` | PASS: exact 15-byte `Hello Mini Hivo`, native proof, independent Falsifier, impact comparison and commit. Nine model calls, six tools, one Falsifier, zero budget exhaustions, 476.59 run seconds. |

Their source hashes are retained as pre-review, not relabeled final. Final review found two counterexamples (standard answer fields not projected; partial answer discarding unnumbered file count), corrected them and reran the focused suites and controlled matrix with matching final pins. No change was made to the ordinary structured/Level 1 execution branches for these final corrections.

Each environment-blocked clarification case receives at most one bounded retry in a fresh workspace under final source pins. The outer wall limit is 720 seconds including preflight; application model/tool/time budgets are unchanged. Final-source ordinary-confirmation execution `20261022T231710-80240587` accepted `yes`, selected recursive mode, split the task, reached child-1 Builder and was interrupted at the outer limit before any verified completion. Its driver metrics refer to the preceding completed clarification turn `20261022T231710-a834c0f2`; those zero-call metrics are **not** the interrupted execution's final metrics. The current [live outcomes](../evidence/level2-generalized-recovery/clarification-repair/live-outcomes-summary.json) identify the latest trace and its boundary independently. Interruption is not reclassified as an application budget-exhaustion outcome or a repeated clarification failure.

Final-source JSON-resumption execution `20261022T232911-4d8ce697` accepted and persisted one answer, including standard Source Contract answer fields. It then timed out in the local Ollama Specifier before Builder/tool execution: `failed`, `root_verified=false`, two model calls, zero tools/Falsifier/impact authorizations, 181.22 seconds. No identical boundary question was repeated. A finished process with exit 0 does not change that failed task result. No further live retries were started.

**Current verdict:** controlled functional repair PASS for the declared bounded scope; structured real Level 2 PASS at its explicitly pinned pre-review checkpoint; complete final-source clarification-to-verified-completion **UNVERIFIED / not yet PASS**. Provider latency/resource availability and practical completion through recursive auto routing remain blockers. The trace establishes the stopping boundaries, not a proven internal cause for model latency or a proof that recursive routing itself is incorrect. The next investigation is to qualify local provider responsiveness and inspect the recursive fit/mission/Worker path under stable conditions without weakening gates or increasing budgets. Broader natural-language understanding, cross-run artifact reuse and complex application behavior remain outside proven scope.

The new curated manifest validates 57 source/derivative pairs; the previous 52-pair package remains valid separately. All nine original failed-run source files (four project-10 and five project-11 files) remain hash-unchanged. Raw logs/databases/workspaces/host inventories/backups are private. Current tests and provenance pin 47 source/test files; publication remains unauthorized.

Failures, interrupted traces, backups and earlier successful results remain preserved. This mixed source/attempt record is not a reliability rate. Root completion for recursive execution and broad language interpretation is not established by the controlled baseline matrix. No higher testing level is started and no publication action is authorized.

## Latest local repair checkpoint — project-12 (23 October 2026)

This section supersedes earlier descriptions of the current checkout. Historical reports, cohorts and successful pins above remain unchanged evidence of their own checkpoints. The complete [project-12 evidence README](../evidence/level2-generalized-recovery/project12-repair/README.md) provides reproduction and the separate [source/derivative manifest](../evidence/level2-generalized-recovery/project12-repair/manifest.json).

### Observe and investigate

| Original real-user run | Established boundary and explanation |
|---|---|
| `20261022T234739-c8d73cc5` | Complete structured two-file source was incorrectly rejected: block headings were outside the parser grammar. Literal obligations were absent from the compiled ledger despite retained raw input. |
| `20261022T234812-4819d2e2` | Independent three-file inventory was incorrectly intercepted by the old pending two-file task because new-task detection reused the same narrow parser. This was within one workspace, not cross-workspace leakage. |
| `20261022T235215-179d65fd` | The JSON helper ran, but decoding began at introductory prose, not the opening object; the actual suffix was also outside the sentence whitelist. Thus no answer was recorded. The JSON itself and its intended values were valid. |
| `20261022T235253-8db69c4f` | One-file content could not complete a two-file obligation. Retaining the missing file was correct; failing to record the supplied portion and repeating the generic question was incorrect. |

All four stopped at SOURCE_REQUIREMENT_INGESTION with zero model/Builder calls. The active mini.py SHA-256 was `0cd452d7463a4a4c06f5f7b816ae3edd29c1ba7332896ff93b9145013ab530e1`, matching stored runs; all six previous production pins matched the pre-edit checkout. There is no evidence of stale entrypoints, competing branches or provider involvement in these four failures. Original pending state retained the correct request, two filenames, three-line scope and empty answers. Earlier JSON successes used accepted object-first syntax; the final provenance/count corrections did not create the prefix/tail restriction.

Actual lifecycle: `main/read_user_prompt` → request runner/reset → `get_goal_contract` → `LiteralClarifications.prepare` → typed literal extraction and persisted task/answer association → canonical exact obligations plus original provenance → normal source contract/Specifier → context/impact gates → Builder/native verification → Falsifier → routing/impact comparison/transaction commit. The original CLI captured multiline text correctly, as demonstrated by stored raw inputs. New tests exercise this controller and persistent state rather than testing only extraction helpers.

### Repair and why it generalizes

The shared typed parser extracts values before task routing. It recognizes numbered/unnumbered content blocks and filename/content JSON with ordinary surrounding prose, retains source spans, and handles policy categories rather than a finite sentence whitelist. Literal bodies are excluded from command/policy interpretation. A JSON-looking line within a literal block cannot become a competing filename map. Windows filename collisions, duplicate keys, invalid counts, unsupported encoding/separators and contradictory newline policies remain blocked. Source-grounded partial values are recorded without reducing original scope. Concatenated natural-language boundaries remain a displayed proposal requiring an actual confirmation, not invented bytes.

Workspace-bound v2 state retains original text/hash/ledger, task ID, accepted values and actual answer provenance; append-only history retains independent task identities. Disjoint explicit creation requests are separately routed without importing pending names/counts/policies. The previous pending task remains resumable. Legacy v1 pending states migrate on write. Copied v2 state bound to another workspace is rejected. This is workspace-local task continuity, not identity across arbitrary users sharing the same workspace. `--conversation-file` provides a generic source-faithful replay interface using the normal controller; it does not bypass Specifier, impact authorization or verification.

This turn modified `mini.py`, `hivo/artifact_progress.py`, `hivo/literal_clarification.py`, new `hivo/literal_source.py`, the four replay/offline scripts (`level1_native_verification_replay.py`, `level2_recovery_replay.py`, `level2_clarification_replay.py`, `verify_level2_offline.py`), `.gitignore`, new `tests/test_project12_clarification.py`, its `tests/fixtures/clarification_user_turns.json`, this candidate report and the evidence README/REVIEW/new packet. Prior local changes in impact/requirements/routing, Level 1 tests and `.gitattributes` were preserved. No budgets, command allowlist or security gates were loosened. New investigation scripts/raw outputs/backups are private under the ignored audit directory.

### Final reviewed-source controlled functionality

| Case | Controlled run | Independent outcome |
|---|---|---|
| Concatenated original then the actual prose-wrapped JSON answer | `20261023T001237-d07c5c33` | Clarification then `done`, one accepted answer; exact 47/63-byte outputs; root verified. |
| Actual complete structured two-file request | `20261023T001238-05a458cd` | Direct `done`, no unnecessary clarification; exact 47/63 bytes; root verified. |
| Actual independent inventory request | `20261023T001239-fe645539` | Direct `done`; three independent exact outputs; root verified. |
| Level 1 | `20261023T001240-d6087ebb` | `done`; exact 15-byte `Hello Mini Hivo`; root verified. |

All four pass thirteen independent checks against real files, retained trace and read-only SQLite data: context before mutation, authorized impact, every Builder native proof and Falsifier read, full required route coverage, impact post-state comparison, transaction commit, verified status, no exhausted budget and source identity. Host and model responses are scripted; actual production execution/gates and filesystem operations are real. Inspector provider/preflight checks are not live assertions for controlled runs. Seven production hashes match the final reviewed checkout. The independently inspected controlled source-bound scale matrix also passes at 1/2/3/4/5/8/10 artifacts; the new parser separately tests those block counts. These are bounded controlled proofs, not a live reliability rate.

Nine new regressions pass, including actual interactive main accepting the complete stored JSON answer to a persisted historical question; separate CLI invocations; independent task followed by partial answer and full continuation; copied-state workspace isolation; four original inputs in order; policy conflicts and literal JSON bodies. In the corrected four-turn sequence, turn one now completes, unlike history. Replaying its answer after completion is accepted but fails the existing-file impact guard instead of silently overwriting those files. This limitation is explicitly asserted and disclosed. A genuine pending full answer completes in a fresh controlled workspace.

### Additional regression results and baseline failures

Final reviewed-source suite results: Level 1 10, generalized recovery 20, previous clarification 9, new clarification 9, greenfield lifecycle 17, impact 27, context 9, applicability 15, authority 23, experiments 122, architecture 90, project understanding 32, model policy 4, requirement clarification 49 all pass separately. The offline runner exits 1 because verification-policy (8 executed, 2 missing-benchmark-fixture errors) and V26 recovery (186 executed, 24 failure records, 2 errors, 3 skips) remain unsuccessful. One historically live-provider requirement test is excluded explicitly. Counts are not summed or inferred from subtest failures.

Failure/error identities match preserved results at unchanged base `9957271`. Inspected causes include absent benchmark/live3 fixtures, old envelopes lacking required `execution_id`/failure-evidence fields, downstream closure assertions/dereferences after those envelopes fail, and obsolete absolute historical-directory expectations in two recovery tests. Recovery production code is unchanged by this clarification repair; these failures do not exercise its new parser/state paths. They remain baseline fixture/compatibility debt, not passing tests or evidence of new repair success. No historical fixture was manufactured, deleted or rewritten.

### Genuine Ollama outcomes and limitations

| Attempt | Actual boundary | Verdict |
|---|---|---|
| First JSON continuation | Host preflight `CRITICAL_MEMORY_HEADROOM`, 1/3 canaries; no task run ID | Not executed; not a clarification result. |
| Inventory `20261023T000915-20404da5` | Preflight passed; structured ingestion accepted with zero answers/questions; Specifier request timed out after 120 seconds. Two model calls, zero tools/Falsifier/authorizations, 167.35 run seconds / 180.12 wall seconds; no output files. | `failed`, root false. Pins precede the last policy/JSON-body negative-case corrections; not final reviewed-source completion. |
| Level 1 | Host preflight `CRITICAL_MEMORY_HEADROOM`, 0/3 canaries; no task run ID | Not executed. Historical Level 1 PASS remains historical. |
| Single final reviewed-source JSON-continuation attempt | Host preflight `CRITICAL_MEMORY_HEADROOM`, 0/3 canaries; no task run ID | Final-source live completion unavailable; no further retries. |

Stored timing/resource records distinguish resource preflight failure and provider timeout from the demonstrated ingestion defects. The Specifier's internal latency cause is not established by a timeout alone. No model request or verifier PASS can substitute for actual output/state. Earlier genuine successes `20261022T225748-a38c9d71` and `20261022T230703-c63e9980`, earlier partial/rejected/interrupted attempts and all seven earlier failure identities listed above remain retained, not relabeled current success.

**Verdict: R_UPDATE_003 remains INCOMPLETE.** Complete JSON works through the actual controlled CLI, structured input avoids unnecessary clarification, and independent tasks do not inherit stale pending requirements in tested cases. The final-source genuine clarification-to-ROOT-VERIFIED workflow, independent three-file completion and refreshed live Level 1 remain unverified. Stable provider/resource qualification followed by those bounded live scenarios is the next safe checkpoint. No Level 3 work is started. Broader language interpretation, more than ten artifacts, cross-run adoption/overwrite of existing files and complex applications remain outside proven scope.

Eight project-12 originals and their ZIP were independently rehashed successfully. Existing raw workspaces/evidence and prior packets remain preserved. The new manifest distinguishes original source and sanitized derivative SHA-256; canonical copies are UTF-8/LF. Raw logs/databases, private host inventories and backups remain local/ignored. All changes remain unstaged/uncommitted on the same local branch; no PR/ref, upstream main or published history is altered. Reproduction commands and exact evidence filenames are in the latest README.

## M. Team / Proposed PR Summary

**Proposed title (local draft only):** `Repair structured literal ingestion and persistent clarification routing`

**Why:** Manual Level 2 exposed format-coupled ingestion: complete content blocks were rejected, prose-wrapped JSON was not decoded, and independent tasks were intercepted by pending questions. Earlier execution also lacked generalized native progress/handoff. **Changes:** shared source parser, workspace-bound task/answer history, retained original byte/count/newline provenance, generic multiline CLI replay, independent artifact obligations, guarded native recovery and verification handoff. **Verified functionality:** four final-source controlled CLI workflows produce exact bytes and complete all context/impact/native/Falsifier/final transaction gates; controlled scale passes through ten artifacts. Nine new manual-path regressions plus prior nine clarification, twenty generalized and ten Level 1 cases pass; other successful suites are listed separately. **Remaining issues:** final-source genuine completion is unverified due host resource failures; the live inventory attempt accepted ingestion but timed out in Specifier. Baseline recovery/fixture failures remain, and resubmitting completed files requires existing-file authority. No earlier live PASS is relabeled current. The local candidate is incomplete and not authorized for publication; PR #5/#6 remain unchanged.

This is a candidate report for a future review. No staging, commit, push, PR creation, merge or modification to PR #5/#6 is performed for R_UPDATE_003.

## Research-Informed Recursive Execution and Recovery Investigation

23 October 2026, Africa/Cairo. **INCOMPLETE; local candidate.** This phase follows the earlier twelve-section investigation and preserves it unchanged as a historical checkpoint. Current evidence is in [research-recovery](../evidence/level2-generalized-recovery/research-recovery/README.md); prior packets retain their own source pins. No new numbered update is allocated.

### A. Problem Definition

Our traces establish baseline PASS `20261023T004235-79109aeb`, recursive FAIL `20261023T005124-a828f3dd` with 28 completed-context calls and no mutation, and Specifier timeout `20261023T012433-0023e35a`. The previous correction established a safe bounded stop, not useful general recovery. The default context branch preceded generic progress observation, rebuilt messages and kept offering the completed prerequisite. The optional constrained policy did not protect that path. Internal model reasoning remains unknown. New controlled experiments additionally expose child literal-scope inheritance and a parent integration authorization boundary; those are not automatically attributed as causes of the historical repeated-call trace.

### B. Literature Search Method

Focused web searches on arXiv, original NeurIPS proceedings, PMLR/ICML and IEEE/official publisher pages used combinations of tool loops, agent feedback, execution monitoring, programmatic task plans, assertions and LLM-Modulo planning. Selection required a concrete feedback/precondition/verifier mechanism relevant to the source defects. Three original works were reviewed through available abstracts, paper text and venue metadata; this is a focused review, not a systematic survey or a reproduction of their experiments. No access to Google Scholar, ACM or IEEE subscription full text is claimed. Public arXiv/full-paper and official proceedings sources were sufficient. Research performance is not evidence that Mini Hivo passes.

### C. Reviewed Research Papers

1. **Reflexion: language agents with verbal reinforcement learning.** Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao. NeurIPS 2023, volume 36. [Official conference record](https://papers.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html), [paper](https://papers.nips.cc/paper_files/paper/2023/file/1b44b878bb782e6954cd888628510e90-Paper-Conference.pdf). DOI 10.52202/075280-0377; related arXiv:2303.11366 lists an additional author, Edward Berman, so the conference citation is used here. Mechanism: retain feedback/reflection in episodic memory without updating model weights. Authors report 91% HumanEval pass@1 and evaluate decision-making/reasoning/coding. Limitations for us: reflection is model-generated, depends on feedback quality and adds inference/context; it cannot authorize actions or prove file bytes. Transfer: preserve reliable feedback across turns. Full reflective retries are rejected for now because local latency is already problematic; no extra reflection model is introduced.

2. **ProgPrompt: Generating Situated Robot Task Plans using Large Language Models.** Ishika Singh, Valts Blukis, Arsalan Mousavian, Ankit Goyal, Danfei Xu, Jonathan Tremblay, Dieter Fox, Jesse Thomason, Animesh Garg. ICRA 2023; 2022 preprint [arXiv:2209.11302](https://arxiv.org/abs/2209.11302), [full text](https://arxiv.org/html/2209.11302v1); DOI 10.1109/ICRA48891.2023.10161317. Mechanism: action/object APIs, program-like plans and assertions with execution feedback. Authors evaluate VirtualHome and demonstrate a physical robot; ablations examine prompt components. Physical execution has perception/grasp limitations, unlike deterministic text-file checks. Adaptation: expose legal capabilities and evaluate real state, without running generated Python plans or importing robotics infrastructure. Its results do not guarantee loop prevention or Mini Hivo completion.

3. **Position: LLMs Can’t Plan, But Can Help Planning in LLM-Modulo Frameworks.** Subbarao Kambhampati, Karthik Valmeekam, Lin Guan, Mudit Verma, Kaya Stechly, Siddhant Bhambri, Lucas Paul Saldyt, Anil B Murthy. ICML 2024, PMLR 235:22895–22907. [Official paper/metadata](https://proceedings.mlr.press/v235/kambhampati24a.html), [preprint arXiv:2402.01817](https://arxiv.org/html/2402.01817v1). Mechanism: candidate generation constrained by external critics in a bidirectional generate/test/critique architecture. This is a position/framework paper drawing on planning evaluations, not a benchmark of our runtime controller; no measured Mini Hivo speedup is inferred. Limits: critic/domain models must themselves be valid; external checking cannot ensure a useful proposal arrives. Transfer: deterministic eligibility, source-bound postconditions and bounded corrective feedback, with all authorization and final verifiers retained.

### D. Comparative Research Analysis

| Technique | Mini Hivo failure / role | Requirements and minimal adaptation | Safety, cost and deterministic measurement |
|---|---|---|---|
| Episodic verbal reflection | Lost feedback / recovery | No training, but extra model calls/memory if fully adopted. Only retained factual feedback is directly transferred. | Reflection must never be approval. Extra inference rejected; compare retained proof and next legal action under the same budget. |
| API/precondition assertions | Repeated satisfied prerequisite / prevention and detection | Adapt existing offered schemas, gate snapshot and dependency fingerprints; no new infrastructure. Generated executable plans are unsuitable here. | No arbitrary plan execution. CPU fingerprints plus bounded context; test changed files, scope and negative gates. |
| External critics and corrective loop | Illegal/redundant action proposals / recovery and verification | Controller identifies the ineligible action and supplies actual proof plus legal capabilities. Model chooses the next action; verifier remains external. | One bounded recovery opportunity within the existing model/tool budget; no forced mutation. Measure duplicate dispatches, actual guarded writes, exact bytes, Falsifier and parent result. |

These are engineering adaptations, not implementations or reproductions of the full papers. Full frameworks, model training/replacement, learned affordance networks and unbounded reflection are unsuitable for this local resource budget. Generic planner verification and hierarchical success remain hypotheses until exercised in our own controller tests. No direct performance comparison with those research systems is claimed.

### E. Selected Engineering Approach

Use an evidence-bound controller checkpoint and bounded generate/check/feedback cycle. A redundant completed-context proposal is suppressed before dispatch; the provider receives current actual gate evidence and already-projected legal tools. It must make a fresh choice. Persistent repetition stops rather than forcing an operation. A receipt binds mission, execution scope, impact identity, working evidence, contradictions and named inspected-file fingerprints. Material changes revoke permission before dispatch and require a refreshed node. The controller accounts for its own successful guarded mutations without accepting an out-of-band change as progress.

The useful comparison is to the preceding implementation: it returned an unavailable-tool result for the redundant proposal and could only terminate. The new controlled recovery path returns actionable controller feedback and demonstrates successful legal work when the next provider proposal is valid. This is not a guarantee that the real model will follow that feedback.

### F. Code-Level Implementation

- `mini.py::execute_agent_task`: duplicate completed-context calls do not run or count as new context evidence; controller recovery records a distinct event and preserves actual proof. No fake tool response or new authorization is emitted. A fresh turn selects its own operation; repeated ineligible selection remains bounded.
- Same function: attempt-local dependency receipt checked before tool dispatch. Mission/scope/impact/evidence/file drift revokes context permission and stops with `CONTEXT_PROOF_STALE`; final summarization preserves that diagnosis. In-place re-specification is not implemented; a refreshed attempt must revalidate normally. This is narrower than automatic successful recovery after arbitrary material changes.
- `hivo/context_sufficiency.py::ContextSufficiencyGate.invalidate`: explicitly revokes mutation permission; only a later valid gate decision can restore it.
- `mini.py::_prepare_task_impact_contract`: child literal postconditions are restricted to the child execution contract or its proposed scope intersected with authoritative source artifacts. A child must not inherit the entire parent artifact set. Source requirement records remain scoped; parent obligations remain at ROOT. Existing-file restrictions, normal impact acceptance and verification remain mandatory.
- `tests/test_context_completed_progress.py`: production-loop repeated-check and external dependency-change regressions plus inherited gate checks.
- New `tests/test_context_recovery_functional.py`: real baseline gates and actual file bytes at 1/2/3/4/5/8/10; real scheduler/leaf persistent-provider failure; sibling-scope negative; productive recursive children with parent completion acceptance assertion.
- `scripts/verify_level2_offline.py`: includes new functional and dependency scheduler suites. `.gitignore` additionally excludes private generated projects 19/20. No model, timeout, budget or routing default is changed.

Important controlled discovery: the productive recursive test initially omitted NEW_PROJECT bookkeeping and used a scripted sequence insufficient for parent context. Those were fixture defects, retained in diagnostic logs, not asserted as production causes. Once corrected, children independently verify their own exact outputs, but parent integration still rejects its existing-file impact contract. That genuine unresolved boundary is retained as a failing acceptance test, not hidden by a mock aggregator or broader mutation permission.

### G. Controlled Evaluation

Commands and exact source pins are in the phase offline results. Root-relative command:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/verify_level2_offline.py --output-dir audit_runs/new-research-offline
```

The initial reviewed-source broad cohort passed new bounded recovery, changed-dependency revocation and existing suites except historical fixture/recovery issues. Subsequent productive recursive probing added child-scope correction and exposed parent integration failure. Use the **latest child-scope cohort** for current results; do not relabel earlier pins final. The acceptance test deliberately asserts parent `done`; its failure is genuine unfinished functionality. Do not count that test as a pass merely because children succeed.

Baseline controlled recovery actually writes and compares exact bytes for seven artifact counts, reaches native proofs, Falsifier, impact comparison and transaction completion. Only provider/planning responses are scripted. The recursive failure test uses real `_execute_children`, `solve_task`/leaf execution and context gate; parent cannot pass when required child work is unverified. The productive test checks actual child bytes/status before asserting parent completion. Existing dependency tests exercise scheduling, partial failure and propagation with injected leaf results; distinguish them from full real-leaf execution.

Not established: full ROOT model-generated decomposition across all counts, interdependent native artifact semantics, automatic in-place revalidation/recovery, or final-source same-session recursive continuity. Historical suite failures remain disclosed. Overlapping suites/inherited cases are not summed as unique tests.

### H. Genuine Ollama Evaluation and Specifier Investigation

One reviewed-source baseline attempt reached host preflight failure `CANARY_PROVIDER_FAILURE`, 0/3 canaries, no task run ID. Record is under phase `live-final-reviewed/structured-blocks/result.json`. No Builder/task success occurred. This attempt predates the final child-scope probing/correction; there is no current final-source live PASS. Additional inventory/different-recursive live attempts are deferred because the provider qualification failed and the deterministic parent acceptance case is still failing. Repeating expensive runs cannot close that known software boundary safely.

For `20261023T012433-0023e35a`, the retained Specifier request used approximately 1350 estimated context tokens and `num_ctx=4096`, with no matching successful Specifier response. The configured provider timeout is 120 seconds. Provider-stage timestamps, not process exit, identify the timeout; task metrics retain two model calls and zero tools. Successful baseline has nine completed provider responses; failed recursive has 36 completed responses among 39 requests and recorded later provider failures. The comparison extraction keeps request/response timings and unmatched stages separately. Since repeated requests share role names, the role-keyed unmatched summary does not represent all historical timeout counts; original traces remain authoritative.

Preflight passed for the earlier timed-out run, but does not prove memory/latency remained healthy during Specifier. Exact model-loading duration and contemporaneous memory at that request are unavailable in the retained trace. Host records are workspace snapshots and not per-request telemetry. Prompt size alone does not prove unnecessary context or a defective timeout. No model call is removed and no timeout is increased without evidence. Provider responsiveness remains independent of the demonstrated controller loop defects.

### I. Remaining Failures and Issue Register

| ID | Status/severity | Evidence, next action and closure test |
|---|---|---|
| RR-1 | Confirmed/high | Real controlled children finish, parent existing-file impact integration fails. Define an appropriately scoped verification/integration contract using current child receipts; prove all read-only and mutation-negative gates before changing production. |
| RR-2 | Unverified/high | Full successful recursive/dependent-artifact matrix and model-generated ROOT decomposition. Extend real scheduler/leaf tests without mocked success/aggregator. |
| RR-3 | Confirmed/high | Provider canary failure / historical Specifier timeouts. Qualify local provider; final-source baseline, inventory and different recursive task must finish all gates. |
| RR-4 | Limited/medium | Material drift revokes permission and stops; automatic node refresh/revalidation remains unimplemented. Test fresh-node recovery and stale scope/authorization negatives. |
| RR-5 | Baseline/medium | Missing fixtures and V26 failures unchanged by earlier comparison; preserve and resolve authentic portable evidence separately. |
| RR-6 | Unverified/medium | Alternating no-progress operations and cross-turn/child progress beyond this completed-prerequisite class require broader adversarial tests. |

### J. Level 2 Readiness Decision and Next Manual Tests

**INCOMPLETE.** New evidence establishes controlled safe forward progress after one redundant prerequisite and scope-bounded productive children; it does not establish successful final parent integration or live recursive reliability. The failing parent acceptance regression is a blocker, not an accepted limitation for declaring completion. Prior papers provide design guidance only. No Level 3, R_UPDATE_004 or publication work occurs.

Windows manual entry from the repository root:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 mini.py --no-bootstrap
```

Select a fresh workspace. First repeat the exact two-file request from the preserved registry; independently compare UTF-8 bytes, not only the response. After provider qualification and RR-1 closure, repeat inventory in another fresh workspace and then a different recursive workload, preserving every run ID/trace. For controlled regression use the offline command above; it is expected to exit nonzero while RR-1/baseline failures remain. Do not test by overwriting project-18 or historical evidence. A new task in a previously used workspace must still respect existing-file authorization.

**Current phase manifest:** production changes `mini.py`, `hivo/context_sufficiency.py`; tests `test_context_completed_progress.py`, new `test_context_recovery_functional.py`; offline runner and scoped ignore rules; this same report and new evidence packet. Source/derivative hashes distinguish raw originals and sanitized copies. All work remains unstaged/uncommitted; protected refs/PRs are unchanged. Full historical phases above are preserved, not rewritten as successes.

Phase review note: the original offline runner pin list omitted `hivo/context_sufficiency.py`; the phase manifest records its actual final SHA-256 alongside seven existing production pins. The runner is corrected for subsequent cohorts; historical result JSON is not rewritten. The final reviewed child-scope cohort has 4 functional acceptance tests: 3 pass, 1 parent integration failure. Context completed-progress has 11 passes; scheduler 9 passes. Other suite results and baseline failures are listed in the phase README.


## Publication Checkpoint — Complete Current State, Phase H/I and Review Boundary

# Publication checkpoint — Level 2: INCOMPLETE

23 October 2026, Africa/Cairo. This checkpoint documents the existing implementation. No production repair is made during publication. The complete chronological report is [R_UPDATE_003](R_UPDATE_003.md); the technical history, research phase, failed attempts and earlier appendices remain retained there. This document supplies the latest Phase H/I, review navigation and publication boundary.

## Branch ancestry and review scope

Starting branch `codex/level2-generalized-recovery`, HEAD `9957271c8e66d10bdfa5b408c74d26fcd7b78be2`, index empty. Team upstream main is `f842fb8fb6e63e3064891d26ee0b24981e55c847`. PR #5 and #6 were inspected using the authenticated GitHub API: both open/unmerged, both target upstream main. PR #5 head is `cca388daa3537030abdb7b6cf175d847f23b99ec`; PR #6 head is the starting HEAD. Their branches are not changed.

The new checkpoint targets upstream main and is explicitly **cumulative**: four existing ancestor commits contain the previously proposed impact/Level 1 work, followed by this new Level 2 checkpoint commit. Reviewers must not interpret the entire main comparison as newly implemented Level 2 functionality. The new commit itself is the incremental Level 2 diff against PR #6. This preserves dependencies without rebasing/cherry-picking or hiding unmerged changes. It is a new Draft/WIP PR, not ready to merge and not a replacement merge instruction for #5/#6.

## Phase H — Latest independent manual tests

Both runs are recorded in `list/project-21`, model `gemma4:e4b`, source mini.py SHA-256 `5a5c337ee868408706ff31b35090c88f2d071f3a50be8481294e67f502aefeae`, matching the checkpoint production file. The shared stored host qualification identifies PASS. Same workspace/host-preflight identity does not independently prove one CLI process. Exact requests, classifications, metrics and source identity are in [latest-run-registry.json](../evidence/level2-generalized-recovery/checkpoint/latest-run-registry.json).

### H.1 — `20261023T160330-5a172f42`

The user supplied three explicit inventory file blocks and detailed safety/verification requirements. Source compilation retained three artifacts. Host preflight passed. The classifier returned EXISTING_PROJECT with the reason “the request assumes an existing implementation but no project files were observed”, while reconnaissance reported REPOSITORY_EMPTY. The run failed before Builder: one model call, zero task tools, zero Falsifier, root false. See [trace](../evidence/level2-generalized-recovery/checkpoint/20261023T160330-5a172f42-trace.json) and [selected tool events](../evidence/level2-generalized-recovery/checkpoint/20261023T160330-5a172f42-tools.json), which are empty for that run.

`mini.py::classify_project_mode` delegates to `hivo/project_understanding.py` through `stage2`; inventory classification and request interpretation are distinct inputs. The stored reason establishes which branch won, not which prompt token caused it or whether prior state was causal. Those remain investigation questions. Do not claim a confirmed cross-workspace leak, empty-inventory caching bug or newly repaired classifier. The user impact was failure despite complete file source data; the engineering impact is that later execution cannot be evaluated until routing admits the task. Required closure: reproduce exact request, compare classification inputs/reasons in clean and sequential sessions, then test general empty-workspace creation requests without overriding intentional existing-project requests.

### H.2 — `20261023T160636-e485f2be`

The simpler three-file request selected NEW_PROJECT. The trace enters recursive ROOT, records `[FIT ROOT] SPLIT`, creates children and executes child 1. It no longer exhibits 28 redundant context calls. Builder `write_file products.txt` is recorded **succeeded**, followed by a failed `run_file products.txt` reporting unsupported `.txt` execution. The persisted success proves a write occurred during the transaction; it does not prove lasting final output. Falsifier read the file, then twice attempted `echo -e ... > products.txt`; both were refused because shell composition/redirection is prohibited. No authorized write by Falsifier or command-security bypass is evidenced.

The deterministic verification path reported `VERIFICATION_EVIDENCE_UNAVAILABLE`. Repairer attempted executable verification for text/metadata and attempted `write_file process_products.py` four times. All four writes failed with `IMPACT_CONTRACT_REQUIRED`; executable/read command failures are retained separately. Repairer successfully read products/host metadata, which is read access, not evidence that creating or executing a helper was authorized. `run_file .agent_host_preflight.json` failed. These actions demonstrate relevance/tool-selection and proof-routing problems without implying guards were bypassed.

Fresh verification still failed after the repair limit. Child 1 was classified IMPLEMENTATION_ERROR; children 2/3 have recorded provider timeout/ENVIRONMENT_ERROR outcomes. Parent integration was not reached. Metrics: 50 model calls, 25 tools, one Falsifier, nine Ollama timeouts, `root_verified=false`, `status=failed`. The [ordered tool events](../evidence/level2-generalized-recovery/checkpoint/20261023T160636-e485f2be-tools.json) and [full sanitized trace](../evidence/level2-generalized-recovery/checkpoint/20261023T160636-e485f2be-trace.json) distinguish attempts, successes and refusals.

The trace records one transaction rollback. An independent read-only inventory after this run found **no non-runtime task files** in project-21: products.txt, supplier.txt, shipment.txt and process_products.py are absent. Runtime logs/database/preflight remain preserved. This is the final observed filesystem state, not a claim that no intermediate write happened or that every possible earlier state can be reconstructed.

### H.3 — Design decision at publication

These are documentation findings only. Allowing redirection, granting helper-file writes, treating readbacks as universal proof, suppressing Falsifier or routing all tasks to baseline would conceal the failing boundaries. None is implemented. Relevant source surfaces are `mini.py::falsify_task`, `analyze_verification_applicability`, `_verification_aggregation`, `evidence_gate`, `repair_task`, `execute_leaf` and `hivo/verification_routing.py`. Source-hash identity supports comparison with the current implementation, but it does not establish which internal candidate/hash/projection caused unavailable text proof. The next phase must trace that identity end to end before changing behavior.

## Phase I — Before/after engineering assessment

| Mechanism | Initial behavior | Implemented change | Evidence | Current status | Remaining gap |
|---|---|---|---|---|---|
| Source extraction | Concatenated literal duties collapsed | Independent source obligations/provenance | Initial/project-12 packets; latest three compiled artifacts | Controlled and live improvement | General unconstrained prose not proven |
| Multi-file parsing | Complete blocks/maps rejected | Typed blocks and prose-wrapped JSON | Project-12 actual inputs and CLI tests | Bounded grammar works in tested cases | Beyond ten artifacts/unrestricted syntax unproven |
| Clarification | Complete answers rejected; new task intercepted | Workspace-bound task/answer history and partial retention | Nine project-12 tests | Controlled improvement | Broader recursive continuation unverified |
| Project mode | Request interpretation could contradict empty inventory | No classifier repair in this update | Latest H.1 | Open | Exact-input classification investigation |
| Baseline | Original execution looped | Native source-bound progress and final gates | Manual `004235-79109aeb`; controlled matrices | Genuine historical PASS | Broad final-source live requalification |
| Decomposition | Generic child duties | Existing scheduler retained; child literal binding narrowed | Recursive production scheduler tests | Partial | Full dependent-artifact/ROOT matrix |
| Context sufficiency | Completed check stayed available | State-aware tool projection and retained JSON proof | 11 context tests; latest Builder progress | Improved | General automatic refreshed-node recovery |
| Builder progress | Repeated prerequisite exhausted 28 turns | Bounded factual corrective feedback | Seven controlled artifact counts; H.2 write | Controlled recovery and genuine observed progress | No current recursive ROOT completion |
| Tool repetition | Early context branch bypassed stall guard | Suppress redundant dispatch; bounded stall event | Real Worker-loop test | Specific loop protected | Alternating/no-progress classes still incomplete |
| Mutation grounding | A successful action was not proof of correctness | Existing guards retained; no claim of general grounding repair | Experiment/authorization suites | Tested restrictions remain | Latest relevance/Repairer path needs inspection |
| Child scope | Parent literal set could enlarge child duties | Intersect authoritative source with child scope | Sibling-scope test, productive children | Controlled improvement | Full dependent scope and provenance matrix |
| Falsifier | Missing coverage or unsuitable actions | Controlled missing-readback coverage and native proofs | Earlier scale inspections; H.2 refusals | Partial | Read-only role/tool relevance and literal route gap |
| Behavioral verification | Write/read completion could lack typed proof | Digest-bound native obligations/routes | Controlled exact-byte and gate tests | Controlled success; live failure persists | H.2 `.txt` execution unsupported/evidence unavailable |
| Repairer | Generic retries can diverge from task | Existing scope/impact enforcement retained | H.2 helper-file refusals | Guards held; recovery ineffective | Relevance and allowed verification capability |
| Impact authorization | Missing/generic targets impeded progress | Source-bound candidates and scoped child duties | Impact tests; H.2 blocked unauthorized writes | Restrictions demonstrated | Current text candidate/proof lineage; parent contract |
| Parent Integration | Completion depended on parent verification | Real child acceptance test retained | New functional suite: parent FAIL | Open | Verification of existing child outputs without new write authority |
| Provider timeouts | Host/Specifier/child failures | Bounded calls and evidence separation, no budget increase | 15/17/18 and latest nine timeouts | Open environment/provider issue | Stable qualification and request telemetry |
| ROOT verification | Failed/incomplete work could not demonstrate success | No weakening of final gates | Latest false root; failing parent acceptance | Correctly remains failed | All required artifacts and gates must pass |

## Current Status — What Works, What Does Not, and Where We Stopped

### What Works

The historical genuine two-file baseline run has independently checked exact bytes, native proofs, Falsifier, impact comparison and commit. Current controlled flows preserve literal bytes, accept supported complete clarification, isolate independent task source, bound completed-context repetition and recover when a valid next proposal arrives. Latest genuine H.2 progresses beyond the old context loop and records a successful transactional file write. Refused redirection/helper mutations show enforcement, not successful verification.

### What Is Partially Working

Controlled artifact-count 1/2/3/4/5/8/10 workflows pass real filesystem/gate checks with scripted model responses. Child-scoped execution produces independently checked outputs in a controlled recursive test. Material drift revokes permission before dispatch, but automatic in-place revalidation is not implemented. These are narrower than live generality or ROOT completion.

### What Remains Broken

1. Falsifier action selection and read-only verification relevance: H.2 attempted redirection rather than completing supported proof.
2. Literal-text behavioral proof routing: `run_file` returned unsupported text and final evidence was unavailable in H.2 despite controlled native success elsewhere.
3. Repairer relevance and recovery: helper execution/creation attempts diverged from the literal task and correctly hit authorization blocks.
4. Recursive parent integration: controlled children finish, parent existing-file Impact Contract is incomplete. Latest live run never reaches this boundary.
5. Project-mode consistency: H.1 EXISTING_PROJECT versus REPOSITORY_EMPTY remains unresolved.
6. Local Ollama qualification/timeouts: latest run has nine; historical canary/Specifier failures remain.
7. Broader-suite debt: verification-policy fixture errors and V26 failures remain; one new parent acceptance test deliberately fails.
8. General no-progress/revalidation: automatic node refresh, alternating-operation progress and broad recursive state propagation are not established.

### Where Development Must Resume

First preserve/reproduce H.1 classification inputs and H.2 verification lineage using offline controller replay. Trace accepted child scope, source hashes, active contract identity, `run_file` eligibility and Falsifier/Repairer capabilities. Close read-only literal verification and relevance while retaining authorization negatives. Then complete child verification reliably; only then evaluate parent integration using current verified child outputs and a properly scoped parent contract. Extend dependencies/material-drift/recovery tests. Finally qualify Ollama and run bounded final-source baseline, inventory, different recursive workload and sequential-state scenarios. Provider errors must remain separate from software failures. Do not start Level 3.

### Level 2 Exit Criteria

Require exact intended artifacts and no unauthorized changes; source/count/newline preservation; current context and impact authorization; native verification; independent Falsifier/applicable behavioral gates; verified required children and correct parent integration; impact post-state comparison; successful transaction; ROOT `done` and `root_verified=true`. Demonstrate baseline and at least two distinct recursive workloads using final-source genuine Ollama, with controlled independent/dependent/partial-failure and stale-proof negatives. No control-flow patch or scripted pass substitutes for those live outcomes. Baseline regression debt must be explicitly resolved or separately accepted, never silently reclassified.

## Outstanding issue register — publication checkpoint

| ID | Severity / status | Confirmed evidence / suspected cause | Next action and closure test |
|---|---|---|---|
| CP-CLASS | High / open | H.1 classification reason contradicts empty inventory; exact trigger unconfirmed | Exact raw-request clean/sequential replay; preserve intentional existing-project behavior |
| CP-LITERAL | High / open | H.2 text run unsupported and evidence unavailable | Trace source/candidate/native receipt identities; exact text verification through real child/Falsifier/final gates |
| CP-FALSIFIER | High / open | H.2 redirection attempts refused | Reproduce role tool surface; enforce/read independently without weakening command restrictions |
| CP-REPAIR | High / open | H.2 irrelevant helper writes refused; repair limit reached | Task-relevant bounded repair and safe-stop tests; unauthorized helper creation must remain rejected |
| RR-1/PARENT | High / confirmed | Controlled three children verified; parent impact contract fails | Proper existing-output verification contract; parent PASS plus stale receipt/write-negative cases |
| RR-2/GENERAL | High / unverified | Full recursive/dependent matrix incomplete | Real ROOT/leaf/scheduler varied counts and partial failures without mocked aggregation success |
| RR-3/PROVIDER | High / confirmed | Nine latest timeouts, historical canary/Specifier failures | Qualify local model; record stage durations/resources; bounded final-source completions |
| RR-4/REFRESH | Medium / partial | Drift stops safely; no automatic refreshed-node continuation | New-node revalidation with changed evidence, scope and authorization negatives |
| RR-5/BASELINE | Medium / known debt | Missing prompt/live3 fixtures and old expectations | Authentic portable fixture resolution; retain original failure comparisons |
| RR-6/PROGRESS | Medium / unverified | Specific completed-check class tested | Alternating actions, unchanged outputs and meaningful evidence novelty tests |

## Test registry and evidence boundaries

Earlier cohorts are not new publication-time executions. The retained `recursive-progress/focused-results.log` reports 66 OK and compatibility log 104 OK; the counts overlap. The latest research `offline-child-scope-final/results.json` reports completed-context 11 OK, recovery functional 4 executed/1 failure/0 errors, scheduler 9 OK, Level 1 10 OK, generalized 20 OK, prior/project-12 clarification 9/9 OK, greenfield 17 OK, impact 27 OK, context 9 OK, applicability 15 OK, authority 23 OK, experiment 122 OK, architecture 90 OK, understanding 32 OK, model policy 4 OK, requirement clarification 49 OK with its known live-provider exclusion. Verification-policy 8 executed/2 errors; V26 186 executed/24 failure records/2 errors/3 skips. Recovery failure/error identities match preserved baseline. Do not sum these counts or infer unique coverage.

The exact root-relative broad command is `.\.venv\Scripts\python.exe -B -X utf8 scripts/verify_level2_offline.py --output-dir <fresh-output-directory>`. Individual log headers identify exact test names, including mutation-grounding under experiment discovery and existing-file negatives under greenfield lifecycle. The new parent test remains an ordinary failed assertion, not skipped or expected-failure. The publication task performs structural/link/privacy/hash/staged-blob checks; it does not claim a new runtime test cohort or start another repair phase.

## Code and evidence navigation

Production modules: `mini.py` (ingestion, exact operations, context/impact lifecycle, progress/recovery, recursive child binding and diagnosis); `hivo/artifact_progress.py` (source literals, native equivalence, progress); `hivo/literal_source.py` and `literal_clarification.py` (typed parsing/task continuity); `hivo/context_sufficiency.py` (revocation); `hivo/requirements.py` (independent source records); `hivo/pre_mutation_impact.py` (anchors/identity); `hivo/verification_routing.py` (full literal route coverage/current readbacks). Each exists in this checkpoint with its unresolved boundaries; no source is altered during publication.

Regression files: existing Level 1/adaptive tests updated for changed tool ordering; added Level 2 generalized, clarification lifecycle, project-12, completed-context and recovery-functional tests, plus exact input fixture. Scripts: Level 1 replay, Level 2 replay, clarification replay, independent read-only inspector and offline runner. `.gitattributes` defines canonical LF for curated evidence; `.gitignore` protects private originals. Research references/decisions remain in R_UPDATE_003's research section; scientific results are never presented as Mini Hivo verification.

[Checkpoint manifest](../evidence/level2-generalized-recovery/checkpoint/manifest.json) distinguishes original source SHA-256 from sanitized derivative SHA-256. Seven project-21 originals and ZIP are preserved privately. Traces/tool selections retain outcome and refusal provenance while replacing absolute machine paths. Sanitized authorization-related copies are evidence, not reusable runtime authorization. No raw SQLite, host inventory, cache, temporary workspace or backup is intended for publication. Earlier public raw Git history remains accessible and is not erased by this commit.


Publication integrity review: 203 derivative/source pairs validate against actual staged Git blobs. Eight Python files receive normal Git source line-ending normalization; the checkpoint manifest records tested Windows bytes and published blob SHA-256 separately. Parsed AST equality passes for all staged Python files; no implementation edit was made. Historical source pins identify Windows tested bytes rather than a platform-independent checkout hash. `git diff --cached --check` reports three reviewed formatting diagnostics (two retained log trailing spaces, one clarification-module EOF blank line); this check is not represented as passing. Preserving those bytes avoids silently rewriting evidence/implementation during the documentation checkpoint.

[Consolidated retained Level 2 run registry](../evidence/level2-generalized-recovery/checkpoint/COMPLETE_RUN_REGISTRY.json) records 111 retained task-run identities with workspace, date, source hash where available, metrics, prompt references and evidence availability. Host-only failures remain separately documented without fabricated IDs. Missing fields remain null; requested automatic mode is not mislabeled as its resolved route.
