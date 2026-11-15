## MODIFIED Requirements

### Requirement: Shared fixed-reference protected-file management
Both companions SHALL deliberately install/replace/remove only the already declared protected model-credential file under contract.md, preserving exact accepted UTF8 and producer original/no-op/admission semantics without reference, provider or runtime changes. Source basis: canonical declared-model-credential, archived exact producer/manual/current source and REM42 selection.
Credential-file and reference controls may share the Model connection context;
their distinct writes and outcomes SHALL remain explicit. Custom reference editing
SHALL be a secondary setup task rather than a separate primary destination.

#### Scenario: Deliberate valid action or no-op
- **WHEN** a user begins a fresh observed file editor and explicitly chooses Install, Replace or Remove
- **THEN** only the original-bound action is prepared/applied at most once, absent/present/mode constraints and producer-only no-op are preserved, and no discovery/root setup/reference edit/transaction or authentication claim follows.

#### Scenario: Invalid original, text or envelope
- **WHEN** original admission, strict shape/identity/binding/action/target, Unicode/nonblank/byte or encoded envelope bounds fail
- **THEN** the invocation refuses without normalization, unsafe fallback, private echo, refreshed conditions or late apply.

