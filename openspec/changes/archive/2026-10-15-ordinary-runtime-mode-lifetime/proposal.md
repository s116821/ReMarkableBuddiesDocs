## Why

The ordinary Reader currently checks absent or LocalOnly sync mode at startup,
then retains the Store through the actual Ledger, optional memory and Reader
loop. The existing legacy data lease prevents selected-store publication but
does not pin sync mode. An ordinary request must not silently continue under a
different mode chosen through another handle to that same Store.

## What Changes

- Add a distinct ordinary read-mode lifetime lease in the existing storage mode
  implementation, coordinated with its REM-52 owner.
- Retain that lease in the actual ordinary Reader startup/loop caller, preserving
  the existing config/mode admission rules and legacy publisher behavior.
- Verify real Store transitions, stale-token refusal, release on drop and the
  actual startup consumer. Do not add an unused routing layer.

## Scope and Delivery

REM-24 and REM-52 coordinate this narrow application/storage boundary. Docs owns
this change; Rust owns implementation. Existing conversation/storage foundation
parents remain explicit and unmerged. This is not REM-39, a new sync engine,
provider activation, a native capability or completion of REM-24/52. Linked code
and Docs form one delivery; this proposal is not a separately completed feature.
