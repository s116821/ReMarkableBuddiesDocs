## Why

The installed Reader captures the notebook ID with the handwriting, but discards that ID before searching subject memory for a first question. A relevant fact saved for the open notebook then cannot reach the answer.

## What Changes

Use the verified notebook ID for the existing memory search after the handwriting has been independently transcribed. Keep the current global scope for captures without an admitted notebook and preserve the selected Reader's existing ownership checks.

## Capabilities

- Modified capability `subject-memory` covers the original notebook for an installed Reader question.

## Impact

Buddy changes the ordinary Reader's query on the existing memory provider. This requires no migration, new provider, or change to the tablet installation.
