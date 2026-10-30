## Implementation

- [x] Inventory all four repositories and current open PRs; coordinate active owners.
- [x] Define the upstream-tooling boundary and preserved publication guarantees.
- [x] Relocate Buddy examples, release/deployment inputs and helper scripts; update every live reference and Cargo target.
- [x] Relocate Manager release inputs and update current commands and workflows.
- [x] Remove custom upstream uploader builds, vendor locks, transferred bundles and implementation fixtures from both applications.
- [x] Replace ordinary command wrappers with direct workflow steps; document concrete retained application-specific logic.
- [x] Update current central contributor/reference paths and keep executable examples application-relevant.

## Verification and delivery

- [x] Validate affected path/workflow, release-policy and package changes with focused controls; retain original hosted failures and verified repairs with exact revision attribution.
- [x] Independently review the paired implementation changes and record exact source, test and CI evidence in their PRs and the cleanup audit.
- [x] Sync the canonical release requirement and archive only this completed implementation change in this PR.

## Remaining delivery coordination

Root owns required hosted checks and final feedback review at each published PR head, normal coordinated merges, main-release observations, and ownership-aware resync of every open PR and active branch. The final queue audit records each remaining PR's unique scope, landed overlap, blocker, owner and next action. These delivery operations remain explicitly pending until their linked PR/issue receipts confirm completion; this implementation archive does not assert them complete.

Paired cleanup PRs: Buddy #112, Manager #50, Docs #121, and independently specified SDK #33. The SDK cleanup merged as `88140f1b64f8b7dc980612343581181b368660c7` after all required final-head checks passed. Buddy/Manager source checks and the focused workflow/extraction corrections are attributed to their original revisions in PR comments. No native qualification follows from this maintenance.
