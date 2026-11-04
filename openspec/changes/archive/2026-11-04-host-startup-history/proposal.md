## Why

Selected Reader startup and historical maintenance are useful as a bounded
host contract while the broader Reader lifecycle is still under development.
Buddy drafts 34/35 and Docs drafts 16/18 preserve the original implementation
and evidence. This increment integrates their host behavior on delivered main.

## What Changes

- Report explicit selected startup refusal and expose bounded historical
  inspection, context refusal and original pending-request recovery.
- Admit persisted modes early, reuse the admitted Store and preserve the
  ordinary mode and data lifetime guard through the Reader loop.
- Publish the matching offline configuration schema and canonical inspector
  checks for the new Reader declaration.
- Keep fresh acquisition, usable model context, native effects, Writer,
  cross-device recovery and the wider conversation lifecycle in the active
  durable-conversation-context change.
