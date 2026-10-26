# Manager release-source preview

## Purpose

Describe implemented read-only stable release discovery and persisted source policy
in the shared browser/Electron Manager. Signed APK verification, wired transport,
package lifecycle and source equivalence remain separate unfinished capabilities.

## Requirements

### Requirement: Stable metadata discovery remains distinct from install eligibility
Both Manager distributions SHALL refresh canonical official stable Buddy release
metadata while open, excluding drafts/prereleases and malformed identity. They SHALL
display candidate version separately from actual installed and qualified available
versions. Missing verified signed APK, source/SDK provenance, package ownership or
connected compatibility SHALL refuse installation. Metadata alone SHALL never qualify.

#### Scenario: Stable promotion while Manager stays open
- **WHEN** a previously prerelease GitHub release becomes a stable semantic-tag release
- **THEN** refresh/poll shows its candidate without restart and no install mutation occurs.

#### Scenario: Incomplete or unreachable release
- **WHEN** assets are incomplete, metadata is malformed, or GitHub is rate-limited/unavailable
- **THEN** Manager shows the unresolved/error state, marks retained metadata stale, and refuses install.

#### Scenario: Server rate-limit delay
- **WHEN** GitHub declines requests with a retry or reset time
- **THEN** both automatic and manual refresh wait until that time, retain honest
  stale metadata, and explain the delay; normal polling is at most once per five minutes.

### Requirement: Source preference does not imply a separate installation
Manager SHALL persist default Official stable policy independently of package origin.
Community SHALL remain unavailable until actual listing; a previously saved unavailable
policy SHALL be displayed honestly rather than silently rewritten. No source selection
SHALL mutate installed package, data or version; equivalence/downgrade requires later
qualified Vellum contract and explicit safeguards.

#### Scenario: Reload with policy
- **WHEN** either distribution restarts with a valid saved preference
- **THEN** the preference is restored; unavailable community is explained without reinstall.

#### Scenario: Protected storage unavailable
- **WHEN** preference storage cannot be read or written
- **THEN** Manager displays that persistence is unavailable and does not claim a saved change.

### Requirement: Shared read-only accessible UI
Browser and Electron SHALL use the same Angular controller/templates and Tailwind
styling, preserve keyboard focus/responsiveness, and retain Electron sandboxing.
Release requests SHALL use a bounded allowlisted public API without tablet/Buddy access.

#### Scenario: Preview on disconnected tablet
- **WHEN** Manager has no identity-verified wired tablet connection
- **THEN** installed version remains unknown, qualified availability is unavailable,
  community is unlisted, and official metadata refresh is still usable in both hosts.
