# Acceptance and delivery checklist

- [x] Read REM-52 and prerequisite/domain/Manager issue chronology; inspect REM-36 source and central contracts and active REM-37 record types.
- [x] Inspect provider documentation and maintained sync prior art; distinguish candidate mechanism from live-provider proof.
- [x] Propose modes, conditional publication, source-document projection, local fencing, media/restore/status contracts before implementation.
- [x] Obtain independent review at ebf8c72 accepting generic fixed-ID metadata create-or-read and transport fixtures only.
- [x] Obtain independent review accepting the admission/settlement/projector/application-matrix contract at 7e06d9; no implementation or live qualification follows from this acceptance.
- [x] Obtain Main's exact0830a9af owner review5442770097 and refreshed673c mapping; SCRAPPY owns storage, Main owns domain/journal/backend paths. Schema2 acceptance remains coordinated separately.
- [x] Obtain Main's efb8fd73 review accepting the coordinated proposal for an isolated selected-store/projector fixture slice; add history/bitmap admission coverage and propose the precise token/commit/activation/journal interfaces for owner agreement.
- [ ] Review the precise interfaces/journal extension with Main before shared domain/workflow edits; verify and independently review the disconnected real-store projection fixtures without claiming activation/admission implementation.
- [x] Read Main's exact0830a9af owner agreement (2026-10-07T13:09:56Z): SCRAPPY's selected storage implementation is unblocked; Main retains domain journal/projector/admission ownership.
- [ ] Complete and review the selected snapshot read-path increment, then implement guarded commit and one durable winner-plus-retained activation with original-selection replay and fault recovery. Interface agreement is no longer a blocker for this storage work.
- [ ] Implement and verify the accepted generic adapter slice without enabling shared-mode publication.
- [ ] Qualify or reject the candidate provider primitive using an explicitly authorized disposable app-data namespace; preserve reproducible evidence without secrets.
- [ ] Implement accepted generic scope/selection and conditional transport seam, reusing REM-36 domain-opaque storage and bounds.
- [ ] Implement mode/binding isolation, bootstrap/catalog registration, outbox replay and first-winner replacement without stale auto-rebase.
- [ ] Integrate domain-owned aggregate projection and in-flight operation fence without duplicating REM-37/24/26/53 schemas or granting native authority.
- [ ] Implement versioned OS/file status, explicit portable configuration/media policy and validated selected-backup maintenance contract for REM-42.
- [ ] Verify two-client same-base winner, sequential A-to-B transfer, different-document/global preservation, clock skew, stale offline attempts, lost acknowledgement and interrupted publication.
- [ ] Verify clean/replacement tablet bootstrap, deletion/tombstones, corrupt/unknown-schema/interrupted restore, native page lag, active operation invalidation and intentional/incomplete media.
- [ ] Verify join/leave/switch/local-only and isolated backups cannot publish emptiness, merge namespaces, delete other backups or reuse device secrets.
- [ ] Run relevant Rust checks/simulator coverage and central Docs checks; distinguish host/provider/native evidence and remaining gates.
- [ ] Publish exact linked Docs/Rust revisions, inspect CI/bot feedback, obtain final independent review and coordinate merge order.
- [ ] Sync final as-built canonical contracts and archive completed scope only; retain unperformed provider/native qualification as explicit unresolved work rather than checking it off.

- [ ] Independently review the guarded commit/atomic activation increment: bounded hash-linked accepted history, original-selection replay, shared ancestor context, abrupt process-exit recovery, stale token/causal conflicts, media refusal and unrelated scopes.
- [ ] Implement portable selected backup/restore/migration policy before enabling these maintenance paths for selected stores; current explicit refusal prevents silent metadata loss.
