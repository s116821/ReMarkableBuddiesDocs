# Verification and separately gated execution

Source [Buddy PR128](https://github.com/s116821/ReMarkableBuddies/pull/128),
`785f553fc1904e60fc0880a855d81e3b86a9f358`; paired
[Docs PR139](https://github.com/s116821/ReMarkableBuddiesDocs/pull/139).

Local Windows focused input controls:6pass/2Linux skips. The real filesystem
tests cover complete frozen inputs, byte/metadata/evidence tamper, absent marker,
extra files, source/producer mismatch, disjoint external roots, preserved partial
first-target output after second-target failure and contradictory SDK metadata
before completion. A complete SDK proof must also remain identical across targets and through the fresh final proof before completion; changed tag-object proof controls pass. These use explicitly synthetic build results, not native builds.
The Linux-only controls cover symlink rejection and maintained/unknown/rootless
Cross mapping. Focused parsed-YAML gate control passes: manual-only event,
default-false execute gate, ordinary full checkout custody, no signing command,
bounded retention and no direct input interpolation into shell text.

The broader local Python suite reports68tests with8errors/6skips: all8errors are
semantic-tool fixtures unable to spawn the absent `semantic-release` executable.
The broader Node workflow suite passes11of12; its sole error is absent `jq` in
an existing body-only predicate fixture. Preserve these failures; they are not
passing hosted checks. No global tool installation or weakened assertion was
used. These preserved local failures are distinct from the completed hosted checks.

Normal exact-head [CI42132317733](https://github.com/s116821/ReMarkableBuddies/actions/runs/42132317733)
passes PR Title, Checks, application Build and Integration; Release is correctly
skipped for a PR. Linux executes all8new Python controls, including the2Windows
skips; full Python suite69tests passes with3existing skips. Parsed workflow
controls, the broader Node fixtures, host Rust tests and strict Clippy pass.
The retained raw Checks log has SHA256
`4fbb609fd96e8bb84df21f4524c460325177442fbd424572ca9a621a82451bd4`.
This normal application CI does not execute the new strict manual qualification.

Root independently accepted source785f553 with Docs e1ba99de after reviewing the
complete helper/YAML/tests/spec/operator plan and actual maintained Cross/Rust
action behavior. Canonical package-build-inputs requirements are synced; this
finite source-interface change is archived in the same paired delivery. Final
Docs checks qualify the archive revision. Root owns final paired merge and actual
main/release verification. Full packaging task3.3 remains open.

## Actual execution plan to review separately

1. Select the final reviewed producer workflow commit and exact published stable
   Buddy tag/full commit. The retained candidate source is v0.63.2/0747f861; using
   it later is an explicit selection, not automatic authority from earlier proofs.
2. Review the committed manual workflow and action/Cross/image pins. Normal owned
   full Linux checkouts disable safe-directory accommodation at creation. The SDK
   source stays v0.2.0/a0c6480. No existing Windows probe or held packet is replayed.
3. Only after separate coordinator selection, manually dispatch with execute_build
   true and those exact source inputs. Default false and normal PR events do not
   perform this operation. The current implementation has NOT been dispatched.
4. Observe the existing strict producer's actual source/SDK/compiler/container/
   descriptor/runtime pre/post results and exclusive final completion. Stop at
   first failure and preserve bounded diagnostics. There is no automatic retry.
5. Retain the exact completed finite artifact and public workflow/run identity for
   review14days. Build caches/intermediates remain ephemeral; no self-hosted or
   held cleanup. Reverify full input hashes before any separately selected consumer.

No APK/private key/signing/trust/resource/settings/install/device step is selected.
Existing normal release tarballs retain their original weaker evidence; no metadata
is invented for them. This finite source interface does not settle actual build
qualification, authenticated artifact provenance or full packaging task3.3.

Source basis: current implementation/parsed workflow, actual local test logs and
directly reviewed maintained Cross source, exact-head hosted CI outputs and
independent Root source review. New strict remote qualification remains prospective.
