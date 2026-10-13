# Initial APKv3 producer serialization

This is proposed exact serialization pending consumer/independent recheck.
All metadata comes from the actual source-build admission in design.md. Valid
fixture signatures authenticate these package bytes/claims, not compiler truth.

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
