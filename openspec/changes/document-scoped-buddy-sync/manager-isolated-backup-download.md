# Selected isolated backup download

This continues the existing [reader](manager-isolated-backup-reader.md) and V1
package contract. Reuse the publisher's content addresses, Buddy's complete
package validator, protected Drive authority, and existing restore/preferences
import. Do not add a second backup format, login store or restore engine.

## Original selection and bounded reconstruction

The private coordinator receives the original host operation/selection, a
callback that revalidates that exact selection, its original invalidation signal,
and the same captured protected read binding. It must not obtain a replacement
grant or advance to a newer marker. Selection expiry, rescan, cancellation,
authority change and disposal invalidate pending reads and staged results. The
first increment finishes within the remaining two-minute selection lifetime;
it creates no extended child lease, retry or automatic resume.

The trusted binding adds only fixed object lookup, exact object metadata and
bounded object streaming. Lookup projects the existing `buddy_isolated`, `kind`,
`root`, `backup` and `sha256` properties in appData. Complete bounded pagination,
reject repeated tokens and ambiguous/missing candidates, and recheck the one
exact candidate's ID, original properties, size, MIME type and non-trashed state
before streaming. No caller-supplied endpoint, path, token or arbitrary request
option enters this interface. Check original authority around every asynchronous
read and while consuming streams, not just when the factory is captured.

Read and hash `data/backup.json` first. Its inventory extractor is only a bounded
way to discover the ordinary V1 producer's exact content-addressed closure; it
is not another semantic backup validator. Refuse selected/feedback formats,
unexpected fields, configuration snapshots, duplicate object digests, invalid
lengths and oversized collections before admitting object reads. Preserve the
existing 8 MiB data-manifest, 128 KiB preferences, 16 KiB marker, 4,096 manifest/
object-count and 256 MiB per-object limits; ordinary content objects may be empty.

One desktop attempt additionally allows at most 512 MiB of total staged bytes,
64 MiB of metadata responses, and 16,384 binding calls. Count before admission;
one deadline is never renewed by pagination or progress. These are desktop
operational limits, not a new package format. Refuse an oversized inventory
before its content downloads. Check free space before creating staging and
against the known remaining closure before further files, retaining at least
256 MiB free. Missing disk/authority information refuses safely. The stream is
bounded before buffering/writing, hashes the original bytes through EOF, and
refuses short, overlong, substituted or interrupted content.

## Owned private staging

Use one exclusively created private directory under the host's designated
canonical staging parent, outside credential, Store, checkout and user-document
roots. Reuse existing protected filesystem and stream/identity utilities where
appropriate; Windows privacy requires the existing protected ACL checks, not
POSIX mode bits alone. A trusted constructor may inject a qualified staging
factory for fixtures; absent/unqualified staging or verifier support reports
unavailable before provider download, with no renderer-controlled filesystem.

Create only `data/backup.json`, `data/objects/<sha256>`,
`portable-configuration.json` and the exact retained `isolated-backup.json`.
Use exclusive file creation, safe canonical membership and original file/directory
identity checks. Write the outer marker last. No unknown file may appear in the
completed package. A valid hash inventory alone is not a verified package.

Cancellation stops and joins reads and the verifier before teardown. Delete only
this attempt's identity-verified owned files/directories. If identity changed or
cleanup failed, preserve the unknown residue and report that condition; never
scavenge other attempts or follow replacement paths. Successful staging has one
explicit owner and remains usable only while the original selection is current.
It is released after its handoff, expiry, cancellation or disposal, not retained
as an indefinite cache. Public output has no credentials, provider IDs, staging
paths, raw settings or personal content.

## Reuse the complete Buddy oracle

Expose `Store::inspect_isolated_package(root, Some(original_marker_sha256))`
through the existing bounded offline archive command family as
`--archive-operation inspect-isolated --archive-input -`. Its closed input is
`{"path":"<absolute package directory>","marker_sha256":"<original sha256>"}`.
Reuse the existing input/output byte caps, strict JSON and redacted failures.
No Store creation, mode switch, credentials, provider call, tablet API, restore
or runtime activation is permitted. Existing archive command inputs and output
shapes remain unchanged. The new operation's successful data contains only
`isolated_package`, the existing redacted `PackageInspection`; errors expose no
raw paths or settings. A failed check cannot issue a success receipt.

The Manager's trusted verifier seam consumes that original package root/digest,
honors cancellation/deadline and checks exact bounded output and verifier
provenance. No available trusted verifier means unavailable, not verified. A
fixture-injected verifier must be labeled synthetic until exercised against a
retained real producer package and this actual Buddy command. This increment
does not claim that existing Windows/Linux Manager distributions already ship
a compatible host Buddy executable; host packaging/runner qualification remains
an explicit delivery task, or verification occurs in a separately qualified
target path before restore. Do not add an unreviewed download/execute helper.

Only complete oracle success for the original marker can yield a private verified
stage handoff. The later wired transfer must preserve and recheck that same
closure/digest before feeding its `data/` child to existing ordinary Prepare.
Portable preferences use the existing explicit import and separate confirmation.
Clean/replacement target admission and actual provider namespace visibility
remain their existing separate obligations. No reconstruction result applies
data or grants native authority.

## Implementation and verification

Native owns the private Manager coordinator and focused offline fixtures. Root
owns protected-host integration, UI, staging/verifier qualification, Docs, CI and
delivery. SCRAPPY owns the narrow Buddy oracle command and actual-producer
command tests, using the existing relevant source branch/cache. Review this
contract before coding; report contradictions without widening other scopes.

Test complete healthy closure, zero-byte objects, incomplete/duplicate lookup,
wrong size/hash/EOF, changed authority/selection during a read, original expiry,
disk/aggregate/call exhaustion, unavailable or failed verifier, exact redacted
success, and cleanup refusal after identity replacement. Exercise the real
Buddy oracle with an actual exported ordinary isolated package, corruption,
extra membership and wrong-marker refusal. No local app build or new Cargo
cache is required; keep platform/runtime/source evidence distinct.
