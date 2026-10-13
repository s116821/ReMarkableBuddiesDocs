# Read-only owned-data inspection

## Why

REM-42 needs a useful file/CLI backend for Buddy-owned category and size views in
both Manager distributions. Calling the existing Store startup to inspect data
would initialize roots, clean staging and rewrite capability files. Inspection
must preserve existing data and report unavailable/partial states honestly.

## What Changes

- Add a versioned JSON report and `reader-buddy --inspect-owned-data` route that
  reads only validated existing Buddy-owned files and returns before runtime,
  provider, credential, sync or device initialization.
- Separate additive apparent file-byte accounting from nonadditive namespace
  media references, including shared content, retained generations and missing
  or intentionally omitted media. Do not report allocated/reclaimable disk space.
- Reuse current Store paths, ownership, format and manifest/envelope validators;
  never call Store::open, recovery, creation or cleanup. Acquire only the existing
  stable lock through a read-only handle; busy and unsupported access are explicit.
- Provide real temporary-Store and actual CLI regressions for nonmutation,
  ownership, sharing, missing/unsupported data, limits and writer contention.

## Capabilities

### New Capabilities
- `owned-data-inspection`: bounded read-only versioned file/CLI accounting.

### Modified Capabilities
- `platform-runtime`: an inspection-only CLI route before normal runtime startup.

## Impact

Rust backend/CLI and central Docs only. No Manager UI/transport, admin API,
service/device operation, cleanup or native-document access. Current source bases
are Rust7b207ec and Docs60a8e0e; parent unfinished REM-37 delivery remains explicit.
The same existing checkouts retain eight dirty native/Cargo files and one tool
unchanged; new topic branches add no checkout or worker. REM-36 is Done; broader
REM-37/41/42/52/53 and release/native gates remain open.

Source basis: current REM-42 description and all five accessible timestamped
comments, including the October 12 ownership claim; actual Store startup and
source/file contracts; focused existing reManager source and primary RCU reference.
