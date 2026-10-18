# Deliver personalization maintenance without the unfinished Reader stack

## Why

The accepted personalization configuration command currently calls an unmerged
subject-memory preflight helper. Its inherited branch therefore cannot deliver
this otherwise independent setting on current main.

## What Changes

Reuse the existing PRs and preserve their original commits. Integrate the current
main tree, retaining only the owned configuration interface, tests and central
documentation. Move existing-store admission into the shared Store constructor,
which already owns the stable lease and configuration writer. Do not import the
Reader, selected-memory or provider stacks.

The public personalization JSON, Unicode limits, compare-and-swap, immutable
snapshot and disk-readback semantics stay unchanged. Runtime activation and
Reader/Writer application remain separate unfinished work. No device or provider
operation is needed to verify this filesystem and CLI delivery.
