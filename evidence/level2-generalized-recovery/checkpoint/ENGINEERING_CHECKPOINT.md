# Publication checkpoint — Level 2: INCOMPLETE

23 October 2026, Africa/Cairo. This checkpoint documents the existing implementation. No production repair is made during publication. The complete chronological report is [R_UPDATE_003](../../../updates/R_UPDATE_003.md); the technical history, research phase, failed attempts and earlier appendices remain retained there. This document supplies the latest Phase H/I, review navigation and publication boundary.

## Branch ancestry and review scope

Starting branch `codex/level2-generalized-recovery`, HEAD `9957271c8e66d10bdfa5b408c74d26fcd7b78be2`, index empty. Team upstream main is `f842fb8fb6e63e3064891d26ee0b24981e55c847`. PR #5 and #6 were inspected using the authenticated GitHub API: both open/unmerged, both target upstream main. PR #5 head is `cca388daa3537030abdb7b6cf175d847f23b99ec`; PR #6 head is the starting HEAD. Their branches are not changed.

The new checkpoint targets upstream main and is explicitly **cumulative**: four existing ancestor commits contain the previously proposed impact/Level 1 work, followed by this new Level 2 checkpoint commit. Reviewers must not interpret the entire main comparison as newly implemented Level 2 functionality. The new commit itself is the incremental Level 2 diff against PR #6. This preserves dependencies without rebasing/cherry-picking or hiding unmerged changes. It is a new Draft/WIP PR, not ready to merge and not a replacement merge instruction for #5/#6.

## Phase H — Latest independent manual tests

Both runs are recorded in `list/project-21`, model `gemma4:e4b`, source mini.py SHA-256 `5a5c337ee868408706ff31b35090c88f2d071f3a50be8481294e67f502aefeae`, matching the checkpoint production file. The shared stored host qualification identifies PASS. Same workspace/host-preflight identity does not independently prove one CLI process. Exact requests, classifications, metrics and source identity are in [latest-run-registry.json](latest-run-registry.json).

### H.1 — `20261023T160330-5a172f42`

The user supplied three explicit inventory file blocks and detailed safety/verification requirements. Source compilation retained three artifacts. Host preflight passed. The classifier returned EXISTING_PROJECT with the reason “the request assumes an existing implementation but no project files were observed”, while reconnaissance reported REPOSITORY_EMPTY. The run failed before Builder: one model call, zero task tools, zero Falsifier, root false. See [trace](20261023T160330-5a172f42-trace.json) and [selected tool events](20261023T160330-5a172f42-tools.json), which are empty for that run.

`mini.py::classify_project_mode` delegates to `hivo/project_understanding.py` through `stage2`; inventory classification and request interpretation are distinct inputs. The stored reason establishes which branch won, not which prompt token caused it or whether prior state was causal. Those remain investigation questions. Do not claim a confirmed cross-workspace leak, empty-inventory caching bug or newly repaired classifier. The user impact was failure despite complete file source data; the engineering impact is that later execution cannot be evaluated until routing admits the task. Required closure: reproduce exact request, compare classification inputs/reasons in clean and sequential sessions, then test general empty-workspace creation requests without overriding intentional existing-project requests.

### H.2 — `20261023T160636-e485f2be`

The simpler three-file request selected NEW_PROJECT. The trace enters recursive ROOT, records `[FIT ROOT] SPLIT`, creates children and executes child 1. It no longer exhibits 28 redundant context calls. Builder `write_file products.txt` is recorded **succeeded**, followed by a failed `run_file products.txt` reporting unsupported `.txt` execution. The persisted success proves a write occurred during the transaction; it does not prove lasting final output. Falsifier read the file, then twice attempted `echo -e ... > products.txt`; both were refused because shell composition/redirection is prohibited. No authorized write by Falsifier or command-security bypass is evidenced.

The deterministic verification path reported `VERIFICATION_EVIDENCE_UNAVAILABLE`. Repairer attempted executable verification for text/metadata and attempted `write_file process_products.py` four times. All four writes failed with `IMPACT_CONTRACT_REQUIRED`; executable/read command failures are retained separately. Repairer successfully read products/host metadata, which is read access, not evidence that creating or executing a helper was authorized. `run_file .agent_host_preflight.json` failed. These actions demonstrate relevance/tool-selection and proof-routing problems without implying guards were bypassed.

Fresh verification still failed after the repair limit. Child 1 was classified IMPLEMENTATION_ERROR; children 2/3 have recorded provider timeout/ENVIRONMENT_ERROR outcomes. Parent integration was not reached. Metrics: 50 model calls, 25 tools, one Falsifier, nine Ollama timeouts, `root_verified=false`, `status=failed`. The [ordered tool events](20261023T160636-e485f2be-tools.json) and [full sanitized trace](20261023T160636-e485f2be-trace.json) distinguish attempts, successes and refusals.

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

[Checkpoint manifest](manifest.json) distinguishes original source SHA-256 from sanitized derivative SHA-256. Seven project-21 originals and ZIP are preserved privately. Traces/tool selections retain outcome and refusal provenance while replacing absolute machine paths. Sanitized authorization-related copies are evidence, not reusable runtime authorization. No raw SQLite, host inventory, cache, temporary workspace or backup is intended for publication. Earlier public raw Git history remains accessible and is not erased by this commit.


Publication integrity review: 203 derivative/source pairs validate against actual staged Git blobs. Eight Python files receive normal Git source line-ending normalization; the checkpoint manifest records tested Windows bytes and published blob SHA-256 separately. Parsed AST equality passes for all staged Python files; no implementation edit was made. Historical source pins identify Windows tested bytes rather than a platform-independent checkout hash. `git diff --cached --check` reports three reviewed formatting diagnostics (two retained log trailing spaces, one clarification-module EOF blank line); this check is not represented as passing. Preserving those bytes avoids silently rewriting evidence/implementation during the documentation checkpoint.

[Consolidated retained Level 2 run registry](COMPLETE_RUN_REGISTRY.json) records 111 retained task-run identities with workspace, date, source hash where available, metrics, prompt references and evidence availability. Host-only failures remain separately documented without fabricated IDs. Missing fields remain null; requested automatic mode is not mislabeled as its resolved route.
