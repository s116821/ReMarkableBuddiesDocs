## ADDED Requirements

### Requirement: Explicit bounded saved-file inspection
The producer SHALL expose one fixed explicit inspect operation over an existing absolute configuration selected by REMARKABLE_BUDDIES_CONFIG, without stdin, default-file fallback, declared-root probes, Store/provider/runtime initialization or writes. It SHALL enforce the exact caps, strict parsing and sanitized whole-view refusal in contract.md.

#### Scenario: Valid saved file
- **WHEN** the explicit bounded regular file has supported strict typed declarations
- **THEN** one bounded complete snapshot is emitted without reading declared roots, credentials, environment overrides or stdin.

#### Scenario: Invalid or unavailable file
- **WHEN** selection, read, schema, duplicate, type, value or bound admission fails
- **THEN** the exact sanitized refusal has null snapshot and no fallback or side effect.

### Requirement: Allowlisted saved declarations and origins
The producer SHALL return only the exact contract.md scalar/presence allowlist and declared/default/declared-null origins from the same raw typed read. Arbitrary text, endpoints, paths, credential references, private selection identities and personalization text SHALL remain absent. Saved bytes/value validation SHALL NOT imply effective runtime state, root admission, reload or write authority; unsupported settings SHALL remain explicit.

#### Scenario: Omitted and null leaves
- **WHEN** a supported Option is omitted versus explicitly null or a nested leaf defaults
- **THEN** its value projection follows existing typed defaults while its exact origin remains distinct.

#### Scenario: Credential-like saved strings
- **WHEN** a valid model/endpoint/path/reference/text/identity contains a sentinel
- **THEN** only its allowed presence/length summary appears and no sentinel or raw error reaches either report logs or renderer.

### Requirement: Shared session-bound companion inspection
Both browser and Electron SHALL consume the strict reduced view through fixed existing host adapters with private raw digest removal, explicit inspection, bounded cancellation and same-target observation generations. External maintenance SHALL invalidate prepared forget host state before I/O. No edit, test-provider, service or reload capability follows.

#### Scenario: Old result after explicit refresh
- **WHEN** refresh/cancellation/disconnect occurs even with unchanged connection and boot IDs
- **THEN** old results cannot repopulate the cleared view or preserve an actionable stale prepared-forget reference.

#### Scenario: Refused or unsupported response
- **WHEN** a producer or transport refuses, truncates, times out or returns unsupported/unknown data
- **THEN** both companions preserve the truthful status with no invented default snapshot, automatic retry or file fallback.
