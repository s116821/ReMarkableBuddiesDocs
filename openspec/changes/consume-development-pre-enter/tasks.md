## 1. Precode and independent review

- [x] Reconcile delivered Buddy/central Docs and the paired SDK/native contracts.
- [x] Specify closed consumer, raw-unit/deadline/admission limits and isolated build recipe.
- [x] Specify ordinary all-features compatibility and explicit official-build refusal.
- [x] Validate named precode with cached OpenSpec 1.2.0 strict validation.
- [x] Publish this exact precode and record strict validation and full revision.
- [x] Obtain independent precode acceptance before consumer implementation/build.

## 2. Consumer implementation after acceptance

- [x] Add only the gated ReadOnlyRequest arm, ResidentConnection method and dispatch.
- [x] Register the build-only cfg, track selection inputs and reject supplied cfg with any official identity channel or exact official semantic tag.
- [x] Preserve original request_read_only deadline, progress, pre/post owner/companion checks, retention errors and no-retry outcome.
- [x] Keep raw u16 results and typed refusal/empty distinctions; no composer or mutation authority.
- [x] Document command-local SDK patch, isolated original/developer lock and target/metadata recipe without changing ordinary pins/config/release validation.

## 3. Focused source/build verification after acceptance

- [x] Ordinary pinned SDK all-features test/Clippy remains valid with cfg absent; cfg registration alone exposes no new arm.
- [x] Actual supplied cfg refuses each release/candidate identity channel alone or paired, empty/malformed/mixed values, and exact official semantic HEAD tags without identity variables; unavailable required Git identity also refuses.
- [x] Demonstrate exact reviewed developer SDK path patch and one generated developer lock, then unchanged --locked metadata/check/build; refuse unused/dirty/duplicate/wrong SDK, unexpected features, changed lock or lost cfg pairing.
- [x] Exercise the real closed path for count0/4096 and boundary overflow, copied raw units including NUL/separator/isolated surrogate, successful empty versus refusal, Unsupported/Capacity, and wrong type/count/source correlation.
- [x] Exercise expired original deadline, progress/admission loss before/after reply and retention failure; assert no deadline renewal, false success or replay/rearm.
- [x] Preserve Native's marker ownership; fixtures do not emit an arming marker or model input. Document separately gated designated-input admission without weakening health/owner/recovery checks or inventing physical-input capability. Actual input/marker qualification remains outside this consumer increment.
- [x] Run applicable required checks once for the actual implementation revision; retain exact source/flags/locks/metadata/artifact evidence and ordinary/native limitations.

## 4. Coordinated completion

- [x] Keep any eventual current execution packet separately gated after independent source/build review; source tests do not authorize device/provider work. No execution packet is selected by this consumer increment.
- [ ] Link exact Docs/Buddy revisions and Native dependency, resolve review findings and applicable CI; keep native-qualification gaps explicit.
- [x] Sync the implemented canonical consumer spec and preserve unrelated contracts.
- [ ] Archive this change only when its selected implementation/verification obligations are complete in the coordinated Docs/Buddy delivery.

## Evidence and remaining authority

Published consumer source: [Buddy PR 138](https://github.com/s116821/ReMarkableBuddies/pull/138)
at `9ee80d8d5c9e540ba6c06884da11f8ef511dcfcf`, based on delivered
`bafa5cc92c175b1319939265c6da5928315cd8bc`. Ordinary manifest, lock, CI and release
validation are unchanged. All twelve published source blobs match the independently
reviewed local implementation. Validation evidence and remaining limits are recorded
in the paired PR discussion. Hosted CI, canonical sync and archival remain open.
No SDK/native shim rebuild, tablet action, provider call or stock qualification
is included. The separate REM-61 native experiment remains unqualified.

Local validation used source-identical commit
`b72eb0391d528a9c0e512b496fb42d6ddf8e6141`: ordinary formatting,
`cargo test --locked --all-features` and
`cargo clippy --locked --all-targets --all-features -- -D warnings` passed with
the original lock and SDK. The library suite reported 975 passed and 35 ignored;
integration and doc suites passed. Developer tests passed all four groups and
the library build passed with the frozen developer lock. Actual final-target-only
`cargo rustc` library and binary selections refused. Missing SDK features and the
wrong `--locked` lock refused. Three compiled build-script regression groups,
effective flag selection and seven negative metadata cases passed. Original
locks were restored. These results cover the consumer source, not native input
or stock execution; hosted CI separately verifies the published revision.
