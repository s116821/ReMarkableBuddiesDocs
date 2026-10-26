## Why
Historical feedback now composes a stored fact with an exact conversation turn, but an error that has no owned conversation/turn cannot be retained through that API. Inventing IDs would falsify attribution; an independent side journal would duplicate storage/recovery policy. The new state needs an explicit domain and compatibility boundary.

## What Changes
- Propose an UnassociatedFeedback namespace containing immutable typed error observations, with no conversation/turn/page identity or display receipt.
- Propose storage contract2 and an explicitly prepared generation format3 fence before the first new-namespace commit, preserving the existing contract1 and legacy generation behavior.
- Add bounded ordinary-mode retention and historical query APIs using the existing Store and static feedback catalog, plus qualified recovery/backup/restore handling.
- Add conditional read-only report2 accounting and a strict Manager consumer while preserving report1 behavior. Manager implementation follows the existing cleanup handback.

## Capabilities
### New Capabilities
- unassociated-feedback-retention: owned static observations before conversation association.
### Modified Capabilities
- shared-storage: explicit format/feature adoption and compatibility handling.
- owned-data-inspection: versioned accounting for the new domain.
- manager-owned-data-inspection: strict report2 consumption and read-only category display.

## Impact
One coordinated Docs/Buddy/Manager change, not a separately completed planning PR. The preferred route and exact proof obligations remain proposed until independent design review. No source/Manager implementation is authorized merely by publishing this draft. No automatic adoption on open, runtime error callback wiring, new retention CLI, presentation, native activation, personal-account sync or maintenance permission is added by this increment. All implementation must preserve current unrelated work and qualify exact heads before canonical sync/archive/delivery.
