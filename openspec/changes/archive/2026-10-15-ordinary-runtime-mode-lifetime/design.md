## Existing Source and Ownership

The inspected Rust contract parent is 67c73e9c4a0a4a6ba5d4fb05eea8ef3d383629a6;
the corresponding Docs parent is 0c1138e2fa133e0db0d268c83783097afc931357.
These topics contain the unmerged conversation foundation. Live main does not
already contain that domain; do not duplicate its types or claim deployment.

reader_runtime::ordinary_store currently returns the admitted Arc<Store> after
a snapshot mode check. main retains it through Ledger, LocalMemory and any
existing legacy worker. Store::set_sync_mode already serializes with mode_handles.
LegacySyncLease pins ordinary data, SyncModeLease admits only explicit publishing
modes, and LegacyPublisherLease is not an application read-mode substitute.

Main owns reader_runtime/main and this central contract. SCRAPPY owns storage
mode implementation and its own focused tests. Coordinate exact API before code;
preserve protected unfinished Reader files and all unrelated work.

## Proposed Storage Seam

A distinct OrdinaryModeLease, returned by
Store::ordinary_mode_lease(&Arc<Self>, &SyncModeToken), admits only absent mode
or LocalOnly. Check the exact current token and mode under the existing Store
mutex, then account the lease in the existing mode exclusion mechanism. Drop
releases that exclusion. No Store mutex is held across model, device or worker
work. No second state file, schema, selection token, worker or mode setter is
introduced. The agreed public names are OrdinaryModeLease and
Store::ordinary_mode_lease. The guard is non-Clone and must_use. Exact original
operation replay may return its existing receipt without changing mode; a new
transition remains refused while a guard exists.

Do not broaden SyncModeLease into implicit publisher permission or reinterpret
LegacySyncLease. The ordinary guard provides no selected catalog, cloud,
current-page or native authority. An absent mode remains legacy compatibility,
not shared selection. Existing legacy publisher admission can coexist with an
ordinary absent-mode guard, while explicit LocalOnly still forbids that publisher.

## Actual Consumer

Retain the ordinary guard alongside the startup-admitted Store for the actual
main Reader lifetime, including Ledger, optional memory and the existing worker.
Acquire against a fresh snapshot after normal config/credential admission and
before device/model effects. Preserve None compatibility and allow LocalOnly
only with config.sync.enabled=false. Explicit isolated/shared, contradictory
configuration, malformed metadata or stale admission refuse; do not silently
retry into another mode. Existing selected receiving and historical recovery
paths retain their distinct contracts.

ordinary_store returns (Arc<Store>, OrdinaryModeLease). main retains the named
_ordinary_mode_lease through its real dependent consumers and run_loop; they
drop before that guard on return or error. The final policy check and lease use
the same captured token; a race refuses instead of refreshing it. Copying the
Arc alone is not a claim of mode admission.

## Verification and Limits

Use real temporary Stores and the actual ordinary startup consumer: absent and
LocalOnly positives, nonlocal/stale refusal, transition blocked until guard drop,
multiple guards, legacy publisher compatibility and unchanged local data. Test
early-return/drop ownership without model/network/device operations. Keep the
existing startup policy and selected/historical controls intact. Do not rerun
unrelated native/provider matrices or fabricate a full mode-switching UI.

This protects supported in-process Store transitions while the existing Store
OS lease protects process ownership. It is not protection against an external
writer bypassing the storage API or proof of provider/remote/native readiness.
No runtime live reconfiguration or Manager service control is added.
