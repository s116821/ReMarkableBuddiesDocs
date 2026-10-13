# Selected Reader request and draft publication

## Missing application behavior

Rust62a5376 has ordinary Ledger create/advance/append, selected immutable reads,
controlled Pending/context and guarded backend dispatch. Actual Attempt uses
ordinary writes for interpretation and Generated drafts; these cannot substitute
for selected publication. Add the selected mutation path using existing
Store.commit_selected and canonical admission. This supplies no SDK capture
producer or production live source verifier. The extra collected-ingestion CLI
is deferred; its local design is preserved separately.

## Domain contract

SelectedAdmission supports interpretation of an acknowledged Prepared Reader user
turn and creation of its Generated assistant draft. Inputs: stable operation ID,
original accepted token, exact root/user IntentRecordRef, bounded text/timestamp,
and new assistant ID for generation. Reject arbitrary caller Envelopes, roles,
outcomes, sequences, completion, bindings, source replacement and descriptors.
Use existing schemas and deterministic per-operation record/revision IDs.

Under domain-before-Store admission, recover original operation before checking
current selection. Validate its original transaction/receipt fingerprint against
logical input including original token and references. Changed payload/pins
refuse. Historical retry returns original acknowledgment/pins only, never a live
context. Do not substitute retained/ordinary winners or allocate new IDs on retry.

New publication requires current token, strict complete selected projection and
exact current root/user heads. Interpretation requires Reader/Prepared user;
generation requires Reader/Interpreted user with text. Existing source links and
required media must be present in this selected closure and belong to the same
conversation/user. Omission, tombstone, malformed/foreign input, unavailable media
or ambiguity refuses. This is historical input integrity, not native authority.
Preserve sources, exchange and original created time. Interpretation advances the
user; generation creates assistant at root.next_sequence and increments once.
Updated time cannot precede acknowledged chronology; reject empty/oversized text,
nil/colliding IDs and sequence overflow before publication.

Commit root, turn and existing schema-1 non-admitted Receipt together through
Store.commit_selected. Preserve unrelated records, retained closure and media;
no ordinary intermediate commit, registry, schema migration or binding. Read back
acknowledged records before success. Lost acknowledgment recovers before stale
head refusal; response failure never retries mutation.

## Actual Attempt and remaining dependency

Actual Attempt gains selected state retaining admission, acknowledged root/user
pins and actual publication token. Interpret/generated use selected operations,
update only from acknowledged publication and never fall through to Ledger
ordinary writes. Install input state only from strict current acknowledged
preparation, not historical receipt/arbitrary strings. Ordinary/development paths
retain existing behavior. Failed selected writes stop later provider/effect work
at actual Orchestrator boundaries. Backend Ok never becomes Completed.

Evidence must be durably selected before input-state installation/first provider
call. Qualified SDK capture production and live source binding remain missing;
synthetic/development correspondence cannot satisfy them. After Generated
acknowledgment, orchestration can finalize plan, use existing controlled
prepare_reader, install its result and dispatch through guarded facade.
Historical result never dispatches. Production SourceAdmission and settlement,
branch-dependent render_answer, trigger/history/status remain unsupported until
separately qualified; full task2.10 stays open.

## Verification and delivery

Review exact contract before code. Test actual domain/Attempt routes: chronology,
exact source preservation, reopen/identical retry/lost acknowledgment, changed
payload/pins, stale/replaced selection/root/user, malformed/omitted/foreign input,
missing media/oversize, no ordinary fallback and write failure stopping later
provider/effects. Historical results cannot initialize fresh Attempt or dispatch.
Recording fixtures prove storage/admission only. Run exact source checks and
required strict lint without suppression; publish paired evidence and independent
review while keeping SDK/native/full lifecycle gates open.

Source basis: exact Rust62a5376, accepted reader-admission-api and selected Store
semantics. This is precode design, not completed application/native integration.

Exact SDK d01 source assessment confirms CapturedBatch.export_facts already
provides immutable source/parent/ordered derivative provenance. Existing Buddy
HistoricalCapture.from_batch maps it; parent and image bytes remain separately
owned. Current SDK origin/qualification/clock/render binding are synthetic only,
and UnqualifiedPlatform.capture is Unsupported. No qualified live producer exists.
Reuse existing historical mapping without relabeling its SDK_SOURCE2d473f09
provenance or updating protected pins. Native origin/profile/clock/render/ownership
semantics require the separately reviewed SDK amendment and qualified producer.
The source assessment is not new capture or effect qualification.
