## Why

A user in an ordinary local conversation should be able to ask Writer for a note about its marked source. Stored-target Writer already generates the note from an exact region, but the installed conversation receiver does not yet resolve that region and send the draft through its existing placement path.

## What Changes

- Accept an explicit current-target request in the existing installed Writer input slot.
- Resolve the current interpreted target and conversation revision from the local ledger, then reuse the existing stored-target Writer flow.
- Send the saved draft through the existing guarded Writer presentation path and keep the same regional source for refinement and deliberate export preparation.

## Capabilities

### Modified Capabilities

- `writer-drafts`: Generate an ordinary local draft from one existing current regional target.

## Impact

This increment depends on the ordinary stored-target engine in Buddy #139. A native composer or preset producer must submit the typed Writer request. The existing Reader release continues to select Reader when the slot is empty. Fresh ordinary selections without a saved region remain outside this delivery.
