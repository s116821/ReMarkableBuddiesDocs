## ADDED Requirements

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
