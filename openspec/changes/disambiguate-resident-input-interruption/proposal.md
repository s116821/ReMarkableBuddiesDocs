## Why

The installed Reader trial retained a verified answer and an insertion receipt but stopped before the answer appeared. Its guard reported cancellation without saying what it observed. The resident input path also accepts some passive device packets as interruption.

## What changes

- Keep passive device output, repeat configuration and timestamp metadata quiet for active resident requests.
- Record one fixed category when the request input guard first interrupts.
- Preserve genuine input cancellation, input integrity checks and the original native operation receipt.

## Capabilities

### Modified Capabilities

- `reader-answer-pages` clarifies active resident request input and its diagnostics.
