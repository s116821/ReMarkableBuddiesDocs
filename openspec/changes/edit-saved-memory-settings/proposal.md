# Edit supported saved subject-memory declarations

## Why and source facts
Actual source8cc380fec9cdbda8c799f82d0f3c8f6875b56d36 defines memory.enabled:boolean and optional memory.profile:UUID, while the general inspector returns enabled and profile/selection presence and no bounded editor exists. Host memory setup/query currently requires a manually configured profile. Add only explicit saved declaration editing, not new settings or profile discovery/setup.

Current validation requires a nonnil profile when enabled and a profile matching any declared selection identity; legacy-sync constraints remain. Explicit manual maintenance chooses the configured profile/selection independently of enabled. Automatic normal Reader memory wiring remains unfinished. A saved flag/profile is not an active profile, query permission, membership, provider or native readiness claim.

## Scope and ownership
Separate bounded inspect/prepare/apply/status edits only nested memory.enabled/profile, preserving selection and every unrelated declaration, exact no-op bytes and current validation. Reuse the guarded config writer/current Store-mode custody and private hash-only intent/original patch protocol. No memory record/profile/catalog creation, migration/deletion, mode/group/credential/provider/runtime change or Manager source overlap. Main owns this producer; separate consumers retain their owners.

Docs base is actual013d13a0304f787600ee23eae9186da8748276a2. Concrete precode review precedes source edits; one linked Docs/source delivery includes tests, independent review, verification, own sync/archive and separate actual-main/publication observations. This precode is unimplemented. No tablet authority follows.
