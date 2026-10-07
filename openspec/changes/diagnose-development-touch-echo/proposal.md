## Why

The source-bound tap-only helper completed its writes while Main's saved before
and after images were identical. Successful writes do not establish that a
complete contact reached evdev readers. The cause remains unresolved.

## What Changes

- Propose one explicitly selected development `tap-echo X Y` command, exposing a
  narrowly feature-gated Touch entry that reuses the production InputObserver and
  owned-touch decoder/watch for one existing tap sequence.
- Report success only after positive down/release observation and existing source,
  released-state and other-input checks. Keep UI acknowledgement false.

## Capabilities

### Modified Capabilities
- `tablet-io`: development diagnostic for one positively observed owned tap.

## Impact

Buddy25c27d8 implements the coordinated proposal, pending independent source review. No SDK,
controller, touch protocol, transform, native OPEN or product-authority changes.
No generic harness, automatic retries or device execution is selected here.
