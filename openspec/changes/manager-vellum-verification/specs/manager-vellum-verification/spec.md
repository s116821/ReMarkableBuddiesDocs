## ADDED Requirements

### Requirement: Verification uses actual pinned upstream apk tooling
The qualification harness SHALL invoke a separately supplied exact-source upstream apk tool with recorded source/build/binary identity and an explicit test trust-key set. It SHALL NOT vendor the GPL implementation, substitute a handwritten verifier or invoke Vellum CLI. Source: REM-41 signed local APK authority and released CLI/apk source inspection.

#### Scenario: Untrusted or altered signed bytes
- **WHEN** a signed synthetic APK/index has a missing/wrong verification key or modified signed control/payload bytes
- **THEN** actual apk verification returns the pinned single-input refusal status and a recognized trust/signature/integrity classification; crash, timeout and generic usage failure do not pass the case.

#### Scenario: Authentic fixture
- **WHEN** unchanged fixture bytes are verified against their explicitly trusted ephemeral signing key
- **THEN** actual apk verification succeeds without untrusted/signature-bypass flags.

### Requirement: Offline read operations preserve isolated roots
The harness SHALL restrict all paths/configuration/key lookups to unique checked fixture roots, disable networking, bound command duration and assert inventories/content/modes/symlinks remain unchanged across every observation. It SHALL NOT invoke bootstrap, package installation/deletion/upgrades or use host `/` as payload install root. Source: REM-41 wired/ownership safeguards and CLI mutation-before-parse finding.

#### Scenario: Observation succeeds or refuses
- **WHEN** verification/query/version/ownership completes successfully or with an expected refusal
- **THEN** fixture root snapshots remain identical and no device or real Vellum state is touched.

### Requirement: Full package metadata remains separate from product qualification
The harness SHALL compare full apk versions including pkgrel using actual apk and observe full version, architecture, source-commit, source-package origin, dependencies, script type names, installed/broken-script status and file ownership from an explicitly seeded synthetic database/scripts archive. It SHALL verify script sentinels never execute. It SHALL distinguish source-package origin from distribution source and SHALL NOT claim signature fixture success, seeded metadata or equal SemVer proves real Buddy provenance, installation, source equivalence or model/firmware/SDK compatibility. Source: REM-41/42 one-owner and version authority; apk query/package/version documentation and pinned query/database source.

#### Scenario: Packaging revisions differ
- **WHEN** fixture versions share application version but differ in `-rN`
- **THEN** actual apk revision ordering is retained without minting or changing a project Git-tag version.

#### Scenario: Fixture validation completes
- **WHEN** all offline fixture cases pass
- **THEN** Manager installation remains unavailable until real signed official artifacts, consumed SDK provenance, wired identity, ownership, lifecycle recovery and supported-device compatibility are qualified separately.
