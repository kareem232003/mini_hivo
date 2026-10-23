# Level 2 generalized recovery investigation

Candidate R_UPDATE_003; implementation and verification remain uncommitted. Base: `9957271` (PR #6 head at branch creation); PR #5 and PR #6 branches are unchanged. Their current GitHub state is not rechecked during this local-only repair.

**Latest local repair (23 October):** see [project-12 clarification repair](project12-repair/README.md) for four additional manual failures, typed block/map parsing, task/answer isolation, final reviewed-source controlled results and failed/blocked live attempts. R_UPDATE_003 remains incomplete: final-source genuine completion is unverified. All prior packets and original evidence remain preserved.

**Earlier checkpoint:** [clarification/Falsifier repair](clarification-repair/README.md) documents Failures B/C and their own source pins. The historical records below retain their original scope and do not describe the latest checkout.

## Confirmed original failure map

Original run `20261022T005130-de9aff61`, model `gemma4:e4b`: 142 trace records and 28 persisted tool events: 17 refused shell commands, four writes, five reads and two context decisions. Builder exhausted its 28-step budget before Falsifier, applicability routing and impact comparison. The original workspace was rolled back; exact persisted output bytes are unavailable. SQLite readbacks retain three newline-separated fields; whitespace-compacted failure summaries must not be used as byte evidence.

| Mechanism | Evidence and consequence |
|---|---|
| Source interpretation | Concatenated exact multi-file input yielded one source requirement. The accepted generic impact candidate had 12 targets and no source-bound literal post-state hashes. It did not supply independent byte oracles. |
| Recovery activation | Level 1 native guidance and refusal termination required accepted literal hashes; no hashes meant neither mechanism activated. |
| Repetition / handoff | Ordinary readbacks were not typed exact-byte proofs. Builder completion depended on a model response; there was no all-artifact, current-proof handoff. Successful repeated writes/readbacks did not establish formal obligation coverage. |
| Budget and diagnosis | Generic budget exhaustion occurred after the tool loop. Diagnosis lacked a denial/stall category and used a small compacted evidence window, yielding unknown/low confidence rather than an evidence-directed recovery action. |
| Additional scale defects found by controlled tests | Literal routes were truncated to three. Impact anchor construction truncated to 700/800 characters while validation compared 900-character prefixes. Windows text writes translated LF into CRLF. These were independently reproduced, not inferred as causes of the original rollback. |

## Scope and oracles

The user confirmed these UTF-8 contents without a final newline:

- `student.txt`: `Name: Sara\nAge: 21\nDepartment: Computer Science`
- `course.txt`: `Course: Software Engineering\nSemester: Fall 2026\nStatus: Active`

`\n` above represents LF. The fresh replay encodes confirmed boundaries explicitly as JSON strings. It is a clarified replay, not an unchanged replay of the ambiguous historical prompt. Historical bytes were not reconstructed or edited. The unclarified historical shape must return one targeted clarification before mutation.

The provider-free replay scripts model responses only. Actual context/impact authorization, tool dispatch, filesystem writes/readbacks, Falsifier, final aggregation, post-state comparison and transaction commit/rollback remain active. Scale cases exercise 1, 2, 3, 4, 5, 8 and 10 artifacts. More than ten is explicitly unsupported by this bounded compiler and requires clarification; it never silently authorizes a prefix.

## Final checkpoint

- [Final-source real Ollama inspection](live/live-final-source-inspection.json): run `20261022T020137-6b8c1201`, `gemma4:e4b`, `done`, `root_verified=true`; all 13 independent checks pass and all five production hashes match the checkout. Two writes, two native Builder proofs, Falsifier read_file on each file, required final routes, impact comparison and transaction commit are observed in trace/database evidence. Nine model calls, seven tool calls, one Falsifier call, zero budget exhaustions; 399.18 run seconds / 428.15 wall seconds.
- Actual byte copies: [student.txt](artifacts/student.txt), 47 bytes; [course.txt](artifacts/course.txt), 63 bytes. UTF-8, two LF separators each, no final newline. Their exact bytes match the user-confirmed oracle and manifest hashes.
- [Controlled matrix](controlled-matrix.json): independent full inspection passes 1, 2, 3, 4, 5 and 8 artifacts. Ten outputs and all ten final routes pass, but the Falsifier reads only eight because its existing step cap is eight. The ten-file stronger inspection is FAIL / partial, despite root/driver success. No budget was increased. A bounded batched Falsifier receipt or explicit incomplete-coverage gate is the next technical correction for that scope.
- [Targeted results](targeted-results.json): 20 passing controlled/regression tests, including wrong-byte rollback, stale proof invalidation, alternating failures, transaction ownership, Repairer edit/range exact writes and mixed-language/typo cases. These do not prove general language understanding or erase the independently found ten-file limitation.
- [Offline results](offline/results.json): passing focused suites are separate from functional proof. Verification-policy has two missing-fixture errors. Recovery has 24 failure records, two errors and three skips across 186 tests, matching unchanged-base identities. A separate suite cannot initialize its missing historical plan fixture. These remain failed/unavailable.
- [Live cohorts](live-results.json) retain four intermediate source variants plus the final source separately, not a repeatability rate. Replays clarify the confirmed byte boundaries; no unchanged ambiguous-prompt success is claimed.

The read-only [inspection script](../../scripts/inspect_level2_replay.py) checks actual bytes, authorized contract-bound proofs, context-before-write, independent Falsifier reads, route coverage, post-state and transaction evidence. It rejects an intentionally wrong in-memory oracle without changing artifacts. The driver alone checks a weaker byte/root oracle; use the independent inspection for full claims.

The [manifest](manifest.json) records 52 source/derivative pairs and canonical LF. Raw transcripts, SQLite databases and host preflight inventories are excluded. All four original failed-run files and their private ZIP backup remain hash-valid. The earlier Level 1 trace/output/first metrics row remain intact; a later preexisting project-9 run changed its whole ledger/database before this investigation, so whole-file equality with that older snapshot is not claimed. No staging or staged-blob check was performed.

## Reproduction

Use a fresh, nonexisting output directory:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/level2_recovery_replay.py --output-dir output/level2-new-controlled
.\.venv\Scripts\python.exe -B -X utf8 scripts/level2_recovery_replay.py --artifacts 8 --output-dir output/level2-new-scale
# Costly genuine local Ollama run; obtain authorization before repeating:
.\.venv\Scripts\python.exe -B -X utf8 scripts/level2_recovery_replay.py --live --output-dir output/level2-new-live
```

The real CLI uses auto mode, actual host preflight and `gemma4:e4b`; no provider functions are mocked. Application budgets are unchanged. The driver has a 600-second wall cutoff including startup/preflight, which is not an application execution-budget increase.

## Limits

This is a bounded literal-artifact correction, not general natural-language understanding or proof of complex application correctness. Supported instruction aliases and delimiters are documented in the parser; exact literal contents are not spell-corrected. Ambiguous concatenated boundaries require confirmation. Arbitrary shell commands, echo redirection/composition and ambiguous command substitutions have no automatic execution equivalent. Native read alternatives retain normal workspace/inspection/role guards. Other tasks retain existing verification gates.

Raw transcripts, databases, machine inventory and workspaces remain private. Sanitized summaries retain failures and distinguish source hashes from derivative hashes. Previously published history is unaffected.
