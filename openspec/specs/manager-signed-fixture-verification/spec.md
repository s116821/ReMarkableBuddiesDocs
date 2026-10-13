# Manager original signed test-fixture verification

## Purpose

Describe the completed bounded public-key-only host observation of original historical Buddy test artifacts. It grants no production, native or installation eligibility. Implementation is paired with Manager PR14; independent review5504317404 accepts source10263 and central contract6f4.

## Requirements

### Requirement: Independently pinned public fixture inputs
The consumer SHALL accept only the six regular public handoff files for the two-target legacy-no-sdk test fixture, validate bounded original sizes/digests against a separately supplied manifest digest, and validate the public PEM's actual DER-SPKI digest against a separately supplied generation-control pin. It SHALL validate exact-source apk binary/archive/build receipt identity and immutable runtime identity. Adjacent files SHALL NOT establish production trust.

#### Scenario: Original fixture or changed trust input
- **WHEN** original files and independently communicated pins match
- **THEN** observation may proceed as host-only test-fixture evidence.
- **WHEN** a pin, file digest, inventory or source-tool identity differs
- **THEN** admission refuses without device, signing or installation operations.

### Requirement: Actual offline read-only signature and payload verification
The consumer SHALL use the pinned actual apk tool only for verify and bounded JSON adbdump under isolated explicit roots and keys, network disabled and read-only observation mounts. It SHALL preserve inventory/content/modes/links for originals and isolated roots across each operation, use nonroot effective-owner binding and bounded execution/output with owned timeout cleanup, and never extract or execute payloads or use trust bypass flags/Vellum wrapper.

#### Scenario: Original and altered artifact observations
- **WHEN** both original APKs and original index use the independently pinned public key
- **THEN** actual verification succeeds and bounded metadata readback corresponds to the fixture source/tag/pkgrel/target/file inventory and authenticated index.
- **WHEN** explicit wrong keys or altered signed control/index/payload copies are observed
- **THEN** actual single-input verification refuses with recognized signature/integrity classification; crash, timeout or usage error fails the test.

### Requirement: Fixture evidence never grants installation eligibility
The report SHALL distinguish actual host verification from reported producer build/runtime and saved index comparison, retain full package versions and source identity without maintaining project source versions, and keep update/install eligibility false. It SHALL distinguish signed metadata hashes from complete-file SHA256 and SHALL NOT claim independent index regeneration or production/compiler/SDK/native/lifecycle/source-equivalence qualification.

#### Scenario: Successful report
- **WHEN** all focused actual-byte checks pass
- **THEN** results remain public-key-only test-fixture evidence and accepted Manager ZIP behavior, device state, production keys and release behavior remain unchanged.
