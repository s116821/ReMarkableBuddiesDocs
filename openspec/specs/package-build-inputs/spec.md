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

### Requirement: Explicit strict receipt consumption
The packaging-only consumer SHALL accept an independently supplied completion
digest and original producer identity, call the strict input verifier without
weakening its canonical inventory/hash/profile/source/SDK checks, and stage the
original binary and build metadata bytes without rebuilding. It SHALL recheck the
actual full release source/license and every field of the independent retained
SDK proof. Tuple/list JSON normalization SHALL NOT discard identity fields.
Original build producer and packaging executor revisions SHALL remain distinct.

#### Scenario: Accepted frozen input bundle
- **WHEN** externally pinned completion, all actual input bytes and original producer/source/SDK identities agree
- **THEN** packaging stages checked original bytes without calling a compiler or target runtime

#### Scenario: Changed or substituted input
- **WHEN** completion, inventory, bytes, source/license, producer, SDK proof, tool or required resident bundle differs
- **THEN** admission refuses before generation, without rebuilding, rewriting metadata or substituting inputs

### Requirement: Shared bounded test-key packaging
The consumer SHALL reuse the original builder's generation and separate
public-key-only observation stages with unchanged tool/image/bundle pins,
isolation, timeouts, owned cleanup and generation-control SPKI channel. Source,
receipt/proof and staged inputs SHALL be rechecked across operation boundaries.
Only a successful complete observation SHALL publish an exclusive final receipt
bound to accepted build inputs and packaging executor, with not-qualified status.
The original build-based CLI SHALL retain its existing behavior.

#### Scenario: Both packaging phases succeed
- **WHEN** generation completes, its ephemeral private key is disposed and owned container absence confirmed, then separate public-key-only observation succeeds
- **THEN** only checked actual artifacts and the final not-qualified completion are retained without exporting a private key or granting installation authority

#### Scenario: Refusal, failure or changed inputs
- **WHEN** generation or observation fails or any admitted input/proof changes before completion
- **THEN** no completion receipt is published, useful diagnostics remain and no retry or trust bypass occurs
