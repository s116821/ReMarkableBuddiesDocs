## Why

A person submitting a handwritten question stays on the source page while Buddy interprets and answers it. On the tested reMarkable 2, another 16.6 seconds elapsed between the last model reply and the page insertion acknowledgement. The gesture should open the conversation promptly even when the model is slow.

## What Changes

- Capture the submitted page and open its conversation immediately. Reopen the associated adjacent Buddy page, or insert one when the conversation has no page yet.
- Use the captured source for routing, recognition and answering. A model reply, generated text size, optional indicator or fixed delay cannot be a prerequisite for opening the conversation.
- Present an unsuccessful request as a short Buddy reply in the conversation the user opened. Preserve the source and keep diagnostic details in the log.

## Capabilities

### Modified Capabilities

- `reader-answer-pages` covers when an ordinary handwritten submission opens a shared Reader/Writer conversation.
- `sanitized-conversation-feedback` covers what the user sees if a request fails after the page opens.

## Impact

Affects the installed tablet app's ordinary source submission, conversation page placement, and display of request outcomes. Uses the existing source capture, page association, insertion and navigation operations, and error catalog. The acceptance case uses the normal packaged service and separately times page opening and model work.
