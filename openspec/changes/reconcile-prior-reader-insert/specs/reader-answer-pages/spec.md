## ADDED Requirements

### Requirement: Later-boot evidence can unblock independent Reader placement

Ordinary resident Reader placement SHALL distinguish an earlier boot's retained `Indeterminate` insertion from current uncertainty. It MAY continue for a different conversation when the old request and reply correlate, the current admitted runtime has a different boot identity, and fresh native facts match the original document, displayed source page and full page order with the old target absent.

#### Scenario: Exact original order after the previous boot

- **WHEN** a different Reader conversation reaches placement on the original source and the later-boot observation matches the entire original order without the earlier target
- **THEN** the earlier indeterminate insertion does not block the independent placement check
- **AND** every new effect remains subject to the ordinary fresh source, input, placement and reservation checks

#### Scenario: Evidence leaves the older insertion unresolved

- **WHEN** the earlier attempt lacks a correlated indeterminate reply, is from the same boot, belongs to this conversation, or its source, order or target absence cannot be verified
- **THEN** the existing placement fence remains in force

#### Scenario: Historical operation remains consumed

- **WHEN** later-boot facts permit independent placement
- **THEN** the original operation, scope, digest and reply are preserved and the original effect is never replayed
