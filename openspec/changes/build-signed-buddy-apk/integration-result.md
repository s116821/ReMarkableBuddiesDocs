# Delivered-parent APK integration

Source `61bcd76db6108a3f7a94fec37e00383691ae8a84` normally integrates
the existing APK branch `d68d5a0` with delivered main `42b5108`.
The effective child is exactly 16 release helper/test/configuration paths.
All 16 retain their exact original branch bytes, including the optional bounded
ABI reader. Every other tracked path equals delivered main, preserving its
Cargo/SDK identity, Reader implementation and maintained release workflows.
Historical pending Reader ancestors are not included in the effective child.

The paired Docs integration uses delivered parent `3eb4174`, retaining the five
original APK change artifacts unchanged plus this result. Historical r5 evidence
remains attributed to its actual v0.2.0 source and absent-SDK build. It does not
qualify SDK-consuming current source, reproducibility or installation.

Current Windows host checks ran 34 tests: 31 passed and three platform/container
controls were skipped. Docs ran 12 tests successfully; manifest checks preserved
25 current guidance files and 126 original blobs. Strict OpenSpec validation
passed all 42 items. Diff checks passed. No container, source compilation,
signer, package generation, installation or tablet contact was performed.

Current exact-head hosted checks and independent integration review remain open.
Source/compiler reproducibility, consumed-SDK variants, full signed negatives,
production trust, release integration and physical lifecycle remain unfinished.
No task completion, canonical sync or archive follows from these host controls.

Source basis: complete Git index comparisons against both merge parents,
unchanged existing source/spec artifacts and current retained host-check logs.

## Cargo-managed SDK metadata admission

Source successor `636a2f66e2f1d34381537cc0c5f4e113b184bd24` changes only
the SDK checkout cleanliness check and adds actual local-Git refusal controls.
The preceding accepted source integration remains attributed to `61bcd76` and
reviews5580813749/5580813819; this is a separate functional repair.

Observed Cargo is `1.98.1 (797e8a9bc 2026-08-05)`. Current Buddy tag v0.11.0
resolves42b5108 and consumes SDK32b86e4. Its actual Cargo checkout under
`.cargo/git/checkouts/remarkableopensdk-717fbf1704bfa168/32b86e4` has only
an untracked, empty regular root `.cargo-ok` file. The existing offline
metadata-only admission refused `clean actual SDK checkout`; the narrow repair
now admits the same SDK as commit-pinned, with no invented SDK tag. This was
metadata resolution from the integration checkout, not an exact-tag build.
Neither the marker nor shared cache/configuration/ignore files were modified.

Nine focused actual local-Git tests ran: eight pass and the Windows symlink
creation control is explicitly skipped for missing host privilege. Hardlink,
directory, nonempty/tracked marker, wrong HEAD/root, other dirty tracked and
untracked files, nested/lookalike marker and changed-during-inspection controls
pass. Existing20 source-helper controls pass. Linux symlink execution, current
hosted checks and independent repair review remain pending, so task1.3a stays
open. No compilation, runtime, signed package or production qualification follows.

Source basis: current Cargo version, immutable Buddy tag/manifest, actual SDK
checkout status/file metadata, before/after offline helper output and focused
host test logs. Cargo's linked GitCheckout documentation explains the marker;
its presence is not treated as independent source authenticity.

## Completed marker checks

