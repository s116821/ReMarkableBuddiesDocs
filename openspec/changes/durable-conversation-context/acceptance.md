# REM-37 authority and acceptance mapping

October 1 refresh: all current REM-37 description/comments and related platform clarifications were read in the 47-issue/138-comment audit. Native capability ownership is now ReMarkableOpenSDK, with its own canonical OpenSpec. This change owns Buddy integration only. Accepted dependency bases are Rust ff8ad75bec45fca403d55a7b6d93eb83ab732e3d / Docs8008389fa676d395401e6f28e049b47baa7b10ef. Domain work may proceed after amendment review; tasks3/4.6 cannot claim native SDK qualification from host fixtures. User October1 resume supersedes all historical90% stops; ordinary allowance to exhaustion, no credits/reset redemption. NonSDK implementation/review uses GPT6.1Sol.

Plan only. No checkbox or scenario is implemented by publishing this file. Authority read in full: REM-37 description updated September 26, 2026 at 21:28:14 UTC, its September 26 21:12:36 UTC export-correlation comment, and the resumed MVP roadmap. The correlation clarification replaces a heavyweight identity prerequisite with a portable lightweight marker. Current resume supersedes older planning-pause text. REM-46's later upstream-Action release constraint applies separately.

| Requirement | Planned implementation and evidence | Tasks |
| --- | --- | --- |
| One stable conversation per Buddy page; restart/revisit and shared Reader/Writer context | Stable root/turn IDs, deterministic binding record, reopened real Store; mixed-mode domain test; qualified native identity required | 2.1-2.5, 3.4, 4.1, 4.6 |
| Stable revisions, role/mode, state and timestamps | Versioned payloads, generic envelope parents, root-CAS sequence; clocks do not define order | 2.1-2.2, 4.1-4.2 |
| All actual source images, useful detail/crops, hash/provenance/turn links | Exact submitted byte batch persisted before provider use; parent capture and normalized transform; both modes retrieve original | 2.3, 3.1-3.2, 4.1, 4.4, 4.6 |
| Later targets in same conversation | Separate per-turn source-use records and document/page/viewport identities; page A/B fixture | 2.3, 4.1 |
| Interpreted request, visible replies, explicit corrections, failure/cancellation | Prepared versus verified interpretation, draft versus complete visible response, append-only corrections, explicit incomplete states | 2.1, 2.5, 3.2-3.3, 4.2 |
| Machine/preset instructions separate | Typed internal fields excluded from default visible history/context; no raw hidden prompts/secrets | 2.1, 2.5, 3.2, 4.1 |
| Chronological canonical history versus newest-first renderer | Sequence ordered ledger and exact view API; native renderer remains REM-38/39 | 2.2, 2.5, 4.1 |
| Interrupted write and retry without duplicate turns/exports | Operation fingerprint, full-head CAS, no replay queue; marker discovery ambiguity explicit | 2.2, 2.4, 2.6, 3.3, 4.2-4.3 |
| Lightweight portable export marker with note/scope/revision association | Existing ExportAssociation namespace, stable UUID metadata/title convention, simulated round-trip/reconcile contract; real adapter REM-23 | 2.6, 4.3 |
| Explicit context limits without silent summary/truncation | Caller budgets, exact selected IDs/text, typed refusal, separate byte/token bounds | 2.5, 4.1 |
| Inspect/export/delete and reference-aware retention | Exact shared APIs, tombstones, retained-reference report; physical collector remains REM-42 | 2.5, 2.7, 4.3 |
| Legacy coexistence and native undo boundaries | No automatic OCR/adoption/rewrite; process-local undo eligibility remains unchanged despite durable history | 3.3-3.4, 4.3, 4.6 |
| Meaningful actual Reader integration | Recording provider verifies all used bytes from real orchestration; native complete-output/restart evidence with source invariance | 3.1-3.4, 4.4-4.6 |

REM-37 acceptance proves its domain and actual Reader persistence boundary. It does not close automatic insertion, unified native conversation rendering, native mixed-Buddy UI, external backend exports, destructive media collection or restart-restored undo. Those remain explicit downstream deliverables rather than falsely passing simulated tests as native behavior. If final issue interpretation requires one of those integrated behaviors before REM-37 closure, keep REM-37 open until that dependency is verified; do not mark the issue Done merely because the library passes.
