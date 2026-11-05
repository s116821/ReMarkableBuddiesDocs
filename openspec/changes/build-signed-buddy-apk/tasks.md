# Tasks

## 1. Contract and implementation

- [x] 1.1 Independently review exact producer scope, actual input proof, signed metadata/key/version/target contract against REM-41/46 and consumer requirements before code. Initial1d7b167 review found build-input admission and exact serialization gaps; subsequent accepted contract/source amendments rechecked and resolved them (Docs dddfc011 and [source review5503229901](https://github.com/s116821/ReMarkableBuddies/pull/38#pullrequestreview-5503229901)).
- [x] 1.2 Freeze concrete serialization with Manager owner and implement actual external-tool build/sign/verify helper without a release engine or source version field.
- [ ] 1.3 Derive exact Buddy/consumed-SDK/build identity from real build/artifact inputs, rejecting mismatches and preserving untagged/absent SDK as ineligible.
- [x] 1.3a Qualify metadata-only admission of Cargo's exact root completion marker while refusing all other SDK dirt and invalid marker identity/type/content; no source compilation or package qualification follows. Source636a2f6 reviews5580852332/5580852439 accepted; current Linux nine controls including symlink and full hosted run39370871074 pass. See integration-result.md for separate Windows skip and remaining package gates.
- [ ] 1.3b Review and verify ordinary Git source admission in the pinned Cross views. Local controls cover raw inventory, mode and dirty-state refusal. The live mapping and source observation are separate, and build/SDK qualification remains open.
- [ ] 1.4 Produce real reproducible test-key Buddy APK/index/public-key artifacts from an actual checked executable; never substitute text/fake metadata for payload proof.
- [x] 1.5 Refuse equal/nested build and final output roots before source/tool admission or creation; pure-local controls cover all three overlap forms and normal sibling admission. No tagged build or signing is implied.
- [x] 1.6 Adopt reviewed actual SDK v0.2.0 source in both dependency declarations/lock and resident SDK pin, retaining exact native bundle hashes; observe both locked target graphs and preserve the unchanged exact-tag check's concrete missing-ref refusal.
- [ ] 1.7 Review and implement legitimate SDK release tag proof independent of Cargo's tagless generated checkout, with exact commit/manifest and pre/post tag-object binding. Do not create cache tags or relax identity checks; see official-release-proposal.md.

## 2. Verification and delivery

- [ ] 2.1 Verify actual signature/control/payload negatives, input/identity/ABI/bounds/timeout/inventory failures and script nonexecution with pinned tool.
- [ ] 2.2 Run exact scoped host/helper/Docs/OpenSpec checks and independent evidence review; identify missing build or SDK-tag inputs precisely.
- [x] 2.3 Publish linked implementation/Docs drafts and durable handoff to Manager consumer, preserving unfinished parent/lifecycle gates.

## 3. Production and full capability

- [ ] 3.1 Provision and qualify approved production signing trust, enrollment/rotation/revocation and authenticated release identity.
- [ ] 3.2 Qualify actual model/firmware/SDK/Vellum dependencies, payload/service ownership, data-preserving lifecycle, backup/rollback and source handoff on supported hardware.
- [ ] 3.3 Integrate APK artifacts with qualified maintained release pipeline and stable/prerelease promotion policy, preserving tag-before-build and no custom release engine.
- [ ] 3.4 Complete required checks, coordinated review/merge, canonical sync/archive and downstream REM-35 acceptance only when the full scope is verified.
- [x] 3.5 Prepare a concrete official signer/trust/release integration proposal, separating observed source absorption from pending approval and execution. See official-release-proposal.md; this completes preparation only, not 3.1–3.4.


## October13 scoped evidence

Contract/precode and the concrete producer were independently reviewed before
each implementation amendment. Exact current implementation4e79104 and paired
Docsfdb33b7 are linked in RustPR38/DocsPR25; source acceptance is recorded in
[review5503229901](https://github.com/s116821/ReMarkableBuddies/pull/38#pullrequestreview-5503229901).

The successful real historical-tag two-target invocation produced signed test-key
APKs/index/public key after fresh source compilation and direct runtime checks;
[owner evidence](https://github.com/s116821/ReMarkableBuddies/pull/38#issuecomment-6145439700)
and [independent saved-evidence consistency](https://github.com/s116821/ReMarkableBuddies/pull/38#issuecomment-6145472860)
separate actual tool execution from receipt/hash inspection. SDK absent is observed
on both actual Cargo graphs; consumed-SDK pinned/tagged variants remain pending.
Whole-package/same-key reproducibility and signature-valid malformed metadata,
mode/script and other full negatives remain pending, so1.3/1.4/2.1/2.2 stay open.

The installation-ineligible fixture is durably saved under Personal/ChatGPT:
[transport-only bundle](https://drive.google.com/file/d/1wVwlgTsJbp3wZw0IGbzqlaW2WaGijrNP/view?usp=drivesdk)
and [hash manifest](https://drive.google.com/file/d/1kMM0A6dnXiiNy9x4h7h9OSqP3LN96PpR/view?usp=drivesdk).
Stored bytes were downloaded and SHA256/size matched local originals. Manager
owner received links, manifest hashes and an independently communicated issuer
SPKI for host-only offline consumer verification. This is durable handoff2.3,
not PR13 ZIP admission, production trust or physical lifecycle qualification.
All production/native/full release and coordinated lifecycle items remain open.
