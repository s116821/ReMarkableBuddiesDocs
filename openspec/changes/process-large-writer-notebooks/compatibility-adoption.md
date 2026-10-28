# Accepted allocations and shared-path handoff gate

This is unimplemented precode. Source3 is reserved only for
ArchivedNormalizedSource; Conversation3 only for NotebookPlan/NotebookStage.
Generic envelopes stay format1. Feedback storage generation3 contains its own
namespace/schema1 and is not notebook adoption. Contract-v1.json and
contract-v2.json remain immutable. Accepted allocations are:

| Axis | Reserved value and scope |
| --- | --- |
| Source payload | Schema3 only ArchivedNormalizedSource, record_kind archived-normalized-source, Kind::Value |
| Conversation payload | Schema3 only NotebookPlan / NotebookStage, record_kind notebook-plan / notebook-stage, Kind::Value |
| Current generation | Format4, explicit in-place adoption, unchanged generation UUID/CURRENT |
| Whole backup | Format4, ordinary same-actor notebook archive only |
| Offline contract | Version3 / contract-v3.json; envelope schema ID urn:remarkable-buddies:envelope:contract-v3 |
| Notebook descriptor | notebook-feature.json format1, bound to actor and generation |

Other domain versions and envelope/manifest/actor format1 retain their meaning.
These numeric axes are independent. Complete amended-contract review remains
required before notebook source work. Intended single-writer ownership is
accepted, but overlapping shared paths remain closed until the native owner
acknowledges an exact handoff revision and preservation of unfinished work.

Main owns notebook-only modules src/writer/notebook.rs,
src/conversation/notebook.rs, src/storage/notebook_generation.rs and the new
contract-v3.json, notebook tests and Writer host integration. Only during an
explicit handoff window does Main become sole writer of conversation
mod/types/selected/receiving/cleanup and storage
mod/types/selection/recovery/inspection/feedback_generation/conversation_cleanup,
including required sync refusal guards. Shared main/simulator dispatch edits also
require that window. Native retains workflow/resident/bootstrap/SDK and
conversation evidence/evidence_tests/historical_association/pending. Root
coordinates rather than becoming a second concurrent source writer.

# Explicit in-place adoption

Use a deliberately prepared unsupported generation format while preserving the
current generation UUID, CURRENT bytes, immutable commits/envelopes/receipts,
object/media files and existing feature identity bindings. Do not copy retained
media solely to change the format. A new unknown marker alone cannot fence an
old binary; the unsupported format replacement is the fencing point. Notebook
domain3 must never be committed under legacy formats1/2 or feedback-only format3.

Preparation owns a fresh mutable Store and exclusive stable-inode OS lease before
Arc clients escape. The process lease does not exclude clones of the same Store.
Refuse active Writer/export/publisher/domain/sync/mode handles, selected/sync mode,
unavailable history, unresolved external effects and foreign or malformed
preparation metadata. Ordinary open never adopts. No service/device operation is
authorized by this preparation contract.

1. Validate actor/current generation and the complete immutable retained history,
   media and feature closure under exclusive custody.
2. Durably publish a notebook-specific actor/generation-bound preparation
   notebook-feature.json descriptor and immutable contract-v3.json. Keep the legacy
   capabilities advertisement while format is old. Do not alter feedback's
   marker, contracts1/2, CURRENT, commits or media. Pending metadata has no
   notebook publication or external-effect authority.
3. Revalidate current identity, heads, retained closure and required features;
   atomically replace format.json with reserved unsupported discriminator4.
   No notebook records may exist before this commit. A failed return value does
   not establish that the rename failed or that the old discriminator remains.
4. Publish/read back successor capabilities bound to actor/generation and exact
   required features, immutable contract revision and namespace/kind/schema
   combinations. Verify the complete format/descriptor/contract/advertisement
   closure before exposing clients that can publish notebook data or incur
   provider/export effects. No capability file alone upgrades a generation.
5. On error or lost acknowledgment, stop without provider/export work. Only
   explicit preparation under newly acquired unique custody may resume after
   reading actual state and revalidating current data. Ordinary open refuses
   incomplete adoption without repair or capability rewrite. Never downgrade
   format or CURRENT automatically.

# Interruption and predecessor behavior

