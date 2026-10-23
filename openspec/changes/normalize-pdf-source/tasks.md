## 1. Contract and parser admission
- [x] Read complete requirements/comments, preserved work and required narrow references; inspect actual maintained parser sources and licenses.
- [x] Propose concrete supported profile, resource controls, refusal semantics and provenance before source changes.
- [x] Obtain independent review of this concrete precode and resolve findings.

## 2. Implementation and original regressions
- [x] Add pinned pure Rust parser and offline PDF adapter with exact byte identity, ordered page units and explicit textless reporting.
- [x] Enforce declared structural, encoding, content, resource and output profile without partial-success fallbacks or CMap expansion.
- [x] Add authored fixtures through maintained writer and actual Index queries, Unicode/boundaries, changed identity and existing cache compatibility.
- [x] Verify malformed, encrypted, unsupported, oversized mapping and resource-bound refusal including later-page failure.
- [x] Add public guide and development example with exact profile and honest library-wide resource limits; preserve existing EPUB/cache/SDK/CI behavior.

## 3. Verification and coordinated delivery
- [x] Run affected fixtures, ordinary library check independent of feature-unified tests, fmt and strict Clippy; preserve failures and current evidence.
- [ ] Obtain independent source/spec review and pass current normal hosted checks/cross-target builds; resolve feedback.
- [ ] Verify every requirement/scenario against implementation and evidence; sync only own canonical PDF spec and archive only this completed change.
- [ ] Obtain final paired lifecycle/source review, deliver Docs first/source second by normal squash, then distinguish actual-main CI/release provenance from PR evidence.
