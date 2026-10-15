# Current producer identity in the existing Manager consumer

## Source and ownership
Read full current REM-41 and all107 comments, current REM-42 and exact called consumer/package sources. Accepted Manager4a9ef9b029a53b8efec9c5427581aa7930cc5ff0 preserves the entire earlier reviewed stack; current live producer99bde579c7ca458cd9670cc83682e0ed93c58c48 removed policy.py/coordinator.py. The old verifier expects two frozen module hashes and package.mjs copies those filenames, so later integration cannot silently retain that obsolete dependency.

Root's release/artifacts.py blob5dee4dee229226b91895fe4a828f40b69a117bfa, SHA2564c0386ae79b1de55f84bea1cb349e62620ef2a763d90c0366a939aec37cdc94c, contains the current pure Release and verify_identity(manifest,release,names). It does not calculate versions or publish releases. release/build.py retains current archive_package and fixed ZIP/provenance/build-info schema. Consumer input checks remain independently bounded; producer verify_packages and its unbounded pathname reads are not called.

## Replacement
Copy unchanged artifacts.py into the explicitly qualified host/qualified-producer runtime resource and record exact provenance. The existing isolated Python verifier hash-checks those bounded trusted source bytes before compilation, registers its private module and calls only Release/verify_identity with the fixed three package names. It must not import a package/script from downloaded ZIPs or search sys.path for an unqualified release module. The selected module is source-owned, not supplied by the artifact being verified.

Desktop packaging already copies trusted host resources. Remove obsolete out/release module copies/extra-resource admission and assert only the selected qualified identity module enters its dedicated host directory. Keep the fixed verifier script, existing licenses/dependency custody and all other runtime resources unchanged. Rebuilding output removes stale selected/legacy resources; no old release policy/coordinator is restored to the active publisher or shipped as a consumer dependency.

## Existing behavior preserved
The existing host manual command, browser helper and Electron download paths continue calling the same bounded verifier. Fixed repository/tag/source/completion/server+actual digest/manifest inventory, ZIP metadata/UTF8/shape/path/size limits, exact embedded identity, no payload extraction/execution, final publication/byte rechecks and atomic cancellation/receipt behavior remain intact. Returned signature/payload/update/APK/native authority remains unqualified/false; later reuse still requires revalidation. No UI/IPC protocol, app version field, transport, credentials or tablet action is added.

## Verification and limits
Use exact current producer build.py only as an attributed TEST-ONLY fixture to create small actual ZIPs and matching provenance with synthetic payload; do not package or select its build engine at runtime. Pin its source bytes and reuse its unchanged archive function with the qualified artifacts module. These are real producer-code/ZIP/process observations, not a live release or full application build.

Before repair, an isolated copy of the existing called helper with only current selected resources and no policy/coordinator must fail the new positive compatibility case; retain that result. After repair it must pass without legacy modules. Retain modified-selected-module refusal before its sentinel executes and all still-selected bounded consumer controls. Exercise the actual copied packaged verifier and exact resources in existing browser/Electron/package checks; preserve synthetic UI versus actual filesystem/process attribution. No duplicate earlier native/provider/APK/compiler matrices.

Required current supported checks and exact hosted logs precede independent source/spec acceptance. Sync/archive only this completed change. Root still owns parent-first delivery/release state; Windows physical, backend/foundation, signed APK/trust, automatic updater and full REM-41/42/35 gates stay open. Proposed memory query input and Main's live-provider work are separate and do not block this implemented-interface task.
