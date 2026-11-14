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
`4192914db255ce9e0c61ed0a0de48b7d9c838302`, tree
`7a893016a7c92ac26bec69b57102433af2e519d5`, with Cargo.lock SHA-256
`dd6ddeeb756da0a93c8e3d7020d2f7e92ba68026a1492d2312da1ad94b2472d1`
over the exact Git blob bytes, independent of checkout line-ending conversion.
This is a development dependency pin, not a published Buddy release or a new
application version. Use Buddy's existing Git-derived identity without Manager
version substitution. A later pin change requires review and fresh applicable
qualification; it must not silently follow a branch or a latest release.

This pin includes the reviewed test-only retained-command selector. Copy the
ordinary executable before compiling tests, bind its exact canonical path, size
and SHA-256 through the all-or-none `READER_BUDDY_ARCHIVE_TEST_COMMAND`,
`READER_BUDDY_ARCHIVE_TEST_BYTES` and `READER_BUDDY_ARCHIVE_TEST_SHA256` variables,
and recheck those same retained bytes after the tests. This avoids accidentally
qualifying a replacement binary compiled with test-only dependency features.
The Windows path uses Rust's canonical verbatim form. The selector's local
Cargo-built test proves the harness only; native retained-release results remain
required. Production code, Cargo.lock and the SDK revision are unchanged by this
test-only successor.

The initial, temporary qualification path builds the dependency within the two
existing platform Integration jobs on PRs. It does not rebuild retained Manager
ZIPs or enable a release path. The final shipping path below replaces that
temporary compilation; qualification artifacts alone are not installed dependencies.

Keep the pin in one Manager host-owned source record. CI checks out that exact
Buddy source separately, builds `--locked --release --bin reader-buddy` with
default features and no native experiment flags for each supported host, and tests
the normal archive command on the native platform. Reuse maintained checkout/toolchain/artifact
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

### Shipping build and native qualification

The final shipping path compiles both dependencies in Manager's existing Build
job. Use Ubuntu 22.04 as the initial tested Linux baseline, Rust 1.98.1 and the
normal default-feature release command. Cross-compile Windows x64 with maintained
cargo-xwin 0.23.1, LLVM/clang-cl 22.1.8, signed Jammy NASM 2.15.05-1, desktop SDK
10.0.26100 and CRT selector 14.44.17.14. Record the actual resolved SDK/CRT inputs
and compiler versions. These selectors and the initial runner are qualification
inputs, not a claim of immutable upstream catalogs or universal Linux support.

Keep Windows CRT linkage static and AWS-LC bundled-source/static with assembly
enabled and prebuilt NASM fallback disabled. Remove global Rust flag overrides
before applying target-specific flags. Preserve the locked dependency graph,
original source identity and normal features. Use pinned maintained setup actions
and workflow orchestration; do not add a custom SDK downloader, new release asset
or executable target. Record native PE imports, ELF dependencies/symbol versions
and matching license/third-party notices. A working compiler alone does not
establish runtime compatibility or notice completeness.

Copy and hash each normal executable before compiling `archive_cli --no-run`.
Use Cargo's root-artifact and build-script JSON records for the original
`READER_BUDDY_VERSION`; do not run Windows code on Linux, substitute Manager's
version or duplicate Buddy's version algorithm. Retain the test executables and
build receipts as CI-only inputs outside the three release ZIPs. Both native
Integration jobs execute those tests against the same oracle bytes extracted
from their retained Manager package, using the existing all-or-none selector.
The pinned Linux test also reads two scenario files beneath its compile-time
`CARGO_MANIFEST_DIR`. Retain their original source bytes and digests, verify that
the recorded path is the exact assigned checkout path, and restore only those
two fixtures there before testing. Refuse a changed path or fixture; do not omit
the test or silently substitute a different source tree.

Compare actual native `--version`, original provenance and command hashes, then
recheck the command and ZIPs after testing. Do not rebuild or repack in Integration.

Preserve the five existing PR jobs, required status contexts and common-check
placement. The Linux Integration runner uses the initial Build baseline even if
its status-context label is retained for repository compatibility. Keep generated
targets on disposable hosted runners, check free space before compiling, and
retain only the bounded original inputs needed for qualification and delivery.

Generate target/default-feature third-party notice JSON with maintained
cargo-about, locked dependencies and failure on unresolved licenses. Keep its
default exclusion of local source and carry Buddy's exact root LICENSE and
THIRD_PARTY_NOTICES separately; do not fabricate a root SPDX declaration. Include
the locked foreign SDK and its notices, all runtime transitive dependencies and
matching Rust standard-library and native-library notices. Do not blanket-ignore
unpublished foreign dependencies. Cargo's graph does not account for statically
linked Microsoft CRT/UCRT objects; retain their resolved input and notice basis
separately before distribution.

### Package readback and compatibility

Extend the existing bounded Manager ZIP observer for embedded dependency checks;
do not extract or execute an archive, add an asset, or introduce a second ZIP
parser. Native ZIPs that carry an oracle contain exactly its platform executable
and provenance in `resources/host/buddy-oracle/`, plus the adjacent host-owned
source record. Require that record and provenance to agree, validate the existing
runtime schema and platform, and stream the declared executable to verify its
exact size, CRC and SHA-256. Preserve current archive, metadata and time limits.
Require regular 0755 for the Linux command and regular 0644 for the Windows
command and JSON. Refuse partial pairs, extra members and target-platform aliases
or collisions into these fixed resources. The static browser ZIP has no oracle.

