## 1. Design
- [x] Inspect actual published assets, hashes/ELF, source workflow attribution and existing emulator identities; retain limits.
- [x] Verify merged bases and write central proposal/design/delta/tasks before implementation.

## 2. Implementation
- [x] Extend existing runner/fixtures with fixed verified emulator and distinct published-asset evidence mode.
- [x] Preserve original source-build gate, Linux ownership, Windows behavior and isolation.
- [x] Document public invocation and licensing/attribution/emulation limits.

## 3. Verification
- [x] All13actualcases pass for both unchanged ARMassets; roots unchanged and script sentinel absent.
- [x] Originalsourcebuild actual13regression and meaningful adapter guards pass (13 Linux guards with no skips; Windows guards retain only symlink-privilege skip).
- [x] Syntax/docs/strictOpenSpec/diff checks pass; freeze exact sources/receipts for Main review.
- [ ] Main review, independent exact-source review and required CI pass.

## 4. Closeout
- [ ] Sync/archive completed bounded capability and coordinated delivery; keep hardware/installer/trust gates open.
