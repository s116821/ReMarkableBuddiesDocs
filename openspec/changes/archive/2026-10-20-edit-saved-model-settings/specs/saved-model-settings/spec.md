## ADDED Requirements

### Requirement: Deliberate bounded saved model declaration edits
The producer SHALL accept only explicit model/base_url set/clear under contract.md and current opaque nonblank/byte-cap rules, preserve unrelated values/absence/null and exact decoded strings, and keep a logical no-op byte-identical. It SHALL NOT change basic/general wire, credential/reference/path/mode/schema/precedence/defaults, runtime or provider behavior.

#### Scenario: Exact opaque text or clear
- **WHEN** a supported exact string is set or its saved declaration cleared
- **THEN** only those declarations change, current valid legacy values survive unrelated edits, null and missing remain distinct, and no URL/whitespace/control normalization or provider validation is inferred.

#### Scenario: Invalid whole document or unsupported patch
- **WHEN** full document/schema/value, unknown/duplicate/type/version/cap or fixed patch admission fails
- **THEN** the bounded invocation refuses without repair, fallback, arbitrary editing, credential resolution or outputting the original/new value.

### Requirement: Private patch binding without value echo
Every report SHALL expose only the exact fixed origin/presence view and private hashes/UUIDs, never old/new model/endpoint text. Prepare SHALL bind original file/path and exact canonical patch/target digests without returning the raw patch. Apply SHALL consume the separately retained original patch and reuse the SAME guarded current-custody conditional writer/CAS/exact readback.

#### Scenario: Credential-like endpoint or model
- **WHEN** old/new text contains userinfo/query/fragment/control/CRLF/trailing or private sentinel values
- **THEN** successful/refused/fault output does not echo them, exact decoded saved text is preserved, and intent contains only hashes/UUIDs.

#### Scenario: Changed original conditions or patch
- **WHEN** base/path/patch/target changes, current Store is Busy, or custody fails
- **THEN** no refreshed conditions or new writer/fallback is used and only truthful phase-limited refusal/unknown status is emitted.

### Requirement: Honest disk verification and read-only reconciliation
Complete verified apply SHALL mean exact saved disk bytes with restart-required/runtime-unverified. Status SHALL compare only original desired full file bytes without raw patch, Store/declared-root/provider probes, writes or historical publisher proof. Output custody SHALL last through consuming write/failure, and later refusal SHALL NOT settle earlier missing/uncertain apply.

#### Scenario: Missing apply report
- **WHEN** original apply may have run but complete verified output is unavailable
- **THEN** it remains unknown with no automatic retry/rollback, and explicit hash-only status may report desired-file-observed or unresolved without raw patch or runtime authority.

#### Scenario: Prefix failure or effective override
- **WHEN** report output fails or a saved value may be overridden by CLI/environment
- **THEN** guards release only after the consuming failure, no second report/replay occurs, and saved-file truth is never relabelled as effective provider/runtime readiness.
