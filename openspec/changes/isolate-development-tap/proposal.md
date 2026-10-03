## Why

The source-bound development hardware helper's tap path also waits two seconds,
captures xochitl's framebuffer and overwrites a fixed PNG. A caller selecting only
one input effect needs a separate explicit command. This does not explain the
saved unchanged My Files screen or qualify native navigation.

## What Changes

- Add `hardware_probe tap-only X Y`, preserving the existing touch sequence and
  returning after successful release, before the common screenshot tail.
- Preserve existing tap/press behavior and all production input/SDK contracts.

## Capabilities

### Modified Capabilities
- `tablet-io`: explicit development input-only helper command.

## Impact

Docs and the Buddy example only. No device action, build selection, ABI repair,
native OPEN, controller or new recovery framework. Frozen3dc/b591 remains history.
