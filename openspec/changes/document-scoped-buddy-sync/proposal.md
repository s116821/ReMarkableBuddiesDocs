# Document-scoped Buddy backup and shared sync

Status: proposed contract, not implemented or provider-qualified. Owner: SCRAPPY-DOO; REM-52. This change and its linked Rust implementation are one delivery. Independent contract review precedes implementation; canonical specs remain as-built until verification and coordinated closeout.

## Why

REM-36 provides immutable records, causal branches, recovery bundles and a bounded optional Drive worker. It does not provide the shared-sync policy now required: different source documents preserve both writers, while competing edits of the same accepted document revision select the first valid upstream commit and replace the losing local view. A filename, timestamp, local mutex or expiring lease alone cannot enforce this policy across tablets.

## Scope

- Explicit local-only, isolated device backup and selected shared-group modes, with distinct identities and namespaces. Manager-to-tablet control and restore use hardwired transport; internet access for optional cloud storage remains allowed.
- Buddy-owned durable history, bookkeeping, source references and export correlations grouped by logical source document; independent stable keys for subject memory, handwriting and portable configuration. Domain schemas remain owned by REM-37/24/26/53.
- Reuse REM-36 envelopes, content-addressed objects, media coverage, recovery validation, credentials and worker bounds. Add only the aggregate selection, conditional publication and local operation-fencing contracts needed for shared mode.
- Candidate Drive mechanism: immutable commit slots identified by provider-generated IDs known to all writers of the accepted base. A bounded create chooses the winner; no mutable shared head or distributed lease is proposed. Provider qualification remains a gate, with explicit fail-closed behavior if a claimed slot is incomplete or invalid.
- Versioned OS/file status and maintenance commands for REM-42. UI and transport implementation remain with Manager's owner.

Native reMarkable documents, rendered Buddy pages, ink and native file metadata are excluded. Turn screenshots and confirmed-learning samples are Buddy-owned media, with explicit inclusion/omission/completeness reporting. No pairing, firmware change, native mutation or personal-account sync follows from this proposal.

## Delivery and dependencies

Rust base: `s116821/ReMarkableBuddies` main `ff8ad75bec45fca403d55a7b6d93eb83ab732e3d`. Docs base: main `8008389fa676d395401e6f28e049b47baa7b10ef`. REM-37 schema inspection: `673c5781cd5d89a89d712b9d8253433c920dc37c`, especially `src/conversation/types.rs`. This reference is an integration input, not permission to copy or modify its unfinished lane. Agree aggregate projection and operation fencing with that owner before domain integration; generic transport and storage work need not acquire native capability.

Review the proposal/design/scenarios together, implement the accepted contract in the owned Rust branch, verify the exact Docs/code pair, sync canonical contracts and archive only completed scope. Neither this draft nor host fixtures closes REM-52 or the ecosystem 1.0 gate.
