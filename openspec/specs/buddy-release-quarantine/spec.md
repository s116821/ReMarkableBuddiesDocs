# Bounded official Buddy release quarantine

## Purpose

Describe fixed-repository source/tag and original-byte verification in a new
local quarantine directory. Receipt completion does not establish signing trust,
SDK or device compatibility, APK installation or payload execution authority.

## Requirements

### Requirement: Actual release bytes are verified against fixed trusted publication
The host consumer SHALL validate an explicitly selected stable annotated Buddy tag and exact canonical release/completion/provenance/server digests, then stream and hash bounded original asset bytes into a new quarantine directory.

#### Scenario: Complete current publication
- **WHEN** tag, release, manifest and all actual asset bytes agree before and after download
- **THEN** quarantine retains exact bytes and a bounded successful receipt without extraction or execution

#### Scenario: Corruption or publication drift
- **WHEN** bytes are missing, truncated, altered, oversized or publication/tag identity changes
- **THEN** no successful receipt is published and existing user data is not overwritten or deleted

### Requirement: Current tarballs never grant APK installation eligibility
The consumer SHALL classify current target tarballs as noninstallable via Vellum even when hashes match and SHALL not substitute metadata for signed APK/trust/SDK/compatibility/lifecycle qualification.

#### Scenario: Verified legacy archive
- **WHEN** current tarball bytes verify
- **THEN** APK eligibility remains false and no payload, script, installer, device or package mutation runs

### Requirement: Boundaries and explicit refusal
The consumer SHALL use fixed public API/asset inputs, bound redirects/network/file bytes, sanitize errors and refuse unsafe or existing destinations.

#### Scenario: Invalid remote or local input
- **WHEN** input selects an unsupported tag, foreign endpoint, untrusted redirect or unsafe destination
- **THEN** the consumer refuses without arbitrary command, path overwrite, secret lookup or key enrollment

#### Scenario: Cancellation or deadline during final directory validation
- **WHEN** cancellation or the operation deadline is observed after the final awaited directory validation and before the atomic completion link is issued
- **THEN** no successful receipt is published

#### Scenario: Cancellation after atomic completion issuance
- **WHEN** cancellation arrives after the atomic link request has been issued
- **THEN** a successful link remains committed success and a failed link refuses, without claiming that the in-flight filesystem request can be preempted
