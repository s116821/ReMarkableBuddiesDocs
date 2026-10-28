## ADDED Requirements

### Requirement: Explicit untrusted companion source selection
A companion consumer MAY accept exactly one untrusted source-path draft during deliberate Prepare under a reviewed bounded consumer contract. The host SHALL derive all authoritative operation/intent/hash/generation conditions from the fixed producer and retained original context, independently validate source/config path domains and exact private packet custody, and accept no renderer path/intent/hash/generation for Confirm, Status or Cancel. This is an explicit prospective exception to the archived producer contract's blanket renderer-path prohibition; the historical archive and producer behavior SHALL remain unchanged.

#### Scenario: User selects an existing on-tablet archive
- **WHEN** the user deliberately prepares one explicit compatible source already on the verified wired tablet
- **THEN** its bounded scalar/path draft is passed only in private stdin and erased synchronously from renderer signal and actual DOM before any await, while producer safe-root/integrity/ordinary-custody checks remain authoritative.

#### Scenario: Later action supplies substitute source conditions
- **WHEN** Confirm, Status or Cancel supplies a source path, intent, hash, generation or replacement original instead of the host-issued reference and captured identity
- **THEN** the consumer refuses without dispatch or refreshed conditions and preserves any genuine original uncertainty.
