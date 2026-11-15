## ADDED Requirements

### Requirement: Resident historical media remains available to receivers
Ordinary receiving SHALL resolve eligible ResidentCapture from the same frozen
context, verify original PNG and exact provider derivation through the existing
resident validator, and attach only its four provider derivatives. It SHALL
preserve source/ordinal/dimensions/attachment-index/digest associations through
deduplication. Existing attachment/count/association limits and one cumulative
resident-proof allowance SHALL be admitted before expensive reads/decodes.

#### Scenario: Resident history reaches another buddy
- **WHEN** an admitted Reader follow-up, Writer Generate/Refine or notebook reducer uses retained resident history
- **THEN** the exact verified overview/strips and ordered associations reach the existing receiver, the original remains provenance, and later handback retains actual prior text.

#### Scenario: Original or derivative cannot be proved
- **WHEN** a required original/derivative is missing, corrupt, recipe-inconsistent or exceeds the cumulative receiving allowance
- **THEN** receiving refuses before a model call without silently discarding the resident source or substituting current pixels.