Exact source `636a2f66e2f1d34381537cc0c5f4e113b184bd24` completed
[run39370871074](https://github.com/s116821/ReMarkableBuddies/actions/runs/39370871074)
successfully through Title, Checks, Build and Integration; PR Release was skipped.
The existing Linux Python discovery explicitly passed all nine marker controls,
including symlink rejection. Its complete suite ran56 tests with three unrelated
platform/tool skips. Windows owner/reviewer eight passes and symlink privilege
skip remain separately attributed. Raw completed-job and final-run identity/logs
were retained; no duplicate workflow or test invocation was added.

[Source review5580852332](https://github.com/s116821/ReMarkableBuddies/pull/38#pullrequestreview-5580852332)
and [Docs review5580852439](https://github.com/s116821/ReMarkableBuddiesDocs/pull/25#pullrequestreview-5580852439)
accepted the functional repair without findings. This completes only metadata
marker task1.3a; broader1.3 and all package reproducibility/SDK-consuming builds,
signed negatives, production trust, release integration and physical lifecycle
tasks remain open. Normal source CI does not produce qualified signed APK input
or replace the historical r5 evidence. The active change stays unarchived.


## Isolated real-Git host fixture

Source `3f0a10a3e62f364f14225200d5eed5281103d3dc` normally integrates
main `b008027b378f8f06422c17d5e58ed7bb041e402b` and changes only test
placement and its CI invocation. Production Git admission remains unchanged.
The real-Git source method is preserved byte-for-byte in
`cicd/release/integration/test_apk_source_git.py`; the 57 ordinary host cases
remain in their original discovery stage. The additional CI stage runs that
single integration case using official Python 3.12 Bookworm, pinned to the
Linux AMD64 image digest `034c3e9d991f148d14c32ff8350286b91420baca7757d37819c7a9cc771317a0`.
Only release test code is mounted read-only. The test creates its own temporary
repository under bounded writable `/tmp`, with no network, daemon socket,
credentials or application source input. It adds no Git trust exception or configuration-loading bypass and does not
weaken ownership, raw-byte, index, mode or dirty-state assertions.

This isolates synthetic fixture prerequisites from the CI runner's ambient
Git trust configuration. Both earlier hosted failures remain attributable to
runs [41814819566](https://github.com/s116821/ReMarkableBuddies/actions/runs/41814819566)
and [41817324112](https://github.com/s116821/ReMarkableBuddies/actions/runs/41817324112);
they do not establish the configuration entry's runtime origin. Independent
discovery found one integration case and 57 host cases without import errors.
The moved case passed locally on Windows in 16.203 seconds before the
nonoverlapping main integration. Current Linux container execution and final
hosted checks remain pending. This source-test environment does not qualify
an actual SDK-consuming source build, package, signature or installation.

## November 5 delivered packaging convergence

Fresh immutable comparison finds all 25 effective paths from builder head
`3f0a10a3e62f364f14225200d5eed5281103d3dc` (19 paths) and resident extension
`221bdfa13d7482e420ee33c19e8d245e7a0c7d12` (16 overlapping/additional paths)
already absorbed into delivered main
`f6af5d1ce08c7ad518c0943d4a293e7c18688699`. Each resulting resident blob matches
main, including CI and unit-byte attributes. The normal builder merge
`429be1743314716a3ef2eaf02636d4472e203405` resolves ten add/add paths to these
delivered resident blobs; its entire tree equals main. No unique code is lost.
Retained comparison receipt SHA-256 is
`809b6126e88e1dc5c77e3b45e01c8da488b463f548c5815d2e784332a2824782`.
Docs normally integrates delivered `7121367efe6989ade78cd5a75cf57b8e88a7288a`
at `5a4666dfbe7f76cfba277b701907b0f7ecb8b0da`, preserving the six unique active
producer contract/evidence files. The drafts' history is not evidence of missing
implementation; their remaining qualification work is real and stays open.

Separate source repair `21beace6ee96fecff4ec1f491c137a2dca181f86` changes only
apk_builder.py and test_apk_source.py: reject equal/nested build/final output
roots before source/tool calls or creation. Two local controls cover three
overlap forms and the accepted sibling path. The Windows Python 3.12 APK-only
suite runs 47 cases: 43 pass, four explicit skips (three pinned-tool container
cases and the SDK symlink privilege case). It invokes no actual Cross build,
APK tool or signer. Retained APK test log SHA-256:
`34c75ce920878c1d8848969686992d3ffe060262fcb3146a97df0061bf713517`.

The initial broader Python discovery ran 60 cases: 48 passed, four skipped and
eight semantic-tool cases errored because the local semantic-release executable
was absent. That failed log is retained, SHA-256
`1679746ba184fa83d213e93f8fb3951699d0839a8345641e2eecf2d7d80d8ac2`.
No unrelated tooling or fixture policy was changed to conceal that result.
Hosted exact-successor application checks and independent review remain required;
no Rust compilation or shared Cargo cache was used. Earlier hosted run
[41823558749](https://github.com/s116821/ReMarkableBuddies/actions/runs/41823558749)
passed the original 3f0a10a source/isolated fixture; it is not this repair's CI.

[The official release proposal](official-release-proposal.md) records exact
delivered native inputs, the observed SDK tag/pin mismatch, production signer
and trust decisions, post-tag maintained release integration, complete asset
admission and Manager lifecycle gates. It is preparation only. Existing test-key
and ineligible metadata remain unchanged. No signing, remote qualification,
trust/resource/settings change, publication or tablet operation occurred. The
full producer change remains active, unsynced and unarchived pending its listed
acceptance gates. Raw local receipts/logs are retained by the maintainer without
a public download link; source identities and hosted references are public.

## Actual released SDK source adoption

Maintainer accepted the source-equivalence review before the four-line
three-file SDK adoption at Buddy
`be488154b06a546ce2c8d25d8870643dcba970e7` (parent 21beace6). Both SDK dependency
edges now select actual v0.2.0, Cargo.lock binds a0c6480, and the resident contract
requires that exact SDK commit. The native bundle hash and every test-key and
installation-ineligible field remain unchanged. Source manifests/lock were
byte-identical before and after ordinary locked metadata, matching the reviewed
patch; no Cargo package version was manually changed.

Ordinary Cargo used the existing Cargo home/cache and populated its normal
a0c6480 Git checkout from the canonical repository. No separate cache or build
target was created, and no cache ref was manually written. ARMv7 resident and
ordinary AArch64 metadata accepted both tag-selected dependency edges with their
declared default-feature opt-out, normal/dev feature sets and locked source.
Actual metadata-only helper observations have 388 and 390 graph nodes; their
normalized graph digests are respectively
`f810e8bde45d6f7f120a35532f18b92ee872562bbace02f6cfd2a22cb42ad76e`
and `0defc0737d0cc819c1f008d28acf73ae271adac9cb767fcb9e2c49de3f0b4d0a`.
The shared lock digest is
`5ae32abe822fd06668d034e09cab8559665dbb0014c6905a8e64a83974cbdaf9`.

The unchanged exact-tag helper was also invoked with v0.2.0 and refused after
metadata. Independently repeating its read-only SDK rev-parse command returned
exit 128: Cargo's checkout has no refs/tags/v0.2.0. Both checkout and Cargo Git
database retain no tag refs. With sdk_tag=None, the same helper accepts only
commit-pinned/tag=null metadata, which is recorded separately and is not tagged
qualification. The missing-ref refusal is preserved; no exact-tag logic, SDK
research files or cache refs were edited to force it through. The separate
proof-boundary proposal in official-release-proposal.md remains unimplemented
and requires maintainer review.

Current adopted-source Python APK suite: 47 cases, 43 pass/four existing explicit
skips. No compilation, actual APK tool, package generation, signing, remote
qualification or native operation ran. Earlier 21beace6/a6e5ed8d hosted results
remain attributed to those heads; successor review/CI is required. The whole
package capability remains active with exact tagged-source build, official
signing/trust/release and installed lifecycle gates open.

## Independent SDK release-source proof implementation

The maintainer accepted this boundary before implementation. Buddy
`0e5f0b13919ed5bbb92b873c8af86ff07a5dea56` (parent be488154) adds explicit
--sdk-tag-source paired with --sdk-tag, using an independent clean full Git SDK
release source. It reuses ordinary source snapshot/identity admission with only
the selected canonical repository parameterized; original Buddy checks remain.
Actual local tag object/peel and Cargo commit/manifest must match canonical
remote observations. Effective URL rewrites, malformed/duplicate/missing refs,
dirty or replaced source, manifest/commit mismatch and remote drift refuse.
The verifier only reads: it creates no tag, fetch, ref, config or cache entry.

Existing Cargo checkout/HEAD/completion-marker checks stay independent. Tagged
proof is bound into the existing graph digest and private source evidence,
compared before/after build, across targets and before completed output. Commit-
only mode remains explicitly tag=null when neither tag/proof is requested; a
requested but missing/refused proof cannot silently downgrade. The public SDK
JSON/signed tag shapes, native bundle hashes and ineligible test profile remain
unchanged. This resolves the source design defect behind the historical tagless
Cargo refusal; it does not relabel that old attempt as a success.

Current Windows Python 3.12 checks: 48 host cases (44 pass/four existing skips)
and 11 integration cases (all pass, 105.978 seconds). Integration includes ten
new actual local-Git proof controls and the original source admission regression.
The canonical remote transport is explicitly replaced by local Git only in the
fixture; real tag objects, peels, checkout/source/manifest checks and mutations
are exercised on disposable fixture repositories. Actual Cargo compilation,
network, signer, package and tablet operations are absent. The positive case
also verifies unchanged generated-cache refs/config and explicitly untagged mode.
Same-commit annotation replacement changes the bound graph identity; replacing
either the manifest inode or entire proof directory refuses. The existing fake
build boundary additionally refuses changed proof across pre/post observations.

Retained host log SHA-256
`acc88f54067acd09cf18aefa2d919380c8fa454b40e8a26829672ddf8a4ff333`;
integration log SHA-256
`82789b5a3cf6edff23f0b6602a015f804d39657a363ec1fc80b2ba46adc2d507`.
The initial eight-case development run is retained but is not counted again.
Existing CI separately discovers all integration cases in its pinned isolated
Git fixture stage. Hosted exact-successor Linux checks and independent review
remain pending, not supplied by these Windows results.

Remaining real gate: independently admit a concrete clean full SDK release
source/tag proof for the current producer and exact eligible Buddy tag, then the
separately held SDK-tagged build/package/signature/reproducibility qualification.
No proof run against the live canonical SDK remote occurred here. Production
signer/trust/release and installed lifecycle remain open; the full active change
is not synced or archived. Dirty SDK source, real Cargo cache and original refusal
receipts were untouched by this implementation/test slice. Local fixture scratch
uses its existing temporary-directory cleanup; no build cache was created.
