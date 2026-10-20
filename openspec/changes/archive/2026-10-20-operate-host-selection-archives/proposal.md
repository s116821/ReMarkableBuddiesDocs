# Operate selected-history archives from the host

## Why
Verified selected export and offline archive inspection are delivered Store APIs,
but have no supported operator command. A custom Rust harness is still required
to preserve historical selected custody or verify a received archive.

## What changes
- Add explicit export-selected and inspect one-shot commands over existing archive policy.
- Retain existing Store/current-mode lifetimes during export and bounded report handoff.
- Expose verified counts/media completeness without contents, live tokens or restore authority.

## Boundaries
This is a complete bounded host command delivery, with paired source/Docs tests,
review, canonical sync/archive and normal publication. It does not restore or
activate selected membership, export ordinary configuration, implement cloud
transfer/bootstrap/workers or contact a provider/tablet. The unfinished sync and
Reader changes remain active. The existing ordinary export API embeds a config
snapshot, so it is deliberately not wrapped by this command.