Runtime download verification checks the downloaded release's own internally
consistent pin, not the currently installed Manager's older pin. Both native
ZIPs must agree on their source record. Existing annotated-tag, completion-record
and asset-digest checks bind the candidate bytes; embedded metadata alone is not
independent build provenance or update authorization. Keep the existing fixed
quarantine response and its lack of installation eligibility.

The runtime compatibility boundary is Manager **1.0.0**: earlier versions may
omit both native oracles, but any present oracle must be complete and both native
ZIPs must carry it. At and after 1.0.0, both are required. The adjacent source
record is not a rollout marker because pre-oracle packages already contain it.
This feature boundary does not create a tag, change version authority, or remove
the existing premature-1.0 release hold.

Shipping CI is stricter at every candidate version: before upload it requires
both native oracles, compares their source to the exact candidate checkout pin,
and checks each against the original retained executable/provenance supplied by
Build. Reuse the bounded observation core for candidate readback and publication.
Runtime verification of a future release must still accept a different valid
embedded pin. Neither a trusted CI expectation nor an executable path may come
from the renderer or downloaded package.

### Installed host verifier

Provide an explicit value-free `--browser-helper` mode in the existing packaged
Manager executable. It starts the existing fixed-loopback helper with browser UI
assets from `app.getAppPath()/dist/manager/browser`, before creating a desktop
window or registering desktop IPC. Host modules and native resources still come
from the same installed external resources used by normal Electron mode; only
static UI reads use ASAR. Do not add an executable, release asset, chosen port or
path, or runtime code download. Source-only browser helper mode does not acquire
installed-dependency authority from a lookalike directory.

Normal explicit launches open only the helper's own returned loopback preview
URL in the user's browser and expose that URL for attached terminals. A trusted
host test seam may suppress external-browser launch without granting any path,
credential or verifier choice. Startup failures produce no success URL and must
not fall through to desktop startup. Normal desktop behavior remains intact.
Windowless Linux use still needs the supported Electron desktop environment;
it does not imply display-server-free operation.

Use one idempotent awaited shutdown on signals and explicit quit. Stop admitting
HTTP requests, invalidate pending owners, close the helper and finish owned
cleanup before ordinary process exit. When the download coordinator is later
composed, shutdown must await its existing child join and checked stage disposal.
Browser page-close signaling is best effort and does not replace host expiry or
authority checks. Forced process termination cannot prove cleanup or authorize
scavenging. Extend the existing packaged host tests to launch this actual mode
and verify its ASAR UI, loopback/session checks, lack of desktop windows, ordinary
shutdown and truthful unconfigured/unqualified results. The launch mode alone
does not activate backup download, restore or the installed oracle factory.

The verifier adapter is disabled by default. Its trusted host constructor may
select the resource directory and expected dependency pin; a renderer, user
setting, provider object or staged package may not select an executable. Before
and after each invocation, validate the original canonical regular executable,
its expected size/hash/target/source and bounded metadata. Refuse missing,
changed, unqualified or mismatched inputs. Never search PATH, install, recapture,
refresh, or fall back to a tablet binary.

On Windows, acquire a narrow resource lock helper before the first Node resource
capture, including availability checks. Use the existing trusted host Python and
pywin32 boundary. The helper accepts only the trusted canonical local resource
root and derives the two fixed file names; it never receives a command, arguments
or backup input. Reuse the existing handle checks through a small shared primitive
without changing staging or Drive behavior. Reject every reparse component,
alternate stream, alias, nonlocal path and nonsingle-link leaf. Hold a
share-accounted handle on each ancestor without delete sharing, and hold each
leaf with generic read access and read sharing only. Compare held and path file
identities before readiness and final confirmation. Directory share modes alone
do not protect arbitrary children.

Node retains the original fixed launch and all provenance, membership and hash
checks. Monitor the helper throughout the same bounded operation. Stop and join
the Buddy child before releasing helper handles on failure, cancellation or
timeout; after success, finish the original checks while handles remain held,
then release and join the helper before accepting output. Missing or lost guard
custody refuses success. A helper crash immediately invalidates the attempt and
aborts/joins Buddy; it does not provide handle retention across that crash.

This requires a trusted interpreter, helper/imports, OS loader, stable local
volume mapping and installed directory, including ancestor delete-child, ACL,
metadata and reparse mutation rights. Only trusted host/installer principals may
alter them. It is not a sandbox against a same-principal attacker or an untrusted
writable installation. Qualify actual Windows loader/read compatibility, denied
leaf write/replacement and ancestor rename, leaf/ancestor reparse refusal, guard
loss, and handle release after success/cancel/timeout before enabling the factory.

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

Retain small synthetic complete and media-omitted packages emitted by the actual
crate-private isolated exporter for the cross-repository runner controls. Record
the producer source, exact file inventory/digests, expected redacted report and
reproduction command with those fixtures. A test-only opt-in emission path may
reuse the existing producer fixture; do not expose a production export API or
manually recreate its outer marker. Treat these as synthetic producer evidence,
separate from live provider publication and native restore. Tests using a retained
oracle must keep its original executable bytes and source attribution explicit.

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
