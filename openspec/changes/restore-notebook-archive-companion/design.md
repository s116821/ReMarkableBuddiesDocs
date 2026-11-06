# Design

## Source boundary and reuse

Base Manager5b05888 and Docs3946800. Existing `OrdinaryRestoreHost`, public/private
restore parsers, controller and `ordinary_restore_transport.py` already implement
the required finite lifecycle. Extend their internal routing with a closed,
constructor-selected family; do not copy that state machine or create a new
maintenance framework. Existing exports/default construction remain strictly
legacy. Notebook construction is explicit and immutable for that instance.

| Selected capability | Prepare / apply / status | Request and report version |
| --- | --- | --- |
| Existing ordinary restore | `prepare` / `apply` / `status` | 1 |
| New notebook restore | `prepare-notebook` / `apply-notebook` / `status-notebook` | 2 |

The browser helper and Electron expose a separate fixed `notebookRestore`
capability with the existing safe request shape. Each family has its own private
host instance/reference inventory and shares the existing `MaintenanceIO` owner
with every other maintenance operation. The shared wired helper accepts only the
six fixed selectors above. No selector, command or family is inferred from a
filename, archive bytes, returned version or caller-provided command text.

## Exact producer correspondence

Prepare sends `{restore_version:2, operation:NEW_UUID, source:PRIVATE_PATH}` to
`prepare-notebook`. Apply and Status send the original source and complete original
fourteen-field intent to their matching notebook selector. Preserve all intent
fields, actor, base/target generations and fingerprints exactly. Version is checked
against the selected family on admission and every retained reuse; it is never
converted. Notebook fingerprints bind effective actor/features inside the
producer; Manager treats them as opaque digests.

The producer deliberately retains the existing path-fingerprint domains
`urn:remarkable-buddies:ordinary-restore-{kind}-path:v1:` for both families.
Use those actual domains, not invented version2 path domains. Keep the exact
configured protected path and current lexical source binding.

Notebook responses must be report_version2 with the exact requested notebook
operation, complete successful transport/exit and existing closed field/outcome
schema. Legacy parsers continue to refuse version2 and notebook selectors;
notebook parsers refuse version1 and legacy selectors. No fallback dispatch is
permitted. A producer that lacks the new command yields unsupported/unavailable,
not legacy restore or empty success.

Notebook-positive frames require `complete_media:true` in both source and target
preview summaries, the original intent and every positive observed inspection.
The notebook producer requires complete closures. A consistently false set of
fields is therefore not a valid notebook preview/result even when its hashes,
version and selectors agree. Keep valid legacy incomplete-media cases unchanged;
enforce this additional condition only in the fixed notebook family. Successful
Apply has `disk_readback_verified:true`; successful Status observation retains
false, as specified by the producer.

## Shared safe view and independent custody

The existing safe `ordinary_restore` view shape can represent either ordinary
storage family without changing its private data exclusions. Retain that wire
field and the existing request actions (`prepare`, `confirm`, `status`, `cancel`,
`retained`) to reuse parsing/presentation; the selected API/host/controller fixes
the family. The visible report retains the actual producer operation string.
Public result parsing selects the expected family from the caller's capability,
never from the response. Do not normalize a notebook operation into a legacy one.

Original sources, configuration fingerprints, full intents and packets stay
host-private in bounded process memory. No new persistence or renderer exposure.
References issued by one family cannot be redeemed through the other. Preserve
the existing two-minute preview, thirty-minute nonrenewing retained intent,
eight-slot/thirty-two-invocation bounds and complete input/output limits. A new
notebook host does not bypass shared I/O ownership, observation quiescence,
captured-invocation cancellation, disconnect or disposal.

Success means the producer reported desired data readback. Preserve unknown and
not-activated original outcomes. A later Status observation is not retroactive
confirmation, retry permission, rollback or runtime activation. No second Apply,
automatic reprepare, source substitution, stage removal or settings activation.

## UI

Add a clearly named notebook restore section adjacent to notebook archive tools,
using the shared restore controller/presentation behavior. State that the archive
must already be on this tablet and belong to the same existing local notebook
store/actor. Enter path, preview, review and separately confirm. Clear the actual
path input on submission. Offer earlier-attempt checks with the existing honest
uncertainty wording. Keep legacy restore as its existing explicit capability.
Technical versions/counts belong in optional details, not the primary flow.

Both browser/local-helper and Electron use the same Angular surface and narrowly
validated bridge DTOs. Integrate observation pause, all-maintenance exclusion,
cancel/dispose and retained-state restoration at every existing application
boundary; do not merely add a button that bypasses those boundaries.

## Verification and delivery

Before implementation, independently review this finite contract against actual
Buddy version2 and current Manager lifecycle code. Focused controls exercise real
parsers/host/controller/helper code, original packet byte retention, family/version/
selector mismatch, cross-host reference refusal, ownership contention,
pre-dispatch cancellation, uncertain apply then status, expiry and teardown.
Include negative notebook incomplete-media frames paired with accepted legacy
incomplete-media controls, and the Apply/Status readback-flag distinction.
Preserve the existing legacy vectors and meaningful regression tests.

Use literal notebook reports derived from the producer contract, explicitly marked
synthetic where no real producer ran. Browser and Electron tests must exercise the
actual app/bridge surface, observation quiescence and interoperation with existing
maintenance lanes. Current source review, CI, source fixtures and visual evidence
are distinct from actual tablet/native qualification. No tablet step follows from
this change. Synchronize and archive only the implemented/verified consumer in the
paired Manager/Docs delivery, retaining broader roadmap gates.
