# Bounded Manager release bundle verification

## Purpose

Describe fixed-release original-byte and bounded ZIP metadata verification by a
trusted source-checkout tool. Embedded identity is not compiler, signing, native
compatibility, payload safety or installation/update authority.

## Requirements

### Requirement: Verify real Manager release bytes and embedded identity
The manual host consumer SHALL bind an explicitly selected stable canonical annotated Manager tag and peeled source to the exact current release/completion/provenance/server digests, actual downloaded ZIP bytes and bounded embedded build-info identity.

#### Scenario: Complete current Manager publication
- **WHEN** all actual downloaded bytes, source records and embedded declarations agree before and after observation
- **THEN** a new quarantine retains original bytes with a successful noninstalling receipt

#### Scenario: Wrong or incomplete publication
- **WHEN** repository, tag, source, assets, digest or embedded identity is missing, malformed or contradictory
- **THEN** no completion receipt is published and user files are not overwritten or deleted

### Requirement: Bound archive and process observation without activation
The consumer SHALL bound ZIP structure/metadata/member decompression and its trusted fixed verification process, execute no package payload, extract no app file and refuse unknown update/installation eligibility.

#### Scenario: Unsafe archive or process result
- **WHEN** ZIP input exceeds qualified bounds or contains unsupported/unsafe metadata, or the verifier fails, stalls or is cancelled
- **THEN** the consumer refuses with sanitized status and no successful completion or payload action

#### Scenario: Cancellation at completion boundary
- **WHEN** cancellation/deadline is observed after final awaited validation before atomic receipt issuance
- **THEN** completion refuses, while an already-issued successful atomic link remains committed without a preemption/rollback claim
