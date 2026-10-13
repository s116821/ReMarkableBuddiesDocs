## ADDED Requirements

### Requirement: Signed exact-source Buddy package artifacts

The Buddy producer SHALL create actual signed APKv3 artifacts with one permanent
package identity, tag-derived version and separate pkgrel. It SHALL authenticate
exact payload/source/consumed-SDK/target identity in verified signed standard
metadata and SHALL distinguish build data from qualified installation eligibility.
It SHALL NOT infer trust from a sidecar key, fabricate an SDK tag, install an SDK
runtime separately, or introduce custom release/version/publication logic.

#### Scenario: Checked test package

- **WHEN** an actual checked exact-tag executable and build inputs are packaged with an isolated explicitly pinned fixture signer
- **THEN** the real package/index verify and their bounded metadata agrees with source/version/SDK/target inputs
- **AND** test-key or unqualified profile artifacts remain ineligible for installation.

#### Scenario: Wrong or incomplete identity

- **WHEN** tag/source/payload/SDK/target metadata or artifact inventory disagrees, or required production SDK-tag/trust/compatibility is absent
- **THEN** packaging verification refuses the conflict or reports the explicit ineligible state
- **AND** it does not invent missing identity or overwrite an earlier artifact.

#### Scenario: Signature and reproducibility

- **WHEN** signed control/payload changes, the key is wrong/missing, or identical fixed inputs/key are rebuilt
- **THEN** actual trusted-tool verification refuses altered/untrusted bytes and accepts only matching signed identity
- **AND** identical deterministic builds yield the same artifact bytes without executing package scripts.

#### Scenario: Deferred installation and release rollout

- **WHEN** only host package build/sign/verification has completed
- **THEN** production key enrollment, device/Vellum compatibility, lifecycle, source handoff and maintained release rollout remain open
- **AND** no tablet, service, public catalog, production tag/asset or repository-secret mutation is performed.
