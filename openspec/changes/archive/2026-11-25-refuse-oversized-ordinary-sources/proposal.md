## Why

The signed RM2 profile normally refuses a notebook above 17 pages during observation. The protocol can still represent a longer complete order. If such an observation reaches Buddy, the pinned SDK rejects its source capture during request encoding and Buddy treats the error as lost runtime integrity.

## What Changes

- Refuse the oversized request after observing the full page order and before sending a capture request or changing the page.
- Keep the owned session available for a new gesture on a supported notebook.
- Publish the verified capture and insertion limits and the dependency for larger notebooks.

## Capabilities

### Modified Capabilities

- `reader-answer-pages`: define how an oversized ordinary source request ends and a later request proceeds.

## Impact

The installed Reader and Writer capture entry point and its offline service fixture. Native capture and mutation contracts retain their existing limits.
