## Why

Reader already captures handwritten source questions and displays their interpretation on the Buddy page. A handwritten question mark indicates that the associated handwritten question may be removed from the source after capture. The current Reader never performs that removal.

## What Changes

- Carry an observation of the marked fragment and its question-only region through the existing source gesture, capture and interpretation flow. Preserve the current answer and independent transcription behavior.
- Link the exact interpreted question and region to the original turn, retained image and observed source. Require a fresh acknowledgment before the request owner may submit the erase.
- Present the retained question in the Buddy conversation even when answering abstains. Use its original user turn and source evidence for any later explicit correction.
- Use the existing ordinary page and viewport guard at the erase handoff. Preserve the printed page, surrounding notes, circles and highlights. A missing mark, unsafe region or stale input leaves the source intact. An uncertain erase stops the original attempt without a retry.
- Keep typed requests, Writer input and explicit handwriting correction on their existing paths. Explain the handwritten-mark convention in the existing Reader usage guidance.

## Capabilities

### Modified Capabilities

- `reader-analysis` covers the mark observation, interpretation and source association.
- `tablet-io` covers bounded erasure, ownership and result evidence.

## Impact

Central Docs and the existing ReMarkableBuddies Reader, Ledger, backend and simulator are affected. The first implementation exercises the ordinary Reader composition with modeled editable ink and Buddy presentation. Installed use requires a supported capture-to-viewport binding and qualified eraser footprint. Erasure when answering abstains also requires the guarded question-only Buddy presentation that is currently missing. Qualify recognition on representative handwriting and preservation on supported technical PDF, notebook and EPUB pages before claiming delivery. Coordinate code and spec review, qualification, canonical sync and archival as one delivery.
