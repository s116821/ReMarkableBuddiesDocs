## Implementation and verification

- [x] Join a configured ordinary Reader question to the open EPUB, preserving PDF and inserted-page behavior.
- [x] Normalize the publication in the bounded worker and retain section provenance across a cache hit and a changed source.
- [x] Exercise a first handwritten EPUB question through the existing hosted pipeline. Verify the saved citation and observe one insertion and the cited answer at the fixture renderer. [Hosted Reader check](https://github.com/s116821/ReMarkableBuddies/actions/runs/45484710642/job/138766992546)
- [ ] Verify a real RM2 EPUB question whose answer needs a passage from another section. Confirm an adjacent answer page is visible after the physical lower-right hold. Sync and archive the completed change after acceptance.
