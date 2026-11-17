# Capacities prepared note export

## Why

Capacities is the first planned destination for new Writer exports. Its REST API assigns object IDs and uses last-write-wins. Existing Mem export evidence assumes a caller-assigned ID and a conditional numeric version.

## What changes

- Add a scoped Capacities create, readback and reconciliation path using the existing export ledger.
- Preserve legacy Mem records and command routes.
- Connect Capacities to the existing Writer and notebook selected-source ownership boundaries, with scoped pending checks and original-only reconciliation.
- Keep existing-object updates, distributed OAuth and device acceptance open within this change.

## Impact

The affected capabilities are prepared note export and the historical conversation ledger. Buddy implements the provider adapter. Manager connection and credential ownership are part of the separately coordinated integration.
