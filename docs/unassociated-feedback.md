# Unassociated feedback retention

The paired Buddy/Manager change adds a local library API for typed error observations that have no conversation or turn. These observations are historical data, not a display queue, success/cancellation receipt, page identity or permission to write to the tablet. The delivery evidence and remaining qualification gates live in [the completed change record](../openspec/changes/archive/2026-10-26-unassociated-feedback-retention/results.md). The archived implementation does not claim a published release or production activation.

## Explicit preparation

`unassociated_feedback::Feedback::prepare(StorePaths)` opens a fresh uniquely owned Store, retains its existing exclusive lease, checks complete ordinary state and prepares the actor/generation-bound feedback feature before exposing shared handles. Another owner makes preparation fail busy; it does not stop a service. Normal `Store::open` does not activate the feature. Production wiring remains gated on a qualified consumer and required management paths; use isolated development storage for API experiments.

```rust
use remarkable_reader_buddy::{
    conversation::AttemptReason,
    storage::{StorePaths, Uuid},
    unassociated_feedback::Feedback,
};

fn isolated_example() -> anyhow::Result<()> {
    let root = std::env::temp_dir().join(format!("buddy-feedback-{}", Uuid::new_v4()));
    let feedback = Feedback::prepare(StorePaths {
        data: root.join("data"),
        cache: root.join("cache"),
        credentials: root.join("credentials"),
    })?;
    let operation = Uuid::new_v4();
    let observed_at = 42; // Caller-owned immutable observation time.
    let description = feedback.retain(operation, observed_at, AttemptReason::ProviderFailure, false)?;
    let historical = feedback.snapshot()?;
    assert!(historical.contains(&description));
    drop(feedback);
    Ok(())
}
```

After dropping the facade, remove the named temporary root through the [development hygiene checklist](../.agents/skills/development-hygiene/SKILL.md), preserving only useful results.

Keep the original operation, time, reason and reconciliation flag for literal retries. Changed content under the same identity refuses; uncertain output stays reconciliation rather than canceled/undone. Descriptions use static catalog text and accept no raw request, answer, credential or diagnostic message. Retention is bounded; there is no automatic expiry, deletion, association or later presentation. A separate admitted protocol must handle any future page effect.

## Compatibility and recovery

Prepared storage uses generation format3, `feedback-feature.json`, storage contract2 and six-domain capabilities. Existing contract1 and unchanged legacy1/2 behavior remain. New namespace writes/imports/recovery require the feature, local identity, immutable content and bounds; parsing failure alone is not a universal old-writer fence. Reopening or creating an admitted next generation must not downgrade3. Existing selected metadata can remain historical without granting selected restore or native authority.

| Operation | Supported boundary |
| --- | --- |
| `Feedback::export` | Ordinary prepared3, no selected feature/history; archive3 retains exact original records and required origin metadata. |
| `Feedback::restore_additive` | Current ordinary3 plus legacy archive1 or same-actor ordinary archive3; additively merges history, never replaces it or rewrites IDs. |
| Selected/current2 or cross-owner archive3 restore | Unsupported by this route; no safe downgrade or native rollback is implied. |
| Existing ordinary export/restore or unqualified maintenance | Existing eligibility remains; unsupported3 refuses. |
| Live sync of unassociated feedback | Unsupported, including explicit policy requests. |

The existing `--inspect-owned-data` route remains read-only and starts no Store/provider/device runtime. It emits unchanged report1 for legacy layouts, and report2 when feedback state is observed. Report2 adds bounded current/retained generation-format evidence and counts-only feedback accounting; missing, partial and unsupported are distinct from zero. Neither report grants cleanup permission. The matched Manager consumer must be delivered first; publishing compatible binaries or matching versions does not activate storage. See [canonical requirements](../openspec/specs/unassociated-feedback-retention/spec.md) and the linked change's exact results for actual execution versus native/publication limits.
