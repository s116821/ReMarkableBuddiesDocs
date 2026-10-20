## Context
Producer Docs71 has an independently accepted fixed saved-only inspection contract
at2a320181. Current Manager3c789a0 already supplies SavedModeController, strict
saved-mode private/public parsers, fixed SSH callbacks and real helper/IPC guards.
Its MemoryForgetHost owns one private mutation intent; renderer clear alone cannot
invalidate that ready host reference. Prior prepared-forget delivery and publication
are complete, and are not replayed to prepare this design.

Source basis: current native files in Manager3c789a0, Docs54085ec canonical
requirements and source-backed producer review5584589306. The25-field vector is
synthetic design evidence. Main has since published an actual35-report corpus at
Buddy0e0eec73 (captured4bc7eb0, retained executable digest); complete artifact
receipt is verified, and dependent consumer parser/controller tests now verify all original bytes and semantics. No corpus case is replayed to create this design.

## Goals / Non-Goals
Goals: strict bounded scalar/presence projection, honest saved/origin/runtime labels,
explicit shared inspection, before-I/O forget invalidation, host/controller lifetime
and current protected package evidence. The exact API and caps are in contract.md.

No general Config serialization/editor, effective environment/model/provider check,
raw digest authority, credentials management, path admission/Store open, new daemon,
persistence, dependency, global timeout expansion, service/native or tablet work.
Main owns producer code and corpus; this lane owns the consumer only.

## Decisions
1. Reuse optional host-method/controller/helper/IPC patterns with the exact names
   in contract.md. Keep fixed remote command separate from bounded host identity
   stdin. Strict private report and public view are distinct shapes; only the
   projection leaves the privileged host. Raw file digest is discarded, never cached.
2. Pin all25 default values and exact types, literal dotted keys, optional origins,
   same-origin complete path triple, text bytes/presence and pure memory/sync
   constraints. Rendering a subset cannot turn malformed reports into partial success.
   Namespace lexical string order is independent of source enum order.
3. Add the new method to external forget invalidation before I/O. Preserve the
   existing raw observer receiver so run's internal cancel remains internal. Unknown
   intent retains original bytes and no settings action grants new mutation authority.
4. Complete host-generation invalidation, not just UI suppression. Navigation uses
   wrapped observer.cancel rather than forget-only invalidation, covering pending
   settings results and retaining mutation uncertainty. Check generations around
   awaits and before public output. Existing transport before/after identity checks
   remain installed on both OSes.
5. New controller pauses polling and serializes cancellation using the existing
   ConnectionController cancellation queue. This reuses its proven stop/read ordering
   and avoids the old independent-cancel-versus-new-read race. No extra scheduler,
   mutation coordinator or durable store is needed.
6. Shared table-like settings/presence/origin UI uses human labels and unverified
   runtime/path notes. Explicit-null remains separate from omission/default even
   when safe values coincide. Existing editor/mode panels retain their own authority;
   unsupported capabilities are visible gaps. Data remains in current view only.

## Risks / Trade-offs
- Presence-only output intentionally cannot diagnose provider endpoints/models or
  hidden identity equality. State this as the saved-view boundary, not redaction
  pretending to be effective configuration.
- Pure typed value validation deliberately leaves path admissibility unverified.
  The all-true path summaries must never become green validity/ownership checks.
- Navigation cancellation affects pending shared-host work. It preserves the current
  unknown/receipt contract and must be covered with actual helper and Electron guards,
  not fixed by disabling them in fixture tests.
- Old installed binaries may reject the selector. Unsupported is explicit and
  creates no successful default snapshot; release equality does not prove capability.
- The separate producer and consumer changes must be composed before final delivery.
  Prior archive/canonical ownership and Git-tag-only versions remain intact.

## Verification and delivery
Use attributed actual CLI reports only after producer implementation; verify exact
report hashes without reserializing expected bytes or relabeling synthetic vectors.
Read-only transport peers and faults use public synthetic identities/sentinels.
Test raw/reduced strictness, all origin/value edge cases, bounds/exit/UTF8/duplicates,
late same-ID/navigation/cancel results and live forget ready/unknown interoperability.
Use real public auth/arity/frame guards in dev and retained packages on Linux/Windows,
inspect responsive captures, then independent review, own canonical sync/archive,
actual producer composition and final paired delivery/main-publication observation.

## Open Questions
None blocking in the agreed producer wire. Independent precode review5584741044 accepted exact5def25f before implementation. Implementation and narrow fixture corrections have independent accepted reviews through5586997048. Exact-head run39444594715 passes both OS package paths; final composed lifecycle review and normal delivery remain separate gates.
