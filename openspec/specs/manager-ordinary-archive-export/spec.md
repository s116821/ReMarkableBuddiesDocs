# Manager ordinary archive export

## Purpose

Provide explicit private on-tablet ordinary archive preview, confirmation and original-status reconciliation in both companions without implying off-device backup or restore.

The completed [implementation contract](../../changes/archive/2026-10-22-export-ordinary-archive-companion/contract.md) and [verification](../../changes/archive/2026-10-22-export-ordinary-archive-companion/results.md) preserve limits and attribution.

## Requirements

### Requirement: Explicit shared on-tablet archive preview and confirmation
The companion SHALL offer the same ordinary format1 export preview and separate deliberate confirmation in browser and Electron using the unchanged original-bound producer, without implying off-device backup, restore or runtime authority.

#### Scenario: Original preview then confirmation
- **WHEN** a user supplies an explicit safe tablet destination and confirms an unexpired preview
- **THEN** only that original intent/destination is applied once, with no refreshed conditions or automatic retry.

#### Scenario: Honest private archive disclosure
- **WHEN** a preview contains portable configuration or intentionally omitted media
- **THEN** both companions disclose private configuration and media completeness, and state that archive bytes remain on this tablet.

### Requirement: Bounded private destination and original reconciliation
The host SHALL retain sensitive destination/intent only in bounded ready or uncertain original records, clear renderer draft and actual DOM synchronously, and expose only finite safe summaries/references.

#### Scenario: Submit or leave the editor
- **WHEN** prepare begins or the editor is invalidated, hidden, stopped, disconnected, expired or destroyed
- **THEN** private renderer draft and actual input clear before the relevant first await/event boundary, without stale completion clearing a newer editor.

#### Scenario: Possible publication without a complete reply
- **WHEN** apply may have run or original desired closure remains unresolved
- **THEN** the exact original packet supports explicit status only, no reapply or destination deletion occurs, and current closure is distinguished from historical publication.

### Requirement: Shared custody and attributed guarded verification
The consumer SHALL preserve existing maintenance ownership and old APIs/corpora, enforce current bounded protected-host admission, and complete only its own independently reviewed lifecycle.

#### Scenario: Busy, expired original or stale cancellation
- **WHEN** another lane owns I/O, ready authority expires or an old callback races new work
- **THEN** no unauthorized I/O/hook/cancel/release/settlement occurs and no conditions are refreshed.

#### Scenario: Historical corpus and finite host boundary
- **WHEN** original Windows reports or malformed public/private requests enter a guarded host
- **THEN** original bytes/hashes remain exact, incompatible path authority refuses, synthetic POSIX surroundings stay separately attributed and no path/config/error text leaks.

#### Scenario: Reviewed complete delivery
- **WHEN** final source/Docs are proposed for merge
- **THEN** ordinary both-OS source/retained checks, own canonical/archive equivalence and independent review precede normal linked delivery, with actual publication and native/transfer/restore work tracked separately.
