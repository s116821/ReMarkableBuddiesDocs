# Architecture and compatibility contract

Three separate repositories: Docs owns all OpenSpec and shared workflow; Rust is one coordinated Reader/Writer application/service; Manager shares Angular UI and logic between browser and Electron. A monorepo requires an explicit decision. Do not split Reader/Writer or invent a fourth core repository.

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
