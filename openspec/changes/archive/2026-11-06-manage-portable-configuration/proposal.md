# Manager portable preference files

## Why
The backend can explicitly export a private V1 preference artifact and has a
separately reviewed conditional import contract. Manager currently offers neither
workflow in its shared browser/Electron UI. Manual Config edits bypass the
original-condition publisher and obscure omitted/null declaration semantics.

## What changes
Add one bounded shared file workflow: export supported saved preferences, choose
an existing preference file, review changed setting names/declaration origins,
then explicitly confirm at most one original-bound import. Reuse current wired
identity, private host transport and maintenance ownership. The backend remains
the sole validator of whole Config state, overlay policy, storage-family admission
and publisher; Manager does not create another importer, Store or sync engine.

## Capabilities
- Added: portable-configuration-companion.
- Consumes unchanged portable-configuration export and the reviewed
  portable-configuration-import producer contract.

This is one linked Manager/Docs delivery through implementation, tests, canonical
sync and archive. This precode is not a standalone delivered feature. Cloud,
archives, replacement-device initialization, service restart, credentials, native
qualification and other portable domains remain outside this slice.
