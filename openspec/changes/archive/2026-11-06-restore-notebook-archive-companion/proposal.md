# Why

Manager can inspect and export ordinary notebook archives, but its restore flow
accepts only the legacy version1 producer. The delivered notebook producer now
supports explicit version2 prepare/apply/status. Users need the same deliberate
preview, confirmation and uncertain-result handling for those archives.

# What Changes

- Add an explicit notebook restore capability in the shared browser/Electron UI.
- Reuse the existing restore lifecycle, private intent custody, maintenance I/O,
  bounded transport and presentation logic with a fixed notebook family.
- Keep legacy selectors/version1 admission unchanged; never infer the family from
  an archive or rewrite an original intent.
- Qualify the actual host/controller/transport and both application surfaces with
  positive notebook examples and cross-family refusal controls.

# Capabilities

## New Capabilities
- `notebook-restore-companion`: explicit same-actor notebook restore consumer.

# Impact

Manager host, renderer, bridge/transport integration and focused tests; central
Docs owns the specification. Consume Buddy main e664c2ea99f5d293908800b54493c57ebf69a9b9
and its archived `restore-ordinary-notebook-archive` contract without changing
that producer. Cross-actor/shared restore, Drive/transfer, initialization, native
pages, runtime activation and package qualification are separate work.
