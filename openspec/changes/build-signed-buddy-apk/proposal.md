# Build signed Buddy APK artifacts

## Why

REM-41 requires one Vellum/apk package owner from the first supported Manager
installer, without public community-catalog acceptance. Current Rust publishing
produces exact-tag target tarballs, provenance and completion digests, but no
signed APK. The existing Manager has actual independently pinned APKv3 tooling
and script-free verifier fixtures. A directly necessary packager can supply real
signed bytes for that consumer while release-pipeline, trust-enrollment, native
compatibility and installation remain separately unfinished.

## What changes

Add a build/sign/verify helper for actual Buddy payloads using the already
qualified external Vellum APKv3 tool. Freeze permanent package identity, stable
Git-tag-derived version/pkgrel, exact source and consumed SDK/build identity in
signed standard package metadata, fixed target/ABI correspondence and artifact
inventory. Produce isolated test-key artifacts first; integrate production
publishing only after its existing gates and approved signer are satisfied.

No new release filter, semantic-version calculator, tagger, publication engine,
Manager API, SDK runtime installation or community submission is introduced.
The unfinished REM-46 candidate and equal-date GitVersion regression stay intact.
No production tag, setting, asset, signing trust, tablet or service changes follow.

## Ownership

Main owns Rust release/build/packaging and this central producer change. SCRAPPY
owns a separately named Manager release-byte quarantine consumer, then future
consumption of this concrete contract. Root owns coordinated review/delivery.
SDK public capability contracts remain SDK-owned. Source placeholders are an
existing REM-46 policy gap and protected Cargo/SDK files remain untouched here.

## Source basis

Current REM-41 description and all 41 comments, REM-46 description and all 14
comments, exact Rust publisher and preserved REM-46 build helper, accepted Manager
ea0c753 / Docs029d823 verifier contract and minimal producer handoff, and pinned
APKv3 upstream documentation. This is precode, not an implemented artifact or
installation/trust qualification.

## Current coordinated delivery boundary

The original producer/resident implementation is already present in delivered
Buddy main. The remaining Buddy PR38 source diff is the usable source correction:
SDK v0.2.0 adoption, independent SDK tag/source proof, disjoint-output refusal and
focused tests. Docs PR25 synchronizes that precise implemented contract in
[canonical source admission](../../specs/buddy-package-source-admission/spec.md)
within this existing pair; it does not create a second feature or planning PR.
See [the scoped delivery receipt](source-admission-result.md) for exact revisions,
actual proof/Cargo identities, validation and Root's next integration action.

This parent remains active and unarchived. Source-proof completion does not
complete its actual artifact/signature/reproducibility, production signer/trust,
release integration, native install or lifecycle requirements. Existing historical
failures and unfinished tasks remain authoritative at their original scope.
