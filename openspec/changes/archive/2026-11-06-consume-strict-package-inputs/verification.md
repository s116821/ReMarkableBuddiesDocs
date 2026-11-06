# Bounded source verification

## Historical/current correction

This change is reopened within the same paired Buddy PR132/Docs PR144 after
read-only preflight found exactly a historical SDK `.git` ctime difference. The
initial source/tests below remain evidence for their exact revision. No package
invocation occurred. The correction was specified in reopened active artifacts
before implementation, then verified, synced and archived in this same delivery.

The SDK source observer, strict verifier, builder/generator/observer, tool/image/
bundle pins and owned isolation are byte-identical to the initial implementation.
Only consumer logic, host controls and operator documentation changed. The new
classification preserves both complete proofs and explicit ctime difference,
while typed current-operation proof equality stays strict. Structured path
components prevent a dictionary key from impersonating the classified leaf.

The APK host suite passes 67 tests with 3 existing explicit-container skips
(64 executed), including 11 focused consumer controls with parameterized cases.
An actual consumer fixture with only historical Git ctime changed reaches both
mocked phases, retains full old/current proof and bound correspondence evidence,
preserves every original byte and calls no build function. Equal proofs remain
accepted with tuple/list normalization. Every other location/source/tag/remote/
manifest/raw/conversion identity, unknown/missing field, type, list/shape and
second-difference case refuses before generation. Cross-target integer/boolean/
float alias controls refuse. Git ctime changes at each of four later boundaries
and changed private correspondence evidence refuse without completion.

A separate actual read-only source preflight observes the original retained SDK
proof and a fresh proof through the unchanged observer. The classifier reports
only the previously recorded Git ctime leaf as
`historical-git-ctime-only-revalidated`; the current observation remains internally
stable. This is source/classification evidence, not package, signing or device
execution. The first failed preflight remains preserved unchanged.

The corrected canonical spec is synced within this delivery. Final strict spec,
Docs and preservation checks are retained with the source handoff. Hosted full
checks and independent review remain delivery gates; actual package/signing and
device operations remain separately selected. No target build was repeated.

## Initial source evidence

Paired implementation is Buddy's `feature/rem-41-consume-strict-package-inputs`
branch, based on delivered main `4ec94a6b162a6f00959f5bf6518dd4835bd0ec7b`.
This central change starts at Docs `b0370dab33efc28349df337ff235db59d0677c15`.
The maintainer links exact final revisions and PRs during coordinated publication.

Six focused host tests pass, including parameterized refusal controls: independently
pinned completion, canonical exact inventory/hash checks, source/license/raw-file
identity and full SDK proof correspondence, original producer vs new executor,
exact binary/build metadata staging, unchanged legacy two-build CLI delegation,
no consumer build calls, generation/observation failures, between-phase changes,
private-key observation refusal and mutation during final copies without completion.
All external phase/tool/source observations in these controls are mocked over
owned synthetic files; these are not actual signature or device observations.

The complete APK host suite passes 62 tests with 3 existing explicit-container
skips. Docs unit tests pass 12 tests; current-guidance/126 preserved-source checks
pass. Strict OpenSpec change validation passes before sync/archive; final complete
spec validation is recorded with the source handoff. The shared tail retains the
original image/tool/bundle pins, resource/mount arguments, 120-second bounds,
owned cleanup, generation-control SPKI and separate public-key-only observation.

The broader release suite initially ran 73 tests with 9 environment errors and
3 skips: metadata setup cannot find `cargo` on PATH and eight existing semantic
tool controls cannot find `semantic-release`. Preserve this failed run separately;
it is not a passing full release check. No global tool/configuration adjustment
or weakened assertion was used. Normal hosted full checks remain delivery gates.

The canonical package-build-inputs spec is synced and this bounded source change
is archived within the paired delivery. Actual APK/signing/key/container execution,
production trust, release/install and native qualification are separate future
operations, not completed or authorized by these source tests. Original successful
producer inputs, metadata, SDK/source checkouts and their evidence remain unchanged.

Source basis: current code/spec comparison and actual host test/validation logs;
no hardware, real signing, compiler rerun or production eligibility is inferred.
