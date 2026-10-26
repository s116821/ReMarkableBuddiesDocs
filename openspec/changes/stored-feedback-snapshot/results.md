# Pre-implementation state

This is proposed behavior only. No source/API implementation, new provider/model call, device action, deployment or qualification is claimed. Source016d78a and Docs mainb66d1b9 contain the separately accepted Reader delivery. Original Reader, native, selected, pending feedback and held failed/spent handwriting work remain preserved.

Current source inspection finds a static catalog with an explicit caller-validation/pending-persistence boundary, ordinary Ledger current-head decoding and existing Store/mode snapshots. The proposed receiver uses stored associated facts rather than inventing another pending record domain. Its limitation is explicit: it does not establish unpresented state or retain a failure before any durable fact exists.

Source basis: current REM-40 description/all32 comments, delivered canonical feedback/layout/ledger contracts and direct current source inspection. The optional advertised Linear field-notes operation returned ToolNotFound; no external field notes were assumed. Scope and implementation remain pending independent review.


## Precode review correction

Independent review found the original completed/no-error promise unreachable: Ledger::decode permits Completed OutcomeFact only with schema two plus VerifiedSubmitted settlement, while this receiver excludes schema two. The corrected proposed API returns Result<FeedbackDescription> and refuses unsupported completed records, preserving the existing decoder and separate pure-catalog behavior. No source/test behavior has been implemented or qualified.

Snapshot matching now explicitly includes original root/fact record IDs even with malformed/foreign metadata and retains every selected head. Pre-validation rejects selected tombstones, duplicate/conflicting heads and unsupported/schema-two envelopes before inspect_snapshot can skip tombstones. Original fact-to-turn membership does not require outcome equality to a later turn. Success serialization has an explicit1024-byte UTF-8 bound and all-branch test requirement. The original866fd2b precode/review evidence remains preserved in history.
