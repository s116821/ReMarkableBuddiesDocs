---
name: development-hygiene
description: Plan build storage and clean completed development outputs at handoff or delivery. Use before heavy builds or when retiring caches, package scratch or worktrees across the ecosystem; preserve active work and useful validation evidence.
---

# Development hygiene

This shared checklist lives in central Docs and applies on every development machine. Run component commands from the selected checkout. Follow existing task ownership and execution permissions; this skill does not authorize device actions or retries of policy-blocked operations.

## Before a heavy build

- Check free space on the actual build and temporary volumes. Estimate working headroom from comparable builds and expected outputs; use no arbitrary universal quota. Resolve insufficient space before starting.
- Reuse an appropriate active cache when revision, toolchain and concurrent ownership permit; isolate only when needed. Identify its owner and path. Prefer existing validation that covers the exact revision and required checks; rebuild or repeat checks for a concrete change or unresolved concern.

## At handoff or delivery

- Inventory only the named task/component scope. Check active owners and processes before choosing unused Cargo targets/incremental data, `node_modules`, `dist`, package output or review scratch. Coordinate shared storage; do not delete another lane's active cache.
- Preserve source commits and lockfiles, dirty/unpushed work, useful failure logs, test/CI references and hashes. Generated intermediates are not evidence merely because they came from a validation run. Delete obsolete caches rather than moving them to a network drive.
- Retain a binary only for a concrete pending use. Record its exact path, owner, source revision, content hash and expiry or review point; review the exception when that use ends. Preserve genuinely required held inputs without retaining their entire build trees.
- Before recursive cleanup on Windows, resolve each exact absolute target and verify it remains inside the named intended scope. Inspect for reparse points and avoid traversal. Use literal paths in one filesystem workflow; do not compose deletion across shells, globally prune caches or retry a policy-blocked operation through another route.
- Treat source/worktree retirement separately from generated-output cleanup. Verify a clean state, relevant commits pushed and preserved on the intended upstream (merged as applicable), and no active owner/dependency. Preserve unmerged or dirty work first. Remove registered worktrees through normal Git lifecycle, without force or blind directory/shared-metadata deletion.

## Closeout

Record exact removed scopes, retained exceptions with review points, and logical file bytes removed. Measure before/after free space on the affected volume separately: other activity, allocation and network storage can make that change differ from logical sizes. Verify preserved source state and retained artifact hashes. State failed/skipped removals honestly; a command exit alone is not a reclaimed-space measurement. Cleanup is bounded task work, not an unattended daemon or a global configuration change.
