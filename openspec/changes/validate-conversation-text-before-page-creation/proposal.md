## Why

Reader can insert a Buddy page before discovering that the tablet keyboard cannot type the formatted answer. Writer can also reject a draft that fits an existing page because its initial check counts the heading for a new page.

## What Changes

- Check the exact new-page text before requesting an insertion. Keep the original answer or draft when the keyboard cannot present it.
- Check the Writer body independently of the creation heading so an existing conversation page can accept the full draft it has room to display.

## Capabilities

- Modified capability: `reader-answer-pages`.

## Impact

The change uses the existing Buddy output backend and page-placement procedure. It keeps the current keyboard, timing, character and byte limits.
