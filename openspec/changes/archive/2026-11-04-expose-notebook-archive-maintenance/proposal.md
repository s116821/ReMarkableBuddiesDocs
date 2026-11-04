## Why

The ordinary notebook archive engine preserves format 4 but only library callers
can invoke it. Local maintenance needs an explicit export and detached readback.

## What Changes

Add `export-notebook` and `inspect-notebook` to the existing archive command.
Reuse the notebook archive schema, validation and streaming publication. Keep
the active source existing-only and the detached archive quiescent.

## Impact

Legacy archive operations retain their contracts. Restore, activation, native
operations and notebook sync remain outside this change.
