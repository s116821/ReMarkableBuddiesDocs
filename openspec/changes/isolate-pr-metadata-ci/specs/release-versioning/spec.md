## ADDED Requirements

### Requirement: PR metadata event isolation

Application CI SHALL validate current PR titles before source checks. Source
events and actual title changes SHALL preserve the existing normal check names,
stage order and job budget. Body-only edits SHALL NOT execute application work
or create/update its normal check contexts. Omitted metadata-only jobs SHALL
have explicitly distinct names and SHALL NOT mask an earlier failed/canceled
application result. No branch-setting change, successful placeholder or extra
normal PR job SHALL be required.

#### Scenario: Body edit after failed source check

- **WHEN** a PR body changes on unchanged source with a recorded failed application check
- **THEN** current title validation runs, no normal application check is created or replaced, and the original failure remains authoritative.

#### Scenario: Correct an initially invalid title

- **WHEN** an invalid title prevented source checks and the title is corrected without changing source
- **THEN** the same maintained title validation refreshes and successful validation admits real source checks and downstream stages with their normal names.

#### Scenario: Source or main event

- **WHEN** source changes or an eligible main merge is evaluated
- **THEN** normal stage names, required dependencies, artifact identity, failure propagation and existing normal job budgets remain unchanged.
