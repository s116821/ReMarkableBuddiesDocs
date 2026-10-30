# Signed APK builder design

## Exact scope

The helper only builds/packages/signs/verifies application bytes. Maintained
release Actions remain responsible for source selection, filtering, versions,
tags and publication. Do not expand the old custom coordinator or replace the
unfinished upstream-action candidate as a shortcut. The first deliverable is an
actual reproducible test-key APK and its verified metadata, not a proposed JSON
schema posing as a package. Production pipeline integration remains unchecked.

Reuse the producer's existing exact-tag build/version verification and ELF/ABI
checks where applicable. A clean exact tag and peeled source SHA must match;
modified/shallow/missing/wrong-tag input refuses. Never accept caller text as
proof that an arbitrary binary was built from that source. Initial input is ONLY the actual reviewed source-build path below. External
official-artifact input remains unsupported until separately qualified
quarantine/provenance/trust admission exists. Matching caller JSON and hashes
are never an alternative source-build admission. SDK identity must come from actual resolved Cargo metadata/lock/build
input, never from the current working override or a guessed version.

Initial package identity: name and origin `remarkable-buddies`. Initial stable
version is the exact vMAJOR.MINOR.PATCH tag without v, with separate nonnegative
pkgrel encoded using standard apk -rN. Reject prerelease/build-metadata tags in
this first helper rather than invent a mapping. That leaves the requested later
prerelease/promote flow open. Application and SDK versions are not source fields.

Targets are fixed armv7-unknown-linux-gnueabihf -> armv7 and
 aarch64-unknown-linux-gnu -> aarch64, with measured ELF class/machine/endianness,
interpreter and ABI evidence. This correspondence is build data, not an RM1/RM2/
Paper Pro firmware eligibility table. Initial fixture payload paths are fixed
usr/bin/reader-buddy plus the applicable license/provenance file, without service
scripts or arbitrary caller paths. Actual Vellum root/lifecycle ownership remains
a separate required design before installable artifacts.

## Authenticated metadata

Use standard APKv3 metadata and its signed vendor tags, not an unsigned sidecar
as the authority. Fixed metadata includes name/version/arch/origin/repo-commit
and deterministic build-time. Reserved remarkable-buddies: tags carry contract1,
canonical source repository, exact Buddy tag/source, Rust target, actual SDK ref
kind/tag/source and build-profile/evidence class. Values are bounded, unique and
canonical; duplicates, missing/unknown required fields or contradictory identity
refuse. The actual APK hash/size and standard signed index bind artifact bytes.

An actual untagged SDK commit is reported as such; do not fabricate an SDK tag
from Cargo's tooling version. A legacy source that demonstrably consumes no SDK
is explicitly absent. Neither can satisfy the required production SDK-version
contract. Unqualified or unknown profile/firmware/lifecycle stays installation
ineligible, regardless of valid signature. No compatibility field grants native
capability. The exact field serialization is in serialized-contract.md and is reviewed
with the consumer before code.

Upstream mkpkg/mkndx generate APKv3 package/index bytes; verify then bounded
adbdump/query inspect those actual fields in isolated roots. Standard signed
index/package metadata must agree. No add/del/upgrade/Vellum wrapper is called;
no package script executes. The current wrapper mutates virtual-package state
before parsing observation commands and is unsuitable for this offline step.

## Signing and deterministic artifacts

Use the existing externally built pinned tool ee31d275, SHA7488a9650411143a205bf80af511203fadd79499e21613c970b4ef8c207fe11a,
with its owner-verified 417 source entries and immutable fixture image receipt.
No binary/source redistribution or new host/global tool installation is needed.
The tool's GPL/source obligations remain explicit if redistribution is proposed.

First tests generate RSA2048 fixture keys only inside generation tmpfs, export
public key/DER fingerprint, and discard private material before observation.
Observation uses independently supplied/pinned fixture public key, never a key
trusted merely because it arrived beside the package. Production signer/private
key provisioning, enrollment, rotation/revocation and authenticated release-source
policy require their own verified gate; no automatic enrollment or repo-secret
mutation. No key material or package script body enters logs/receipts.

