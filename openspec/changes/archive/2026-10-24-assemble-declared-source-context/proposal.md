# Assemble declared source context

## Why

The standalone source resolver correctly returns ordinary historical IDs and a
caller-supplied key. It explicitly does not freeze the next receiving call. A
caller composing resolution with receiving must therefore handle source/anchor
changes between those snapshots. The existing receiver and durable preparation
already own validated frame snapshots; an opt-in composed path can resolve the
declaration within those same records without inventing active intent.

The standalone resolver and its publication are complete. This is an additive
contract, not a repair or reopening of that delivery.

## What changes

- Add read-only receiving and durable preparation entry points accepting the
  existing SourceDirective, resolving against the same validated records used
  for assembly instead of chaining public resolution and receiving calls.
- Reuse complete frame budgets, local Provider querying and captured publication.
  Preserve explicit no-document/change, named-operation selection and independent
  key admission, with no current-page or timestamp fallback.
- Preserve every existing API, serialized frame/evidence schema and historical
  retry rule. Record the resulting selected frame, not new directive lineage.
- Add focused real Store/Index fixtures and a public guide for the composition.

## Capabilities

- Add `declared-source-receiving`: snapshot-coherent declared receiving and
  existing sealed durable preparation.

## Impact and exclusions

One paired Rust/central Docs delivery. Internal factoring is confined to ordinary
resolution, receiving and preparation. No Store-format extension, new durable
record/source registry, capture membership change, active-intent selection,
router/Reader/Writer integration, model/research/device/service call or settings
change. Held work and completed publication evidence remain preserved.
