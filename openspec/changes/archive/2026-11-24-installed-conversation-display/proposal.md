## Why

New installed Buddy pages still show the legacy Reader title and coordinate-delimited answer blocks. Use the unified conversation title and show the interpreted question before its answer.

## What Changes

- Use `ReMarkableBuddies` on newly created signed/installed conversation pages, including blank start.
- Use plain question and answer text for Reader output on those pages. Keep selection coordinates and the original turn records in the existing data path.
- Keep the legacy formatter available to previously bound pages, explicit legacy adoption, fixture profiles, and manual output.

## Scope

This increment covers the application-owned display text within the existing guarded renderer. Composer focus, prepend, scroll, settlement and physical acceptance remain separately tracked.
