# Resident fixture observer source verification

## Scope and evidence

This is the source implementation of the previously reviewed finite observer
contract, extending existing Manager tests/vellum/real_fixture.py and its test
module/guide. The source baseline is Manager
2c61579270d0478c74d6e6f76390b962f87bee9f. Precode was accepted at Docs
4a4a60b3c9a7b58abc5b910f75f21afed76141f8; the source delivery normally merges
Docs main 2720aad9373464771f47fbbeb9d5d5bbbbb6a27d before canonical sync.
Exact resulting heads and paired merge order belong in the delivery comments.

Local Linux command:
`python3 -B -m unittest discover -s tests/vellum -p 'test_*.py' -v`.
All 35 tests passed on 2026-11-06. These use tiny owned synthetic metadata,
files and fake ELF inputs plus existing owned subprocess output/timeout guards.
No Docker/APK invocation, signing, package generation, payload execution,
large-artifact copy, provider or tablet contact occurred.

The retained small declared ARMv7/AArch64 build.json records also pass
current_build against the retained producer receipt (ten/three finite paths).
This read-only metadata check neither reads APK payloads nor verifies signatures.

Docs verification: 12 tests pass; guidance/manifest and 126 preserved source blobs
verify; OpenSpec 1.2.0 named validation passed before archive and all 119 active
spec/change items pass strict validation after explicit canonical sync/archive.
The CLI was invoked from its existing local installation because it was not on
the shell PATH; no dependency was installed.

## Requirement correspondence

- Independently pinned inputs: explicit external schema2 selection; exact five-file
  current inventory and unchanged adjacent legacy default; digest/size/profile/
  authority/source guards, safe external path and bounded per-command rechecks.
- Finite metadata: both target positives; exact ten resident/three ordinary paths,
  canonical declared build hash, SDK/features/ABI/source/profile/dependencies,
  modes/ownership/time/index and payload correspondence. Repinned nested-type
  faults and integer/float aliases refuse rather than comparing equal.
- Bounded operation: existing isolated read-only nonroot verify/adbdump, source
  and runtime identity, snapshots and cleanup reused. Pure controls cover both
  separately hash-identified resident executable/library corruptions, control/
  index mutations and the complete six-case current negative schedule. Legacy
  four-case schedule remains. This is source evidence, not a real refusal result.

The earlier test-development failure expected FileNotFoundError for an absent
legacy manifest; the existing regular-file guard raises ValueError. The test
expectation was corrected and subsequent full suites pass. The final portability
edits use PurePosixPath for signed package paths and canonical temporary host
paths; both are included in the final 35-test pass.

## Remaining delivery and operation gates

Independent review accepted the precode contract; independent implementation
review and current hosted CI are still required before coordinated merge.
Deliver Manager source and central Docs as one paired change: publish exact
heads, run required current CI, resolve review findings, then coordinate squash
merges and verify actual main/release outcomes. No hosted CI or merge pass is
claimed by this local source evidence.

Actual opt-in current-fixture observation is explicitly UNQUALIFIED and UNRUN.
It needs its own selected execution, bounded temporary-copy/runtime plan and
actual result/cleanup evidence. Producer observations and these pure tests do
not substitute for it. The original accepted public fixture remains unchanged.
No installation/update eligibility, production signing trust, native firmware/
model compatibility, runtime enablement, service/Stop/recovery changes or broad
installer completion follows from this source archive.
