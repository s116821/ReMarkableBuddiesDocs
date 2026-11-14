# Disconnected isolated backup inspection

This increment implements the existing Manager requirement to inspect and select
Buddy-owned backups without a connected tablet. It consumes the ordinary V1
[isolated publisher](isolated-backup-publication.md), its existing root/object/
marker properties and `isolated-backup.json`; it creates no new publisher,
catalog, backup format, provider protocol or synchronization engine.

## Existing authority

Manager sign-in uses the existing protected `DriveAuth`/`DriveStore` registration,
grant, token refresh and account checks. Its public authorization ID remains an
opaque revocation reference and `backupReady:false` remains unchanged. A signed-in
account, matching account label, or tablet root-preparation report is insufficient
to establish access to the tablet application's hidden backup namespace.

A privileged host factory must supply a separately qualified read-only binding
for the actual Manager registration/account/grant and publisher namespace. The
current production binding remains unavailable until that visibility is proved.
Fixture injection is constructor-only, with no renderer input for eligibility,
tokens, endpoints, provider IDs, grant digests or paths. Root's publisher-grant
property is preserved as private metadata; it is not assumed to equal Manager's
separately issued grant digest. The binding checks current protected authority
before and after asynchronous reads. Grant replacement, disconnect, revocation,
expiry or host disposal invalidates existing inspection and selection handles.

## Read-only reader

Use one private reader with a narrow injected binding for root/marker metadata
listing, exact-ID metadata readback and bounded raw marker download. The binding
provides cancellation and authority-currentness checks. It supplies no create,
upload, delete, arbitrary request, secret export or tablet operation.

Validate the producer's exact V1 property shapes, canonical non-nil UUIDs, bounded
provider IDs, lowercase SHA-256 strings and non-trashed objects. Root metadata
must identify itself and its original backup/device/grant. Marker metadata must
identify that root/backup and an original predecessor. Names, modification times,
listing order and wall clocks are never ancestry. Complete the relevant listing
before treating a predecessor as having no successor; duplicate IDs, repeated
page tokens, ambiguous children, cycles, disconnected markers or malformed
properties prevent a coherent revision list. Unreadable, unqualified, incomplete
and qualified-empty remain distinct states.

Keep the publisher's maximum of 100 entries per listing page and 4,096 total
entries as outer supported limits. Each user-requested scan has one 60-second
deadline, at most 128 binding calls and 8 MiB of total metadata/raw marker bytes.
Charge before accepting work and never renew a window on pagination or retry.
Exhaustion reports an incomplete scan without selectable partial results.
The binding enforces bounded responses before returning them to the reader.
Do not fetch every historical package to list revisions: validated listing
metadata establishes the observed predecessor chain; raw marker validation is
required when the user explicitly selects one revision.

Selection retains an opaque host-issued handle tied to the inspection generation,
binding, exact root, marker ID and raw digest, with a two-minute maximum lifetime.
Before issuing it, recheck the exact root and selected marker metadata, download
at most 16 KiB of marker bytes, verify raw size/hash and parse duplicate-free
strict JSON with exactly `isolated_backup_version:1`, `data_backup` and
`portable_configuration`. Each reference has only `bytes` and `sha256`; lengths
are positive safe integers bounded by the existing 8 MiB data-manifest and
128 KiB portable-configuration limits. No JSON reserialization substitutes for
the original raw marker digest. Preserve exact marker bytes privately for the
later download handoff. Cancellation, timeout or changed metadata/authority
cannot issue or retain a usable selection. A new scan replaces the old view and
selection; no automatic retry follows a refusal.

The reduced view may show backup/device identifiers, revision digests and their
observed ancestry. It must call the chain tip the newest observed revision, not
a permanent current head. A selection verifies marker metadata and raw marker
bytes only. It does not establish archive/media completeness, restore eligibility,
portable settings validity, runtime health or native-page authority. A later
append can leave a deliberately selected historical revision valid; it must not
silently switch the user's selection to that newer revision.

## Following connected work

The shared browser/Electron UI will use the same private reader through narrow
host requests and reduced results. Root owns the existing auth read seam and
host wiring. A reviewed offline reader does not enable live Drive requests.
Use the maintained OAuth client for the eventual fixed read-only API adapter;
do not implement another login/token store or expose provider request options.

Download must separately fetch the pinned closure into owned private staging and
use the existing `Store::inspect_isolated_package` validation before offering
restore. Reuse the existing ordinary data restore and explicit portable import
flows. Clean/replacement target admission, wired transfer and readback remain
their own implementation work; selecting a marker does not bootstrap a Store,
switch modes, apply data, reinstall credentials or recreate native pages.

## Verification and ownership

Native owns the private reader and focused tests in Manager; Root owns this
canonical contract, auth/host/UI integration, publication and delivery. SCRAPPY's
notebook publication correction is disjoint. Reuse retained producer-emitted
fixtures where available. Label source-derived synthetic frames honestly; do not
claim cross-language byte acceptance without a retained producer receipt or
comparison through the existing Buddy package oracle.

Cover multiple pages, changed authority during a read, qualified empty versus
unqualified/unreadable, cancellation/expiry, repeated tokens/IDs, corrupt or
ambiguous predecessor chains, exact/oversized/duplicate-key markers, substituted
root/marker metadata, original raw digest preservation and stale selections.
Healthy controls must demonstrate disconnected inspection and explicit selection
without provider writes, package-completeness claims or tablet contact. Record
source/fixture, distribution, actual-provider and wired evidence separately.