Set deterministic file modes/ownership/times, source-commit epoch, ordering and
compression choices; build twice with the same retained fixture key and inputs
and compare exact APK/index bytes. A fresh key is not expected to produce the
same signature. Verify output names/inventory/hash/size and all signed identity
before atomically publishing a new local output directory; never overwrite an
existing receipt/package or silently rebase inputs.

## Bounds and failures

Producer inputs are fixed regular files, no symlink/device/special file or
caller-controlled archive extraction. Bound package/input size (128MiB per target),
metadata (64KiB), file inventory (fixed <=8), subprocess time (120s per actual
package/tool phase;900s for the separately bounded fresh source compilation only)
and output diagnostics (16KiB sanitized combined per phase). Streams
hash/copy with pre/post identity and complete byte counts; changed/truncated
input, unexpected inventory, signature/metadata mismatch or timeout discards
incomplete staging and preserves earlier outputs. Container network is disabled,
capabilities dropped, host credentials/trust/config excluded and mounts read-only
except owned new outputs/tmpfs. Do not widen shared image tags or permissions.

## Verification and limits

Use actual signed package bytes and independently pinned external tool, not only
mock command argv. Test wrong/missing key, tampered signed tags/control/payload,
truncated package, input mutation, conflicting tag/source/SDK/target/ABI, extra
files/escaping links, wrong output/version/pkgrel and reproducibility. Refusals
must be recognized integrity/trust/validation outcomes, not generic crashes.
Inspect metadata without executing scripts; sentinel remains absent. Use an
actual checked Buddy executable payload, not a fixture text file relabeled as
Buddy. If exact build or SDK tag is unavailable, record that explicit limitation
and finish independent build/sign/verify work without a production claim.

No real-device installation, firmware mapping, source switching, data preservation,
service rollback, trusted production signing, upstream catalog acceptance or
release-pipeline rollout follows. Those remain REM-41/35/46/55 responsibilities.

## Primary sources

- Pinned mkpkg: https://raw.githubusercontent.com/vellum-dev/apk-tools/ee31d275c7a2b7486e6de481ffe624b1de46d131/doc/apk-mkpkg.8.scd
- Pinned package fields/tags: https://raw.githubusercontent.com/vellum-dev/apk-tools/ee31d275c7a2b7486e6de481ffe624b1de46d131/doc/apk-package.5.scd
- Pinned query fields: https://raw.githubusercontent.com/vellum-dev/apk-tools/ee31d275c7a2b7486e6de481ffe624b1de46d131/doc/apk-query.8.scd
- Current concrete consumer: https://github.com/s116821/ReMarkableBuddiesManager/blob/ea0c75328cea68ca0797ea1ee7043ad4428dd55e/docs/vellum-verification.md

Exact serialization/build-input qualification and fixed fixture payload paths are
proposed decisions pending independent precode and consumer review.

## Initial actual build-input admission

The helper executes the existing tag-before-build subset: verify clean complete
Git source/tag/peeled SHA; use the reviewed Cross target configuration and run
cross run --locked --release --target TARGET --target-dir OWNED --bin reader-buddy
-- --version with expected tag/SHA build-script variables. Runtime version must
match the actual tag. Reuse the preserved REM-46 build.py/abi.py checks as
reference, not its unsigned provenance as authentication or a new coordinator.
No prebuilt executable path or external receipt is admitted in the initial CLI.

