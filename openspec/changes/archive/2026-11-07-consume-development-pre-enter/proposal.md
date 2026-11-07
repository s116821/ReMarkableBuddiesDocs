# Consume the development pre-Enter diagnostic

## Why

The SDK has an opt-in historical pre-Enter command, but delivered Buddy has no
closed read-only request for it. Adding a normal Cargo feature alone would break
Buddy's ordinary `--all-features` checks against its unchanged SDK v0.2.0 pin.
A small build-only consumer seam is needed before an independently selected
native diagnostic can use the existing connection and original deadline.

## What Changes

- Add one build-only typed request and connection method through the existing
  read-only admission, progress and retention path.
- Preserve exact raw UTF-16 and explicit refusal/empty distinctions, without
  exposing current composer or mutation authority.
- Specify an isolated command-local Cargo path patch and developer lock/target,
  while keeping ordinary dependency pins and release/source validation intact.
- Refuse the diagnostic cfg under official candidate/release identity inputs or
  an exact official semantic tag, including externally supplied compiler cfg.
- Keep the SDK's separate native variant/arming marker and eventual input and
  recovery qualification with their existing owners.

## Capabilities

### New Capabilities

- `development-native-pre-enter-consumer`: bounded build-only Buddy consumer of
  the SDK's historical diagnostic, including isolated source and build admission.

### Modified Capabilities

None. The new capability is synchronized in this coordinated implementation.

## Impact

The implementation affects Buddy's build script, closed read-only request dispatch and
ResidentConnection only. Ordinary Cargo.toml/lock pins, CI feature coverage,
release/APK validators, production CLI and runtime configuration stay unchanged.
Docs PR 152 and Buddy PR 138 form one implemented change. No native or provider
operation is authorized by this delivery.
