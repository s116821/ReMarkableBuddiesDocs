# Finite current fixture extension

## Reuse and ownership
Use the existing observer/admission/metadata functions and test module; no second
verifier, compiler, release engine or renderer/host service. Actual source base is
Manager2c61579270d0478c74d6e6f76390b962f87bee9f; central Docs87baf6b. The existing
recovery draft has no tests/vellum consumer overlap and stays with its owner.
Historical canonical contract and archived original outcomes remain intact.

## Handoff and immutable originals
Legacy invocation keeps its adjacent six-file manifest and32MiB APK cap. A new
explicit optional external-manifest input selects schema2/current-resident-fixture;
never infer the profile from adjacent files. Independently supplied manifestSHA
and generation DER-SPKI remain required. The new original root contains exactly
two APKs, index, fixture.pub and completed receipt; no manifest or derived bytes
are written there. External manifest is regular/ancestor-safe, bounded16KiB and
rehashed across the operation. No APK copies are needed before an actual selected
negative-control operation. Input receipt/artifact bytes stay independently pinned.

New fixture APK cap is64MiB each (total128MiB), receipt64KiB and external manifest
16KiB; legacy limits do not change. Unknown profile/fields/members, absent/extra
files, alias/symlink/nonregular, changed byte/size/manifest or cross-source identity
refuse. Runtime/readback/control-copy budgets must account for this finite bound;
no arbitrary size override is introduced.

## Finite signed metadata and payload
Manifest supplies separately reviewed canonical per-target build metadata and
expected payload pins. Canonical build JSON bytes must hash to each signed metadata
file entry, and source/tag/epoch/arch/ABI/pkgrel0, binary hash, profile and SDK fields
must agree across manifest, receipt, signed tags and authenticated index. Preserve
actual package/index metadata-hash versus complete-file-SHA distinction. Metadata
from the developer producer is reported provenance, never compiler attestation.

ARMv7 profile is only rm2-resident-test-key, device rm2, firmware3.28.0.172 and
remarkable-os=3.28.0.172-r0/rm2 dependencies, fixed consumed SDK source/bundle pins
from the accepted fixture. Its exact ten paths are:
- home/root/.local/lib/remarkable-buddies/{Dobby-LICENSE,OpenSDK-LICENSE,libremarkable-resident.so,reader-buddy,resident-profile.json,resident-recovery.json}
- usr/lib/systemd/system/{reader-buddy-stock-recovery.service,reader-buddy.service}
- usr/share/remarkable-buddies/{LICENSE,build.json}

No glob or manifest-declared extra path is admissible: expand those names to a
finite literal table. Modes come from the existing reviewed payload policy, with
root/root ownership, exact epoch and directory set. AArch64 remains the three
ordinary usr/bin/reader-buddy + LICENSE/build.json files, SDK-bound unqualified-
development, with no fabricated resident capability/dependency. No scripts,
triggers, symlinks, devices or unknown signed metadata are admitted.

Keep canonical source SDK/bundle/feature relationships finite and explicit; do not
copy the producer compiler/private-proof engine into Manager. No imported helper
from an arbitrary manifest/source path and no execution of downloaded code.

## Public-only operation and refusal controls
Reuse exact-source apk receipt/archive417-entry identity and immutable runtime
checks, existing nonroot effective-owner binds, bounded no-network readonly
verify/adbdump calls, original/root snapshots and timeout cleanup. Keep wrong-key,
missing-key, changed signed control/index/payload controls, recognized signature/
integrity failures and no crash/timeout/usage-error-as-success. No mkpkg/mkndx,
key generation, payload extraction/execution, package-manager mutation or tablet.
Actual-tool observation requires separate selection; pure owned schema/metadata/
filesystem controls do not claim cryptographic/native success.

## Limits
No production signer/trust/publication, stable asset eligibility, GUI downloads,
package installation, runtime profile enablement, service/Stop/recovery change,
SDK/native support or actual source-switching qualification. Legacy output stays
unchanged; new report is explicitly current fixture/public-key-only and installation-
ineligible. One retained final fixture remains owned by the package lane until
consumer handoff; no new large output tree or duplicate signing trial.
