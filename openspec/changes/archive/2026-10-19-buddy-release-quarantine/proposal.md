# Actual Buddy release quarantine consumer

## Why
Main confirms the current publisher creates real tagged two-target tarballs, not signed APKs. Manager can verify and quarantine their actual bytes without pretending installation eligibility or overlapping producer work.

## What Changes
- Add a manual host consumer using fixed public GitHub tag/release/asset APIs and the actual publisher completion/provenance contract.
- Stream bounded assets into a newly created user-selected host directory, verify real bytes and recheck release/tag before final receipt.
- Preserve original archives without extraction/execution; always refuse APK install eligibility for current format.

## Impact
Manager consumer files and this separate central change only. No discovery/UI/host IPC change, Rust/release/producer packaging edit, key provisioning, device/provider/install/updater/native operation, source version mint or new worker/checkout. Main owns signed APK and qualified compatibility/lifecycle.
