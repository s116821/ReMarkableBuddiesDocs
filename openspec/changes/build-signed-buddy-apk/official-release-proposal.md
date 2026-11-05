# Packaging convergence and official release proposal

Status: source/local preparation for maintainer review, November 5, 2026.
Nothing here admits signing, remote qualification, trust changes, publication
or tablet access. The tagged-source execution hold remains in effect. The
existing fixture producer remains test-key and installation-ineligible.

## Observed delivery and ownership

Delivered Buddy main `f6af5d1ce08c7ad518c0943d4a293e7c18688699` contains the
packaging code from [builder PR38](https://github.com/s116821/ReMarkableBuddies/pull/38)
and [resident PR123](https://github.com/s116821/ReMarkableBuddies/pull/123).
Every effective packaging blob from PR123 head
`221bdfa13d7482e420ee33c19e8d245e7a0c7d12` matches main, including the original
builder helpers/tests/CI, resident payload and unit-byte Git attributes. The
later ordinary release build.py selects installed-resident-output on ARMv7.
This is source absorption through the native delivery, not completed signing
or installer qualification. Preserve both drafts and evidence until the
maintainer reconciles their PR status; do not merge another copy of their code.

The normal builder reconciliation uses main for the ten add/add conflicts:
each incoming file is the reviewed resident extension of that builder file.
The entire resulting source tree equals delivered main before the separate
output-path refusal repair. That reconciliation's first successor adds only the
refusal repair; the later reviewed SDK identity adoption is described below.
The paired Docs draft still has its unique active contract/evidence; it must
remain active until the unfinished capability is verified, synced and archived.

[Windows Docs13](https://github.com/s116821/ReMarkableBuddiesDocs/pull/13) at
`a924d469cfc24757f71d079202da92845c0816c0` retains Windows qualification records;
the source adapter and quiet polling already shipped. Existing accepted cable
observations are not a reason to repeat human unplug tests. Precise invalidation,
competing-route and current composition gates remain separately owned.
[Manager57](https://github.com/s116821/ReMarkableBuddiesManager/pull/57) at
`0b678e4611bff20ecb86338d373b355dc98425c3` owns guarded package transitions,
stop/recovery and their actual transaction caller. This proposal edits neither
lane. Maintainer owns delivery; native operator remains the sole tablet owner.

## Exact resident input, still ineligible

The delivered RM2 fixture selected installed-resident-output, SDK commit
`c87e5628f35af5647c1d2da3331ad5e07a55f0f8`, and bundle SHA-256
`f9c4b44b9baf281bc47c74470ddd8d098853e79383e9323e5ff02ef2846fb477`.
It packages eight resident files plus package LICENSE/build.json. Executable,
adapter, profile and policy live under home/root/.local/lib/remarkable-buddies;
the two units live under usr/lib/systemd/system. Recovery policy v6 binds app,
adapter/native profile and units; native recovery uses lease v3 and restores
stock Reader and rm-sync. Dependencies are remarkable-os=3.28.0.172-r0 and rm2.
These are fixed fixture constraints, not a general firmware compatibility claim.
The SDK is built into the Buddy dependency and bundled adapter, not installed
as an independently versioned runtime package. No package script is executed.

Fresh remote tag observation finds SDK v0.2.0 tag object
`876f90b62ae4623b31295d45b3d13e2f99b99b72`, peeled commit
`a0c6480be6785480c2e0da76a3c06697a18efae4`, different from the consumed c87e5628.
The existing cargo_identity --sdk-tag check requires exact commit equality.
SDK publication alone therefore does not make this consumed pin tagged.
Do not label c87e5628 as v0.2.0 or weaken that check. The reviewed source adoption
below changes Buddy to the actual released commit; the historical native evidence
remains attributed to its original source. Exact-tag producer admission remains
an observed separate gap rather than an assumed pass.

### Reviewed source adoption and observed tag refusal

Maintainer source review accepted the SDK update after independently verifying
173 identical existing Rust/manifest/tool/license/native entries, four exact
bundle recipe files and the squash tree correspondence. Consumed c87e5628 is an
ancestor of PR31 head 2f7c886, whose complete tree equals released a0c6480. It is
not an ancestor of the squash commit itself. Between c87e5628 and that tree,
only deterministic bundle tooling, attributes/docs and OpenSpec closeout changed;
the Rust API/features/dependencies, existing native build/profile inputs and
licenses are unchanged. A new SDK release or retag is unnecessary for adoption.

Buddy now selects tag v0.2.0 in both dependency declarations, locks exact
a0c6480be6785480c2e0da76a3c06697a18efae4 and requires that same SDK hash in the
resident package contract. The native bundle hash remains f9c4b44b...: all
existing native inputs and the executed R128 recipe are identical in released
source. This is source/recipe equivalence plus prior operator evidence, not a
new native rebuild. The Git dependency's generated Cargo package version stays
0.0.0 because its source manifest omits version; Git tag and locked source remain
the version authority.

Ordinary locked Cargo metadata resolves both normal and dev edges to the actual
tag/commit. ARMv7 has root features development-input-diagnostics,
development-resident-bootstrap and installed-resident-output; the ordinary
AArch64 root has no enabled features. Both metadata graphs show the SDK's
development-capture/mock/native-adapter features (metadata includes dev edges),
with default features disabled on both declarations. These are resolved graphs,
not compilation evidence or a claim that dev mock code ships in the binary.

At Buddy be488154, the unchanged cargo_identity check with sdk_tag=v0.2.0 refused after
metadata because Cargo's generated a0c6480 checkout has no refs/tags/v0.2.0.
The direct rev-parse command exits 128; show-ref --tags exits 1 with no tags.
The checkout's origin is Cargo's local Git database, which also retains only
commit refs after normal Cargo resolution. No cache tag was fabricated/fetched
manually. With no SDK tag requested, the original helper accepts metadata-only
commit-pinned identity and explicitly returns tag=null. That separate observation
does not pass the required tagged identity or confer installation eligibility.

The source successor implements the maintainer-accepted explicit proof boundary:
--sdk-tag must be paired with --sdk-tag-source, an independent clean full Git SDK
release source. It reuses ordinary source snapshot admission with canonical SDK
origin, exact tag/HEAD, clean tracked inventory and actual Cargo manifest equality.
The real local tag object/peel must match two bounded canonical remote
observations; the local object already exists, so no fetch or ref/config write is
needed. Effective remote URL rewriting refuses. File and source/Git directory
identity, local snapshots and remote observations must stay unchanged. Build
pre/post, both targets and final completion recheck the same proof. The stable
tag object enters the existing normalized graph digest; filesystem facts remain
private. SDK signed metadata shape and test-key eligibility are unchanged.

Missing/refused proof is explicit; commit-only mode stays tag=null only when no
SDK tag/proof was requested. The dirty research checkout is not admissible.
Offline actual local-Git controls cover the positive tagless-Cargo case and
malformed/mismatched/moved/dirty/replaced proofs with a simulated canonical
remote transport. Original be488154 refusal remains historical evidence; it was
not rerun through or overwritten by this code. No live remote qualification,
source compilation, packaging or signing ran. Independent source review and a
separately admitted real proof run remain required. Manifest tag text, cache
commit refs and adjacent release JSON alone never replace actual tag proof.

Fresh [Buddy v0.62.0 release metadata](https://github.com/s116821/ReMarkableBuddies/releases/tag/v0.62.0)
points to native consumer `91dcc601154507790254946f8f0f811204a0fd43` and lists
only two target tarballs and provenance.json. No APK/index/key is published
there. Assets were not downloaded or executed in this preparation. An eligible
Buddy tag is only one gate; the SDK version, signer, verification and installed
lifecycle still need admission. Historical r5 absent-SDK packages and later
source-only preflight observations retain their original scope and must not be
replayed or relabeled as current resident qualification.

## Proposed official producer boundary

Keep apk_builder.py and its ephemeral fixture signer unchanged as a development
producer. Do not flip its eligibility field or swap in a production key. Add a
separately reviewed official mode/entry point only after the inputs below are
approved, with a distinct authenticated contract that the Manager explicitly
recognizes. Test-key profiles must remain refused even if their key is enrolled
accidentally. A signed assertion is not proof of native compatibility.

Official inputs must bind exact immutable Buddy semantic tag/object/commit,
consumed SDK release/commit and manifest, approved bundle hash, resolved Cargo
features/lock/graph, compiler/Cross/image/tool identities, architecture/ABI,
payload files/modes/epoch, units/recovery profile and qualified device/firmware
matrix. Keep one remarkable-buddies identity/database; derive pkgver from the
Buddy tag and keep pkgrel solely for reviewed packaging revisions. Reject
prereleases until their separately reviewed mapping/promotion policy exists.

The pinned apk tool currently accepts --sign-key as a file. A practical first
candidate is a protected offline signing station using that actual interface,
with private key available only to its approved bounded signer process. This is
a proposal, not a chosen signer or permission to provision a key. A remote/HSM
signer needs demonstrated tool integration before selection; do not assume it
works. Logs/receipts contain key IDs/public fingerprints, never private bytes.
Require an identified custodian, approved key algorithm, backup/recovery and
access policy, exact pinned tool/image and narrowly admitted signing inputs.

After signing, end the signer process and expose only immutable artifacts and
public trust material to a separate verifier. Independently verify package and
index signatures, exact metadata and script-free inventory, whole-file hashes
and sizes, payload hashes, target ABI, dependencies, and index metadata-hash
binding reconstructed from the verified APKs. Pass expected issuer pin through
an authenticated control channel. Never trust a key merely adjacent to a download.
Require same-input/same-key determinism evidence separately from repeatable
source compilation, plus wrong-key, tamper, truncation, same-version substitution,
duplicate/unknown identity, script/mode and interrupted-output controls.

## Proposed trust enrollment and release admission

The first trust root must be approved independently and shipped in a reviewed
Manager trust policy, or enrolled by an explicit user action that displays the
approved fingerprint. Package metadata and GitHub sidecar keys cannot bootstrap
that trust. Browser/helper and Electron must enforce the same allowlist and
artifact policy. Existing protected SSH identity remains a separate prerequisite.
Vellum bootstrap/key installation requires its own reviewed, consented bounded
transaction and rollback; no automatic network-script execution or implicit key
enrollment. Keep installed data/configuration/secrets through failure.

Before rollout, specify key IDs/epochs, how reviewed Manager releases distribute
new/revoked issuer policy to both hosts, old/new key overlap, offline/stale-policy
refusal and recovery from a compromised/lost signer. Rotation cannot be authorized
solely by a new package's own key; revocation cannot silently uninstall the
existing application. Pick and qualify the maintained trust-distribution mechanism
before code; this proposal does not invent a parallel trust service.

Reuse the maintained semantic-release and GitHub release pipeline. The current
ordinary pipeline builds a candidate, verifies integration, then creates/verifies
the official tag before publishing tarballs. It does not invoke the APK builder.
Proposed APK extension starts only after an exact eligible remote tag is verified,
with separate build/sign/verify admission and immutable source input. Preserve
the current ordinary pipeline until that extension is reviewed; do not send its
pre-tag candidate to the exact-tag APK producer or add a second version engine.

Only verified complete official artifacts may enter the existing release upload
path. Extend the maintained inventory/provenance and Manager quarantine contract
together, naming every APK/index/public-policy artifact and exact digest/size.
An incomplete, mutable or mismatched release must remain unavailable for install
even if GitHub marks it published. CI success, source absorption and a self-signed
receipt do not grant release admission. No job, environment, secret, permission,
trust file or GitHub setting changes are made by this proposal.

Manager57 must combine actual signed package/database ownership with the exact
solver result, installed file identities, current activation/boot/lease, durable
intent and post-reconnect reconciliation before a mutation. After ambiguity,
observe/reconcile rather than repeat stop/install. Prove preservation and rollback
for install/update/disable/uninstall/replacement, process/USB loss, low space and
recovery failure through both browser/helper and Electron on supported RM2.
Source handoff uses that same Vellum identity: equivalent same-version packages
need no reinstall; source preference never silently downgrades or creates a
second service/database. Real public catalog listing is deferred and is not an
official local-package release dependency.

## Inputs and gates the maintainer must supply

| Gate | Required input or decision | Owner / next action |
| --- | --- | --- |
| Source | Buddy selects actual SDK v0.2.0/a0c6480 with unchanged bundle; explicit release-source proof implemented and only offline qualified | Maintainer reviews exact successor and CI, then admits a real clean SDK source/tag proof and eligible Buddy tag |
| Qualification | Exact producer revision, source path, build budget/tool identities and separate execution admission | Maintainer reviews new packet; existing held/spent packets stay untouched |
| Signing | Selected custodian/location/interface and approved public fingerprint/policy | Maintainer supplies concrete proposal for approval; no production key created/read |
| Trust | Initial enrollment, rotation/revocation/staleness and Vellum bootstrap rollback | Manager/package owner implements only after approved trust contract |
| Contract | Distinct official eligibility/compatibility schema and Manager verification policy | Producer/Manager owners review together; test profile never promoted |
| Release | Post-tag APK path, authenticated complete asset inventory/provenance, incomplete-release refusal | Maintainer reviews maintained workflow change; no resource/settings edits now |
| Lifecycle | Signed Vellum database/solver ownership, guarded mutation and exact installed recovery | Manager57 owner plus exclusive native operator; both host distributions required |
| Delivery | Fresh exact-head CI and independent source/Docs review; retain unfinished canonical lifecycle | Maintainer publishes/reviews; broader capability stays open |

Source basis: fresh immutable Git comparisons and GitHub PR/release/tag outputs,
current producer/native payload/workflow source, central active contract, and
maintainer scope/holds. The official design above is a proposal, not implemented
or executed behavior. Private task coordination has no public transcript link.
