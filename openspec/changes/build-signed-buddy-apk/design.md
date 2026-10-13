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
proof that an arbitrary binary was built from that source. Package build input
comes from a recorded actual build or a verified immutable official artifact
whose provenance/inventory and bytes match. The packager records which basis it
used. SDK identity must come from actual resolved Cargo metadata/lock/build
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
capability. Exact field serialization is reviewed with the consumer before code.

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
package/tool phase) and output diagnostics (16KiB sanitized per phase). Streams
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
