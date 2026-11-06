# Portable preference artifacts

## Purpose

Explicit private V1 export and offline inspection for the three supported saved preference declarations. See the [wire contract](../../changes/archive/2026-11-06-export-portable-configuration/contract.md). Import/application, archive/sync integration and broader portable domains remain separate.

## Requirements

### Requirement: Explicit allowlisted preference export
The backend SHALL expose an explicit read-only export from an existing absolute saved configuration file, validating the complete duplicate-free typed source before projecting only product_settings, personalization and research_policy into a strict version1 portable artifact. It SHALL preserve raw declaration absence, sparse fields, supported null and exact bounded personalization text without materializing defaults. Other settings and device/account/runtime bindings SHALL be excluded.

#### Scenario: Private preferences with excluded bindings
- **WHEN** a valid saved configuration contains portable preferences and device-specific settings
- **THEN** export emits only the declared allowlisted preferences with exact text and declaration semantics, leaves source bytes unchanged and performs no root/credential/provider/runtime initialization.

#### Scenario: Unsupported or invalid source
- **WHEN** the source has unsupported schemas, repeated/unknown members, invalid values or unsafe/unavailable file input
- **THEN** export returns a bounded sanitized refusal without emitting a partial artifact or creating a Store.

### Requirement: Offline portable artifact inspection
The backend SHALL validate the complete bounded artifact offline with exact version/root/settings allowlists and existing preference semantics. It SHALL return sanitized content digest/count information without echoing text, importing preferences, granting runtime authority or admitting archive/sync integration.

#### Scenario: Artifact roundtrip
- **WHEN** the exported artifact is inspected as an independent regular file
- **THEN** inspection validates the same preference declarations and compact artifact digest without runtime configuration, directories, credentials or mutations.

#### Scenario: Unknown or corrupt artifact
- **WHEN** the artifact includes an incompatible version, duplicate/unknown member, invalid preference, excluded binding or exceeds its bound
- **THEN** whole inspection refuses rather than dropping fields, accepting a prefix or reporting empty success.

### Requirement: Bounded explicit input and consuming output
Both selectors SHALL be exclusive before normal startup, require explicit absolute regular-file input, read no stdin and emit at most128KiB including newline through one write/flush. Only export success SHALL include the private artifact. I/O failure SHALL NOT append a replacement frame, retry or claim persisted/runtime activation. Existing configuration and archive interfaces SHALL retain their behavior.

#### Scenario: Output uncertainty
- **WHEN** a writer accepts a prefix or flush fails
- **THEN** the command returns a fixed output failure without another frame or operation and the source remains unchanged.
