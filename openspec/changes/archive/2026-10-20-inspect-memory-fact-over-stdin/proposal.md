# Inspect one memory fact over stdin

## Why
The delivered backend inspects current revision envelopes from a bounded file but
accepts stdin only for searches. The companion needs a supported stdin operation
to inspect a fact deliberately selected from search, without remote staging files.

## What changes
- Admit inspect alongside query through bounded stdin and the existing profile/domain path.
- Decode the new inspect wire with explicit strict global/document scope variants.
- Publish the existing raw-envelope/currentness contract and meaningful actual producer specimens.

## Boundaries
Search remains incomplete discovery, not an inventory or permission to edit.
File APIs, query decoding, mutation/setup stdin refusal and existing Store/mode/
selected guards remain unchanged. No editor, write bridge, provider, model,
tablet, native or service operation is added. This is one paired source/Docs
delivery through review, verification, canonical sync/archive and publication.