Immediately before and after each actual build, collect cargo metadata --locked
--format-version 1 --filter-platform TARGET, Cargo.lock SHA, source Git status/
HEAD/tag, the SDK package's actual git source fragment/resolved checkout HEAD,
SDK manifest hash/status, compiler/cross/image identity and exact argv/features.
Require stable matching inputs, fixed canonical SDK repository when present,
exact one resolved SDK package, actual clean resolved SDK source and lock agreement.
For Cargo-managed Git checkouts, cleanliness may exclude only the root untracked
`.cargo-ok` completion marker. Cargo documents this marker in its
[GitCheckout reset contract](https://doc.rust-lang.org/stable/nightly-rustc/cargo/sources/git/struct.GitCheckout.html#method.reset).
The marker must be absent or an empty regular file with one link; a tracked
marker, symlink/reparse point, directory, nonempty file or changed file identity
during inspection refuses. Confirm the actual Git top-level is the resolved SDK
root, exact HEAD matches the resolved source fragment, and all remaining tracked
and untracked paths are clean using Git's complete untracked inventory. Do not
delete the marker, alter ignore/configuration files, hide unrelated changes or
accept marker presence as source authenticity. Existing pre/post-build source,
SDK, lock, manifest and compiler comparisons remain required. Host-only actual
Git controls must cover the valid marker, ordinary dirty tracked/untracked files,
nested/renamed lookalikes, tracked markers and invalid marker types/content.
Record absent SDK only if actual metadata has none. A supplied stable SDK tag
must resolve to that actual SDK SHA; without verified tag record commit-pinned,
not a version inferred from Cargo. This remains developer source-build evidence,
not authenticated compiler/SLSA proof or production trust.

The executable from that owned build output is fstat/hash/ELF-verified, checked
by actual --version under the declared target runner, then copied with complete
byte counts and rehashed before/after package generation. The helper produces
its internal build.json itself from these observations. It does not accept caller
build identity, compiler fields, profile, executable digest or eligibility as
admission. Current unqualified-development/legacy-no-sdk vocabulary is fixed;
no approved native profile can be invented by a command option. Failure of build,
identity recheck or actual target execution ends that build; no cached binary
fallback or unsigned receipt substitution.

Production source/compiler authentication, source-version placeholder remediation
and the maintained REM-46 pipeline remain open. The first source build can use
an isolated already-stamped fixture tag; it must not create/change a live tag.

The first actual fresh ARM build at public v0.2.0 hit the original120s phase
watchdog while creating hundreds of dependency/object files, before an executable
was available. That incomplete output and owned cleanup are preserved. A900s
compilation-only bound accommodates normal clean compilation; completion still
requires actual process exit and every original input/runtime/descriptor check.
Metadata, runtime version, signing/verification and observation retain120s bounds.
Retain already collected bounded compiler stdout/stderr privately on both success
and refusal, with fixed public classifications; never enlarge the16KiB combined
diagnostic allowance, admit partial/cached executable output, or retry unchanged
settings as a substitute for actual build evidence.


The actual Windows-to-Linux build diagnostic found the same tracked source bytes
clean in host Git (core.autocrlf=true) but changed in the pinned Linux image's
default Git view; command-local core.autocrlf=true restored equality without
changing source/index/config files. This is a concrete conversion-view mismatch,
not proof of the complete historical build-script failure reason. Record the
host's effective core.autocrlf (false/true/input) and core.eol (lf/crlf/native),
resolve native eol to the host platform, and supply only those verified semantics
in the existing temporary Linux Git config alongside its exact safe.directory.
Recheck these effective inputs after build/runtime and retain the comparison
privately. Both host and container still must admit exact clean tagged source;
never suppress Git status, alter source/index, disable cleanliness, or treat
line-ending configuration as compiler/source authentication. Unknown semantics
refuse. Metadata, compilation and artifact caps/eligibility remain unchanged.


The corrected fourth actual ARM build completed fresh compilation in 4m54s, but
Cross run began another compilation and hit the unchanged120s runtime-phase
bound. That attempt remains compilation-only and produced no admitted package.
A separate read-only host diagnostic of its retained file returned the expected
version under the existing image's QEMU; it is not a package-admission shortcut.
For subsequent fresh builds, replace Cross run with direct execution of the
newly built descriptor-checked file in the same immutable target image. Keep
runtime120s and combined diagnostics16KiB; no compiler invocation, writable
source/target mount, network, new runner, cached input or library installation.
Mount only the actual newly built file read-only, retain original descriptor and
path identity/hash checks before/after runtime and freeze exactly those bytes.

ARM uses existing /usr/bin/qemu-arm-static with -L/usr/arm-linux-gnueabihf;
AArch64 uses /usr/bin/qemu-aarch64-static with -L/usr/aarch64-linux-gnu. Observe
actual image identity and fixed runner/dynamic-loader file size/hash before and
after; require the observed reviewed identities and paired equality. The image
hash binds the remaining sysroot contents; this does not qualify tablet/native
ABI or complete dynamic-dependency/source/compiler authentication. Capture exact
actual runtime argv, runtime output and runner observations privately, preserving
fixed public failures and bounded buffers even on refusal. The selected file
must come from this invocation's successful fresh source compilation, not any
prior failed target directory or diagnostic receipt. Version mismatch, runtime
failure/timeout, changed file/image/runner/loader or missing identity refuses.
