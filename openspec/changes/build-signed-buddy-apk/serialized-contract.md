# Initial APKv3 producer serialization

This is proposed exact serialization pending consumer/independent recheck.
All metadata comes from the actual source-build admission in design.md. Valid
fixture signatures authenticate these package bytes/claims, not compiler truth.

## Existing project license attribution

Source license admission is not restricted to a Cargo `license` field. The
initial source retains the project's tracked GPL version 3 license and its
[project-specific declaration](https://github.com/s116821/RemarkableBuddiesDocs/blob/d34c14d5d25eee671f7441a69f4feef7bd2c5d69/docs/licensing.md),
which preserves the original licensing and does not relicense inherited material.
GitHub's current public repository-license API detects `GPL-3.0` for the same
`LICENSE` Git blob `f288702d2fa16d3cdf0035b15a9fcbc552cd88e7`.
[SPDX identifies this legacy identifier](https://spdx.org/licenses/GPL-3.0.html)
as deprecated and explicitly version 3 only. It is not neutral between only and
or-later, and GitHub detection is not an independent copyright-owner grant.

For this exact existing project declaration and committed license blob only,
the initial producer may retain the observed legacy `GPL-3.0` identifier when
Cargo has no license declaration. It must check both committed blob identity and
actual file bytes: LF SHA256
`3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986`,
or its existing CRLF checkout SHA256
`230184f60bae2feaf244f10a8bac053c8ff33a183bcc365b4d8b876d2b7f4809`.
An explicit matching `GPL-3.0` or `GPL-3.0-only` declaration may be preserved;
contradictory declarations, altered/unknown license bytes or blobs refuse this
initial mapping. Other license policy changes require their own source review.
Do not infer a grant from the license's application appendix, translate to
or-later, change protected Cargo files, or create a new licensing choice merely
to build an offline fixture. This is recorded source attribution with known
legacy metadata, not legal advice or production qualification.

## Standard fields and fixed inventory

- name and origin: remarkable-buddies, permanent identity.
- version: MAJOR.MINOR.PATCH-rPKGREL, from actual stable vMAJOR.MINOR.PATCH tag; tag <=64 ASCII bytes, each numeric component canonical without leading zeros.
- pkgrel: integer0..65535, canonical decimal, packaging-only.
- arch: armv7 or aarch64, matching actual verified Rust target/ELF/ABI.
- repo-commit: actual 40 lowercase hex Buddy source SHA.
- build-time: source commit epoch, nonnegative integer <=2^63-1.
- license: actual source SPDX license, bounded64 ASCII bytes; absent/unsupported license refuses.
- description: fixed ReMarkableBuddies test-key source-build package.
- paths: usr/bin/reader-buddy mode0755; usr/share/remarkable-buddies/LICENSE mode0644; usr/share/remarkable-buddies/build.json mode0644. Only their parent directories, mode0755, are included. No links/xattrs/scripts/triggers/service unit/data/config/secrets.
- artifacts: remarkable-buddies-VERSION.armv7.apk and remarkable-buddies-VERSION.aarch64.apk, plus signed buddy-index.adb and public fixture key only. No private key output. Missing target build yields no completed two-target output.

build.json is canonical UTF8 JSON generated from actual build observations, <=64KiB,
with source tag/SHA/epoch, target/ELF/ABI, resolved SDK ref/tag/SHA/manifest+lock
hash, exact features/compiler/cross/image/argv and executable SHA256/byte count.
Its bytes are part of the signed package payload. No external build.json is admitted.
The same source/compiler limitations are explicit in evidence and do not disappear
because this file is signed.

## Exact reserved signed tags

Tags are unique ASCII strings NAME=VALUE with no whitespace, escapes or empty
values. Names/values use the pinned APKv3 allowed character set; max256 bytes per
tag, max18 tags and max4096 combined bytes. Serialize in ASCII lexical name order.
The following names are exact, all beginning remarkable-buddies:

| Suffix after remarkable-buddies: | Value |
| --- | --- |
| contract | 1 |
| evidence | developer-source-build |
| eligibility | not-qualified |
| source-repo | https://github.com/s116821/ReMarkableBuddies |
| source-tag | actual stable Buddy tag |
| source-sha | actual 40 lowercase hex source SHA |
| target | armv7-unknown-linux-gnueabihf or aarch64-unknown-linux-gnu |
| abi | gnu-arm-eabihf or gnu-aarch64, consistent with measured ELF |
| pkgrel | canonical decimal0..65535, matching version |
| binary-sha256 | actual64 lowercase hex payload executable digest |
| sdk-ref | tagged-git, commit-pinned or absent |
| sdk-repo | https://github.com/s116821/ReMarkableOpenSDK, present iff SDK exists |
| sdk-sha | actual40 lowercase hex resolved SDK SHA, present iff SDK exists |
| sdk-tag | actual verified stable SDK tag, present iff tagged-git |
| profile | unqualified-development if SDK exists; legacy-no-sdk iff absent |

Tagged-git requires sdk-repo/sdk-sha/sdk-tag and matching actual resolved tag/SHA.
Commit-pinned requires sdk-repo/sdk-sha, forbids sdk-tag and remains version/
production-ineligible. Absent forbids all three SDK details and requires actual
no-SDK build metadata. No placeholder empty/zero version or guessed SDK tag.
All three initial variants are explicitly installation-ineligible: trusted
production signer/compatibility/lifecycle is not part of this first builder.

Duplicate names, unknown remarkable-buddies: names, missing required fields,
unknown enum values, wrong encoding/limits, inconsistent arch/target/ABI/version/
pkgrel/source/SDK/profile or package/index/payload metadata refuse. Initial
producer emits no unrelated vendor tags. A future contract change needs explicit
version/review; an unknown contract is unsupported, never best-effort parsed.

## Signature reading boundary

Verify APK/index with independently supplied fixture public key before bounded
metadata inspection. Standard indexed package-info contains the signed tags;
query exposes commit/tags. Require package/index identity and hash agreement,
and actual build.json/executable hashes from signed payload inventory. No install,
script invocation, key enrollment or Vellum wrapper. Public key fingerprint is
SHA256 of DER SubjectPublicKeyInfo, independently supplied, not trusted from its
adjacency to the APK. Production trust/enrollment remains unsupported.

## Exact build.json v1 schema and bytes

Top-level keys are exactly schema, evidence, eligibility, source, target, sdk,
cargo, toolchain, build and binary. Unknown/duplicate keys at every object level
refuse. schema is integer1; evidence is developer-source-build; eligibility is
not-qualified. No floating-point values, NaN, infinity or booleans as integers.

| Object | Exact fields and types |
| --- | --- |
| source | repository fixed Buddy HTTPS URL; tag stable tag string; sha40 lowercase hex; epoch integer0..2^63-1 |
| target | rust_target fixed target enum; apk_arch matching armv7/aarch64; abi matching gnu-arm-eabihf/gnu-aarch64; elf_class integer32/64; elf_machine ARM/AArch64; elf_endian little; interpreter absolute bounded ASCII path observed from ELF |
| sdk | null iff actual no SDK; otherwise ref_kind tagged-git/commit-pinned, repository fixed SDK HTTPS URL, sha40 lowercase hex, tag stable string iff tagged-git otherwise null, manifest_sha256 64 lowercase hex |
| cargo | lock_sha256 64 lowercase hex; metadata_identity_sha256 64 lowercase hex of canonical normalized resolved source/SDK/feature identity; features sorted unique ASCII array <=64 items, each<=128 bytes |
| toolchain | rustc_release ASCII<=128; rustc_commit40 hex or null; rustc_host ASCII<=128; cross_version ASCII<=128; cross_binary_sha256 64 hex; image_digest sha256:64 hex; build_configuration_sha256 64 hex |
| build | argv ASCII token array<=64, each<=256; environment object with exact keys RUSTFLAGS,CFLAGS,CXXFLAGS,CPPFLAGS,LDFLAGS, each ASCII<=1024; profile fixed unqualified-development or legacy-no-sdk; source_build_helper_sha256 64 hex |
| binary | path fixed usr/bin/reader-buddy; sha256 64 hex; bytes integer1..134217728; mode integer493 (0755) |

All strings are ASCII with no control characters. Stable tags<=64 bytes,
interpreter<=256. SDK null/tag requiredness exactly matches the signed tags;
profile legacy-no-sdk iff sdk is null. Environment is the actual explicit build
environment, not a current-shell dump; unrecorded compiler/linker override refuses.
argv/environment temporary source/target/SDK/tool roots are replaced ONLY by
verified complete path-prefix boundaries with fixed tokens SOURCE_ROOT,
TARGET_ROOT,SDK_ROOT,TOOL_ROOT. Other values remain exact. Raw actual paths,
commands and metadata stay in private build evidence; normalization is not a
claim that different flags/inputs are identical. Normalize before computing
metadata_identity_sha256 and reproducible package bytes.

Bytes are UTF8 without BOM, ASCII-only JSON via sorted object keys, compact comma/
colon separators, standard JSON escaping, then exactly one LF; no indentation,
CR or trailing spaces. Arrays retain defined order (features sorted; argv exact).
Duplicate-key-aware parse, schema/type validation and canonical re-encoding must
produce exactly the original bytes. Whole file<=65536 bytes. All file/SDK/lock/
binary digests and matching signed tags are verified against actual source-build
observations; a signed build.json is not compiler attestation.

## Verified index-to-package binding

The APK index hashes field is the upstream package METADATA hash. It is never
named or compared as SHA256 of the complete APK file. Record these separately:
index_metadata_hash (algorithm/encoding and value exactly as pinned tool exposes),
apk_file_sha256, apk_file_bytes, and each signed payload file digest/size.

Use actual pinned mkpkg to create signed APKs, then pinned mkndx over exactly
those verified APK paths to generate the signed local index. Independently verify
both package and index with the externally supplied fixture key. Inspect each
actual APK's bounded authenticated metadata using the pinned adbdump/readback
path after verification. Inspect the signed index using explicit all-matches,
all required fields including hashes,tags,commit,arch,version, and select BOTH
expected architecture entries, not a single best-match result.

The binding predicate is the pinned tool's package metadata-hash identity from
verified APK metadata versus the verified index entry, plus exact equality of
name/version/arch/origin/commit/tags and the index's recorded artifact filename/
size where applicable. Whole-file hash/size is computed directly from immutable
produced bytes independently; it is not derived from hashes. Payload digests are
verified by actual apk verify and separately compared with generated build.json/
executable/license inventory. The tool's precise hash algorithm/encoding and
available readback command must be confirmed using the actual tool BEFORE this
predicate is accepted as executed. If the pinned readback cannot expose a valid
binding, refuse completion and seek a narrow upstream-supported readback; do not
invent a hash recipe or fall back to matching only caller fields.

Qualify using real two-architecture packages/index with one entry replaced by a
different valid signed package having the same name/version/arch but different
metadata or payload, altered index tags, wrong entry hash, truncation and duplicate
entries. Correct tool integrity rejection versus predicate rejection remains
separate. These tests confirm binding and do not grant installation eligibility.

### Concrete initial metadata-hash readback

For the first implementation, generate a fresh comparison index with pinned
mkndx --hash sha256 from exactly the independently verified immutable APK files,
using the same explicitly supplied fixture signer. Do not use an existing index
or update/reuse entries. Verify the regenerated index, then bounded adbdump
--format json both signed indexes and compare their two package entries' hashes
and complete standard/tag metadata. This invokes the tool's actual package
metadata identity generator; it does not hash whole APK bytes as that identity.
mkndx's source calls apk_extract_generate_identity with its configured algorithm
and stores that digest in the index hashes field; full-file file-size is separate.
Actual byte tests must confirm command/encoding and refusal when a different valid
signed same-name/version/arch package is used to regenerate the comparison.
APK full-file SHA256/size and payload hashes remain separate checks. No index
hash is accepted solely from caller text or matching name/version.

Both index generations use the standard upstream `--pkgname-spec` value
`${name}-${version}.${arch}.apk`, matching the two actual artifact filenames.
The authenticated JSON readback must contain that exact `pkgname-spec` beside
`packages`; compare it as well as both entries. This is a standard signed index
field, not a custom filename hash or payload tag. Refuse an absent/different
pattern, duplicate keys or package entries, or any other unexpected initial
index root member. Filename/whole-file-size observations remain separate from
the upstream metadata hash. Confirm this actual pinned-tool readback before
calling the complete producer byte binding qualified.
