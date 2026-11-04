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
