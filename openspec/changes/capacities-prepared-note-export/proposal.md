# Capacities prepared note export

## Why

Capacities is the first planned destination for new Writer exports. Its REST API assigns object IDs and uses last-write-wins. Existing Mem export evidence assumes a caller-assigned ID and a conditional numeric version.

## What changes

- Add a scoped Capacities create, readback and reconciliation path using the existing export ledger.
- Preserve legacy Mem records and command routes.
- Connect Capacities to the existing Writer and notebook selected-source ownership boundaries, with scoped pending checks and original-only reconciliation.
- Add a compact Capacities connection in the existing Manager Reader/Writer settings, using public-client OAuth and tablet-owned credentials.
- Keep existing-object updates and actual provider/device acceptance open within this change.

## Impact

The affected capabilities are prepared note export, the historical conversation ledger, and Manager Capacities connection. Buddy implements the provider adapter and credential ownership; Manager brokers consent. Code and central Docs remain one coordinated change across the affected repositories.
