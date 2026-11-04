# Prepare Buddy storage explicitly in both companions

## Why

Existing Manager saved-mode inspection, Local-only choice, ordinary export and
ordinary restore all require an existing valid Buddy Store. They deliberately
refuse initialization/recovery. A clean or structurally incomplete tablet cannot
use those capabilities through Manager even though the delivered host-mode CLI
already offers explicit initialization. This is one missing user-facing setup
step; it does not complete replacement-device restore, installation or cloud sync.

## Change

Add a distinct **Prepare Buddy storage** capability to browser helper and Electron.
Show a policy-only review of the existing producer's actual effects, require a
separate deliberate confirmation, then invoke only the fixed no-input
`--sync-mode-operation initialize` once for the captured target/reference.
Reduce a valid complete successful report to a saved-mode kind without exposing
private authority. Preserve uncertain attempts separately from later observations.
Reuse existing wired observation, maintenance ownership, host lifetimes and the
producer's Store rules, not a second setup/recovery engine.

The review explicitly states that normal owned storage creation/recovery may
change markers/staging at the configured locations. It cannot promise that the
Store is empty, freeze configuration, reserve a destination, predict repairs or
report counts. Configured valid roots and legacy sync disabled remain producer
prerequisites. This feature does not set paths/configuration or choose a mode.

## Existing contract and delivery

This is a Manager/Docs consumer of the existing host-sync-mode producer contract.
The mode command module is exact Git blob80e9a21b9e1a7b2d447b830c6796f47ca32c97a0
at reference4eeaabef, delivered82201bb and integration897b082. Source-body
equivalence does not establish host/device qualification. The consumer precode
was independently accepted before implementation.

Keep one paired Manager/central-Docs change through meaningful verification,
canonical sync, archival and coordinated review/delivery. Existing mode/archive
contracts remain unchanged. Public/manual contributors need no private account,
particular agent, development machine or task-tracking service.

## Exclusions

No APK/native installation, source
payload display, arbitrary paths, configuration/credential edits, service stop,
mode choice, remote binding/bootstrap, archive transfer/restore, selected adoption,
new cleanup algorithm, automatic retry or implicit uncertainty settlement. Provider authentication is already delivered; backup
inspection still lacks a qualified provider/status interface and is separate.
