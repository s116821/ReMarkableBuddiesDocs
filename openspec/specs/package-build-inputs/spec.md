# Strict hosted package build inputs

## Purpose

Expose the existing strict source-build phase as finite frozen inputs before APK generation. Actual remote qualification, signing/trust and device lifecycle remain separately selected work.

## Requirements

### Requirement: Strict build-only completion
The producer SHALL expose its existing strict tagged build phase independently
of APK generation. It SHALL require real source/SDK bindings and preserve existing
ordinary ownership/Git/raw-byte/compiler/runtime/pre-post checks. It SHALL publish
frozen binaries, canonical per-target metadata and retained evidence with a final
exclusive completion manifest only after both targets validate. No install or
signing authority SHALL follow.

#### Scenario: Both target builds complete
- **WHEN** original strict ARMv7 resident and AArch64 ordinary builds pass
- **THEN** exact output hashes and original source/SDK/profile identities are verified before the final completion marker

#### Scenario: Interrupted or changed input bundle
- **WHEN** a build fails, completion is absent, metadata contradicts expected identity or any output is missing, extra or changed
- **THEN** the operation refuses completion and preserves bounded diagnostics without signing or silently retrying

### Requirement: Explicit maintained workflow execution
Hosted build-input qualification SHALL use a default-off manual workflow over
normally owned full source/SDK checkouts, without source ownership or Git
configuration exceptions. Existing maintained toolchain/action/image primitives
SHALL be reused, and no automatic release or ordinary PR event SHALL dispatch it.

#### Scenario: Source delivery or ordinary PR check
- **WHEN** this implementation is pushed, reviewed or tested normally
- **THEN** no remote build-input qualification, APK/signing or device operation is dispatched

#### Scenario: Later explicitly selected build
- **WHEN** the manual gate is deliberately enabled with the exact reviewed source/tag plan
- **THEN** the workflow runs only the strict build-input phase with finite timeout, bounded diagnostics and documented ephemeral/retained outputs
