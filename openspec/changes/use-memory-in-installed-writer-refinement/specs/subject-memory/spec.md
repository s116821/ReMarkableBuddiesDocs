## ADDED Requirements

### Requirement: Subject memory in installed Writer refinements

When the installed tablet service receives an ordinary request to refine the current draft, it SHALL use the configured local subject memory from the conversation Store. It SHALL apply the existing ordinary Writer query, source, cancellation and publication rules while retaining the same Writer owner through page placement.

#### Scenario: A draft uses an earlier relevant fact

- **WHEN** the user refines the current draft on its bound page and the configured profile has relevant subject memory
- **THEN** Writer SHALL query using the exact refinement text and original source document and supply the bounded results as a separate associative context alongside the existing draft and source.

#### Scenario: Disabled or empty memory

- **WHEN** memory is disabled or the installed refinement finds a valid empty view
- **THEN** the ordinary draft input SHALL remain unchanged and disabled memory SHALL perform no lookup.

#### Scenario: An explicit development plan

- **WHEN** the refinement comes from an explicit development plan
- **THEN** it SHALL use the inputs declared by that plan and SHALL NOT implicitly include the installed profile.

#### Scenario: Incompatible provider

- **WHEN** the installed request would use a foreign Store or a provider requiring selected publication
- **THEN** Buddy SHALL refuse before claiming the queued request, calling the model or changing the draft.
