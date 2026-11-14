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

Protected record checks must leave cancellation responsive and fit the same
remaining lifetime. Do not launch a synchronous credential-helper process for
each stream chunk. Reuse one bounded read-only guard for the original protected
record digests, with asynchronous checks around reads and accepted chunks,
including admission before stage creation and completion. In-memory generation,
expiry and exact-selection predicates must not repeatedly copy marker bytes.
A file watcher alone does not replace authoritative protected-record checks.
Guard failure invalidates the original capture; it cannot silently restart.

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

If a staging child fails after creation but before returning custody, report
uncertain cleanup even though the coordinator has no stage object. A joined
process exit alone is not proof of rollback; retain the warning unless explicit
owned cleanup succeeded. Do not retry deletion or adopt a new process's residue.

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

A successful run of the full existing oracle for the original marker can yield
a private verified stage handoff. Declared media omissions retain the oracle's
`complete_media=false` and `incomplete=true`; verified package structure never
means all media is present or that a restore has been applied. The later wired
transfer must preserve and recheck that same
closure/digest before feeding its `data/` child to existing ordinary Prepare.
Portable preferences use the existing explicit import and separate confirmation.
Clean/replacement target admission and actual provider namespace visibility
remain their existing separate obligations. No reconstruction result applies
data or grants native authority.

## Implementation and verification

### Host oracle delivery decision

Use the existing normal `reader-buddy` command as a pinned, offline host
dependency of Manager. Its Windows x64 and Linux x64 builds belong inside
Manager's existing private host resources, not Buddy's tablet release asset
inventory. Do not add another binary target, parser, backup format, release
channel or runtime download-and-execute path.

The initial dependency source is reviewed Buddy commit
`958cacf2810f501dc3cb23b525481f0bedf706f2`, tree
`08612c77637d83388c88e20a4080b3a9d469c764`, with Cargo.lock SHA-256
`dd6ddeeb756da0a93c8e3d7020d2f7e92ba68026a1492d2312da1ad94b2472d1`
over the exact Git blob bytes, independent of checkout line-ending conversion.
This is a development dependency pin, not a published Buddy release or a new
application version. Use Buddy's existing Git-derived identity without Manager
version substitution. A later pin change requires review and fresh applicable
qualification; it must not silently follow a branch or a latest release.

Initial native qualification runs within the existing two platform Integration
jobs on PRs, preserving the five-job Manager budget. It builds the new dependency
for that qualification only; it does not rebuild or replace retained Manager
ZIPs, repeat Manager's common source checks, or enable a release path. The final
shipping assembly must also respect the existing pipeline contract before
production use; qualification artifacts alone are not installed dependencies.

Keep the pin in one Manager host-owned source record. CI checks out that exact
Buddy source separately, builds `--locked --release --bin reader-buddy` with
default features and no native experiment flags on each native host, and tests
the normal archive command. Reuse maintained checkout/toolchain/artifact
actions and put orchestration in the existing workflow. Record source/tree,
lockfile, resolved SDK revision, target, toolchain, feature/profile settings,
Git-derived identity, executable size/hash and matching notices with the
retained artifact. Source and native platform claims remain distinct.

Only the matching qualified executable and bounded provenance enter
`host/buddy-oracle/` in Manager's private resources. Preserve its Linux execute
bit through ZIP assembly. Verify the embedded source/target/hash and original
Manager package digests without executing downloaded ZIP contents. Keep the
existing three Manager ZIP names and size limits; measure before proposing any
limit change. Source-tree helper mode and browser use must resolve the same
qualified installed host dependency through the existing local helper contract.
A static browser ZIP alone does not supply a native verifier.

The verifier adapter is disabled by default. Its trusted host constructor may
select the resource directory and expected dependency pin; a renderer, user
setting, provider object or staged package may not select an executable. Before
and after each invocation, validate the original canonical regular executable,
its expected size/hash/target/source and bounded metadata. Refuse missing,
changed, unqualified or mismatched inputs. Never search PATH, install, recapture,
refresh, or fall back to a tablet binary.

Run only `--archive-operation inspect-isolated --archive-input -`, with the
original root/digest on bounded stdin, shell disabled, hidden Windows console,
a private working directory and a minimal environment without credentials,
configuration or loader overrides. Bound stdout to the existing 16 KiB report,
refuse stderr and nonzero/ambiguous exit, honor the original remaining deadline
and cancellation, and join the child before settling or releasing staging.
Process fixtures may test these mechanics but are not Rust-oracle evidence.
The coordinator continues to validate exact report semantics and original
selection authority; the runner must not become another package parser.

Before wiring download, independently verify native Windows compilation and
normal command behavior, the supported Linux runtime baseline, actual retained
package bytes/modes and both browser-helper and Electron paths. Exercise the
runner against an actual isolated-producer package as well as malformed output,
wrong dependency, cancellation and timeout controls. Keep platform and provider
qualification incomplete until their own evidence exists.

Native owns the private Manager coordinator, staging/read-guard adapters and
their focused offline fixtures. Root owns protected-host integration, UI,
independent staging/verifier qualification, Docs, CI and delivery. SCRAPPY owns
the narrow Buddy oracle command and actual-producer
command tests, using the existing relevant source branch/cache. Review this
contract before coding; report contradictions without widening other scopes.

Test complete healthy closure, zero-byte objects, incomplete/duplicate lookup,
wrong size/hash/EOF, changed authority/selection during a read, original expiry,
disk/aggregate/call exhaustion, unavailable or failed verifier, exact redacted
success, and cleanup refusal after identity replacement. Exercise the real
Buddy oracle with an actual exported ordinary isolated package, corruption,
extra membership and wrong-marker refusal. No local app build or new Cargo
cache is required; keep platform/runtime/source evidence distinct.
