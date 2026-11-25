## Why

The installed Reader retains a verified question and provider-failure fact but leaves its usable Buddy page without an explanation. The Reader can present the existing sanitized description through its guarded output path.

## What changes

- Present the verified question and a static provider-failure description when the same conversation already has a usable Buddy page.
- Retain the original owned failure when safe placement is unavailable.
- Keep marked-question presentation and source ink handling under their existing rules.

## Capabilities

### Modified Capabilities

- `sanitized-conversation-feedback` adds a scoped installed Reader consumer for the current provider failure.
