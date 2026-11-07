# Ordinary memory caller implementation

This finite increment is implemented in [Buddy #137](https://github.com/s116821/ReMarkableBuddies/pull/137)
at `02924ffac26527e0dea9d508e9e230f2dff7140e`, normally composed with delivered
`cb9cd0c255921385a35d4ca80b8f48815cc2b4e4`. Its accepted precode and live-run
Docs revision remains `0feadf560bc8a5aa9778035d4b910cbf3076f16f` in the same
[Docs #151](https://github.com/s116821/ReMarkableBuddiesDocs/pull/151).
The closeout normally reconciles delivered Docs
`55378445c70eb70245f9f840eb215e2637a6a55d`; it does not replace the run's pins.

## Implemented seams

| Requirement | Implementation at the source pin | Verification |
| --- | --- | --- |
| Ordinary caller memory composition | `main.rs` shares Dispatch's enabled LocalMemory Arc with captured Reader; `workflow/conversation_dispatch.rs` passes it to typed Reader, routed Writer and notebook preparation. Disabled paths create no provider or query. | Actual ordinary Reader -> Generate -> Refine -> Reader and notebook -> Reader sequences preserve exact history, returned draft identity and image associations. |
| Already-ready local memory lifetime | `mode_maintenance.rs` retains the exact Store in the existing shared mode/domain lifetime; `memory/mod.rs` adds an internal ordinary lifetime variant. `storage/maintenance.rs` adds existing-custody ReadyOrdinary admission. | Foreign Store and final-provider release controls, generation4 legacy refusal, wrong mode/selected history and missing/malformed readiness without repair. |
| Bounded separate ordinary memory snapshots | `memory/receiving.rs` reuses the existing pure result validator and query bounds; `answer.rs` counts the original payload plus labeled memory under96KiB. Reader settlement uses the original persisted Turn and original root/turn CAS. Routed Writer keeps its existing memory seam and supplied root/selection. | Scope/profile/result/bound controls, exact2048/2049-byte behavior, interpreted failure/cancellation and intervening-winner preservation. Existing dedicated Writer/selected tests remain separate. |
| Frozen notebook reducer memory | `writer/notebook/command.rs` checks consumed plans before querying, then queries archive.document once. `payload.rs` freezes a private optional snapshot and adds it only to reducer parts, including prefix/actual digests and worst-case reservation. Standalone enabled commands open ready storage before credentials/model/destination construction. | Linux actual-file empty/enriched map equality, reservation/digest sensitivity and spent-operation zero-query replay; existing notebook ownership/failure/refinement controls; Windows frozen-input scripted and live sequence. |
| Ordinary memory caller qualification | `simulator/combined/qualification.rs` adds the closed `local-fixture-v1` selector, at most two synthetic assertions and six receiving queries across seven model stages. Explicit scripted/live scenario files preserve disabled defaults and original bounds. | Scripted same-entry report, separately selected one-shot live report and independent semantic review in [verification.md](verification.md). |

The new snapshot helper owns immutable data only. It does not grant freshness,
selected membership or effects. New ordinary admission does not replace
`new_local`, `configured`, `legacy_sync_lease`, or selected receiving/publication.
There is no new dependency, Store format, memory schema, retrieval engine, sync
worker, Manager setting or native operation.

## Design disposition

The accepted design was implemented without broadening its functional scope.
The later private `from_result` extraction permits direct malformed-result tests
while preserving admission/query/validation order. A test-only invalid remote-mode
fixture initially used a production generation4 transition that correctly refused;
the fixture now restores a synthetic invalid mode without widening that API.
The real-file notebook replay test is Linux-gated because the existing external
notebook safe-open path is unsupported on Windows. Frozen in-process notebook
inputs remain exercised on Windows; that distinction is preserved in verification.

The earlier subject-memory and shared-conversation archives are unchanged.
Broader shared/isolated memory sync, migration/restore/replacement recovery,
firmware survival, native Writer input/effects and whole-feature acceptance remain
with their existing owners and contracts. This archive completes caller composition
and its bounded qualification, not those obligations.
