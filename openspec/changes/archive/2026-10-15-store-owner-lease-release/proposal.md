# Release a dropped Store owner's lease

## Why

Current main's Store closes its private lease file implicitly when dropped. On Unix, another thread's subprocess can temporarily inherit the same open-file description before exec, retaining flock after the logical Store owner drops. Current independent retrieval CI38754475546 failed its existing interrupted-commit/reopen test with this ownership error; that trace alone is not deterministic proof of the proposed cause.

## What changes

Extract only the already-existing explicit owner unlock and deterministic duplicated-descriptor regression from accepted selected-storage commit cca7ea9d6a1942ccdfed70d76aab615fd2dca5d4. Storage-owner comments6195113780/6195208828 confirm the exact boundary and no duplicate edit. Do not import the selected-storage stack, serialize tests, add retries, weaken live-owner exclusion or change tests/storage.rs.

## Independent delivery

Two source paths: Store Drop/private test-module declaration and its standalone Unix regression. Verify the actual current-main regression fails without the fix and passes with it, retain ordinary cross-process exclusion/kill/reopen coverage, then complete own review/CI/canonical/archive. No device, SDK, schema, Manager or retrieval behavior changes. The current pipeline failure remains a gate until resolved by actual evidence.