| Boundary | Required behavior |
| --- | --- |
| Before format commit | Old format remains authoritative, no notebook data/effects; new ordinary open refuses recognized pending preparation |
| Pending descriptor, old binary opens later | Old code may ignore the unknown descriptor and write legacy history; explicit resume must revalidate rather than trust stale closure hashes |
| Partial atomic file publication | Read actual complete file or refuse malformed/missing state; no inference from an unsuccessful acknowledgment |
| Format rename or parent-sync error | Treat commit acknowledgment as uncertain; read actual format on explicit resume, never assume rollback |
| New format, missing/stale capability metadata | Older writers refuse unsupported format; new ordinary open refuses; explicit preparation verifies/rebuilds the advertisement before clients/effects |
| Complete adoption, lost return acknowledgment | Deliberate preparation retry may revalidate; it never replays a paid notebook operation |
| Notebook history exists | No downgrade or automatic rollback; preserve all bytes and use supported successor recovery |

The existing atomic helper syncs a temporary file, renames and syncs its parent
on Unix. Its non-Unix directory-sync branch does not establish Windows power-loss
durability. Qualify supported platform/filesystem durability explicitly; source
inspection is not such qualification.

Actual predecessor normal writer, sync/outbox, import/restore, recovery, archive,
cleanup and maintenance entrypoints must reject the unsupported current format
before history recovery/publication or capability rewrite. Supported open paths
can touch auxiliary directories before format refusal; this is not a guarantee
of zero filesystem metadata changes or prevention of unrelated config writes.
Read-only inspection reports unsupported without claiming complete history.
A predecessor bypass blocks adoption for either copying or in-place approaches.
Arbitrary manual filesystem edits are outside this supported-entrypoint guarantee.

# Feedback, consumers and archives

Keep feedback's original marker and immutable payload1 semantics. Its current
validator requires format3 except within its own preparation path. Add a reviewed
successor-aware composition branch for unchanged retained feedback features;
never globally relax allow_pending or conflate feedback preparation with notebook
adoption. Existing generation3/backup3 retains its exact meaning.

Narrow native receiving and conversation cleanup refuse relevant notebook data
before effects, without silently dropping records/media. Historical projection
retains original user-turn linkage and archive JSON descriptors; it grants no
native document ownership. Current native Source1 and Conversation2 remain
unchanged. Sync/selected/group and cross-actor import of notebook-bearing data
refuse before remote publication or local mutation in this increment; namespace
filtering is not permission to publish an incomplete notebook history.

Whole ordinary same-actor backup/restore requires reserved archive format4 and an
explicit supported entrypoint. Preserve every retained
envelope/media byte, feature binding, conflict/tombstone and receipt identity.
Never import notebook domain3 into legacy formats or reuse feedback backup3.
Restore may require staged copying for its additive semantics; that does not make
copying necessary for format adoption. Retain uncertain evidence and refuse any
lineage that cannot be preserved without rewriting immutable facts.

Generic owned-data inspection may retain existing truthful unsupported/null for
generation4 under unchanged report1/report2 during this increment. Do not widen
report2's generation enum1..3 or claim complete generation4 accounting. Dedicated
notebook Ledger/history and whole-backup paths must traverse real retained
records/media rather than return fabricated empty success. Complete generation4
category/media accounting and companion handling remain required 1.0 integration
under data management and final readiness (REM42/REM35); interim refusal does not
remove that dependency.

# Why adoption preserves identity

Feedback preparation already uses a fresh Store before Arc escape and an
in-place marker/format/capability sequence. Conditional operations check current
generation identity; retaining it avoids unnecessary feature/replay rebinding.
Additive restore copies objects and switches CURRENT for a different purpose.
Copying retained media adds proportional I/O/peak space and does not make root
capabilities.json and CURRENT one transaction. Both designs need exclusive
custody, stale-snapshot revalidation and the same unsupported format gate.

Source basis: inspected storage/mod.rs, selection.rs, feedback_generation.rs,
files.rs, maintenance.rs, conditional.rs and recovery.rs plus public maintenance
entrypoints at the pinned source in design.md. These are design evidence, not
new tests or predecessor execution. Existing test definitions were read, not
rerun as notebook qualification.
