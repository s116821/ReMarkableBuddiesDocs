# Architecture and compatibility contract

ReMarkableBuddiesDocs owns Buddy/Manager OpenSpec and shared workflow; ReMarkableBuddies is one coordinated Reader/Writer product; ReMarkableBuddiesManager shares Angular UI and logic between browser and Electron. ReMarkableOpenSDK is an independent fourth repository with its own API/device contracts and OpenSpec. Buddy consumes the SDK at build time; Manager does not separately install an SDK runtime. Do not split Reader/Writer products or invent another repository for fault isolation.

The October 1 conditional supervised XOVI candidate keeps a tiny Buddy Supervisor independent of xochitl/XOVI and the normal Buddy runtime as separate processes in the same Buddy repository, release artifact and Manager installation. Native/direct mechanisms remain preferred wherever robust. If XOVI is necessary and qualified, its vetted minimal payload is managed internally; cold boot stays stock, the first supported Buddy gesture activates only the current session, bounded readiness/heartbeat and crash-loop checks govern stock rollback, and reboot returns to stock. Manager owns disable/update/uninstall; recovery cannot depend on the modified UI. A triggering action resumed after restart reacquires its source and validates cancellation/identity rather than replaying stale handles. This is a candidate requirement, not selected or implemented capability. Narrow semantic hooks preserve the stock experience; broad UI replacement is outside scope.

Manager uses host adapters for SSH, OS commands and protected known files. It never queries the running Buddy service; Rust exposes no admin API. Electron supplies host integration. Browser transport must also be supported, potentially by a separate companion helper; the foundation does not claim transport exists yet. REM-41 implements installation/transport after REM-36 storage and REM-25 extension outcomes.

## Compatibility envelope v1

This versioned contract format does not claim unimplemented schema compatibility. Implemented contracts record:

| Field | Meaning |
| -- | -- |
| `contract_version` | Envelope integer, initially 1 |
| `component`, `release` | Component identity and independent official Git tag |
| `configuration_schema` | Implemented schema and supported read/write range |
| `data_schema` | Buddy-owned schema versions and migrations |
| `transport` | Supported host/SSH/OS/file operations and platform constraints |
| `page_extension` | Optional extension identity/version/firmware limits, or explicit none |

REM-36/41/42 own implemented values, adapters and compatibility tests. Unknown combinations are unverified; matching app versions do not imply compatibility. Contract changes need linked Docs/code PRs and explicit deployment/merge order. Discover updates from each manifest release source; never invent a shared ecosystem version.

Rust retains REM-30 Git-tag version authority and post-tag official builds. Manager releases independently. Docs has validation CI only; pure docs merges must not tag/build either app. Accepted page extensions are managed by the installer, never silently by workspace setup. Source documents/annotations, personal account state and firmware remain protected; optional Drive support implies no blanket account pairing/sync.
