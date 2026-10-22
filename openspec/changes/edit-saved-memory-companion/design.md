## Context
Actual Manager0983fed has separate model/basic/forget/export consumers and one MaintenanceIO owner. The unchanged saved-memory producer on Buddy7f07169 exposes strict inspect/prepare/apply/status, origin-only profile data and digest-only status intent. Its report always says runtime unverified. Read the exact producer contract and implementation before adapting the consumer: the model editor's restart-required success and model string grammar are incompatible here.

## Goals / Non-Goals
**Goals:** one shared enabled/profile declaration editor, exact private replacement input, truthful saved-only results, original-bound reconciliation and five-lane ownership. Preserve all existing Reader/Writer/selected-memory drafts, current maintenance APIs and corpus attribution.

**Non-Goals:** profile setup/discovery/catalog/membership, selection repair, domain initialization/migration/delete, effective runtime/automatic Reader activation, credentials/provider/service operations or tablet qualification. No producer change, administrative service API, new dependency or release machinery.

## Decisions
Use a separate optional memorySettings capability with the same begin/save/status/cancel/retained interaction as the existing model editor. This permits explicit saving of a bounded supported patch without changing older API caps or applying the model parser's different activation semantics. Begin inspects one saved file; Save prepares then conditionally applies exactly once within one total budget. No-op never applies. Pure status retains only the original hash-only intent, never profile text.

Render enabled boolean/origin and profile origin/presence; never render an existing profile identifier. Keep/Set/Clear choices operate independently. New profile text stays private and uses the existing exact opaque-text mapping, including decoded UUID spelling, rather than a new UUID regexp or trim/canonicalization. Producer validation decides UUID, enabled/profile/selection and legacy-sync consistency. Raw replacement is not signal state, DOM persistence, safe result, error or log content. Synchronous clearing precedes the first save await and every invalidation boundary.

Extend the existing shared token owner to a fifth memory-settings lane. An acquired remote operation invalidates every other idle grant; Busy performs no hook/cancel/I/O. Reference/token/generation guards keep old cancel/completion from affecting new work. Explicit observation and other maintenance invalidate this editor; editing pauses polling, matching existing model editing. Retained uncertainty remains original-bound across renderer reload only while the host process survives.

Reuse fixed wired child/identity checks and standard Node/Python libraries. Add guarded HTTP/main-frame IPC separately and share the Angular controller. Keep a precode review gate before source/API edits, and ordinary both-OS development/source/retained-browser/packaged-Electron verification before final linked delivery.

## Risks / Trade-offs
- Coarse profile presence cannot prove equality or membership: trust only the original-bound producer result; never infer a no-op or repair selection from the public view.
- Saving enabled true/profile does not make Reader memory operational: every success/status remains runtime unverified, with explicit saved-only UI copy. Explicit maintenance remains available when disabled.
- Unknown publication cannot be safely retried: retain original digest-only status context, cap unresolved records at8 without eviction and require an explicit original status check.
- Private immutable JS/IPC/OS copies cannot be zeroized: clear mutable buffers/draft/actual input promptly and make no stronger erasure claim.
- Historical reports are Windows host evidence: consume original streams/hashes without execution or relabelling; separate synthetic POSIX transport/UI cases from original evidence.

## Migration and delivery
The capability is optional; older/unavailable producer support refuses without fallback. No configuration/domain migration or source version is introduced. One central Docs PR and linked Manager implementation PR contain the whole own lifecycle; final review/current CI precede Docs-first squash, with actual-main/new-tag/publication observed separately. Existing credential work remains independent.
