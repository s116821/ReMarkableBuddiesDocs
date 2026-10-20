## Context
Delivered inspection Buddy69 source4fad1681 and Docs66 source1c736fab are independently reviewed. Their exact actual trees match accepted4e2f8dec/5cb04c1. Inspection is a one-key read and exposes no mutation preparation evidence. The existing regular-file Forget is intentionally preserved.

## Decisions
1. Add separate prepare-forget, guarded forget stdin and read-only forget-receipt selectors. Do not teach ordinary inspection or search to mint write permission. New prepare/receipt selectors accept only exact-dash stdin; existing file operations remain compatible.
2. Preparation obtains preview and conditional evidence from the same configured Store/mode/domain admission and guarded consuming writer. Initial preview permits exactly one valid supported value; empty, tombstone, conflict and opaque states refuse without selecting a head. Producer evidence is conditional metadata, never a serialized live token.
3. Confirmation retains the original UUID/Key/heads/content, explicit config binding, original mode token, Store actor/generation and full local/selected identity. Selected catalog/all aggregate acceptance evidence is independent of mode choice and must be compared to freshly minted live tokens under existing gates. No fallback/rebinding.
4. Separate first execution from exact historical acknowledgement. First execution requires every original pin current. Receipt reconciliation never calls a mutation if no receipt exists. For selected historical acknowledgement the original commit's direct predecessor must match the prepared target; current catalog/other aggregate pins remain exact, while validated later target changes do not invalidate the historical receipt. This conservative policy may leave unrelated-drift cases unresolved.
5. Only acknowledgements of exact original transactions are returned, without a current-deleted promise. Possible dispatch plus lost/partial/failed response stays unknown; no automatic retry, new UUID, replacement heads, optimistic removal or second JSON. Fresh deliberate inspection is required for current state.
6. No new journal/provider/admin service. Add narrow pure bounded local receipt lookup rather than reusing LocalMemory.replay, which routes through Store.commit. Selected original_receipt intent checks remain authoritative, with an additional prepared predecessor check.

## Config and lifetime precision
The invocation loads one explicit config and uses that frozen authority; its original nonsecret binding must match preparation. An external config-file edit after that load cannot retarget the admitted operation, but this is not a claim to atomically observe arbitrary external file edits. The host invalidates intent on known config/target/boot/session changes. Store process ownership, original-token mode lease and selected gates remain held through operation/output. No precondition is a capability to choose arbitrary paths or recreate private SelectionToken.

## Local preview sealing
Existing ordinary Inspection has no selected Pins seal. New preparation must not
reuse that absence as currentness proof: add a narrow Store-owned local conditional
heads/generation guard, compare the original complete envelope/content set under
the Store mutex, then consume the fully sealed preparation report while retaining
that guard and original mode/process lifetime. Do not relock the same mutex inside
the writer or change existing inspect/file output behavior. Selected preparation
reuses its freshly admitted whole-view pins and byte-integrity seal. Meaningful
controls must cover local as well as selected stale/forged/prefix output.

## Atomic local first publication
The original ordinary mode lease does not prevent Store::restore from replacing
inner.generation. First confirmation therefore needs a NEW narrow Store conditional
publication entry point holding ONE mutex guard continuously through original
Store generation, exact parent Envelope content/head-set validation and actual
publication. A precheck followed by LocalMemory::forget/Store::commit is unsafe
and is prohibited. Factor a private already-locked publish helper if necessary;
never reacquire the mutex recursively or change the older file entry point's
behavior. A replacement-generation/same-head test must exercise this exact gap.

## Historical proof boundary
The logical original operation is actor/Key/operation/parents/tombstone, plus
content-hash comparison against every original parent Envelope. Selected direct
predecessor matching adds original accepted target context. Current config/mode,
catalog and other-aggregate checks are conservative present admission, not proof
those fields were checked when the historical operation originally committed.
No persisted full prepared-packet fingerprint exists, and no receipt may claim
that it does. A matching manual/file-origin transaction can acknowledge that same
logical deletion without claiming it used this new preparation protocol.

## Risks and verification
Own successful mutation changes target selected pins; blindly checking old pins before receipt lookup breaks legitimate unknown-outcome reconciliation. Conversely, fresh substitution would permit a second mutation after later values. Exact original envelope/predecessor matching must precede any new mutation path; receipt-only never falls through. Original mode/config/store changes refuse reconciliation rather than quietly moving it. A cloned actor/mode tree is not sufficient host target identity.

## Delivery
Publish/review exact contract and coordinate consumer before implementation. Verify meaningful real CLI/domain faults and actual corpus separately from synthetic host cancellation; then canonical sync, own archive, final independent review and Docs-first/source-second squash, actual main/publication observations. Current inspection publication remains separately tracked; broad memory/Manager/native scope remains open.

## Canonical whitelist reconciliation
The delta also modifies the pre-existing bounded-input requirement's query/inspect-only
whitelist to permit only the separately specified prepared selectors. Its four
existing scenarios remain byte-identical, as do both unrelated requirements. This
is reconciliation of the already accepted protocol, not broader write authority.
Canonical sync remains withheld until implementation/CI/consumer qualification.

## Fresh selected handoff proof
No selected gate is retained across the original operation and post-operation
read. The fresh admitted target must explicitly prove the identical logical
receipt and original direct predecessor again before its pins seal stdout. A
legitimate target activation may append validated lineage; historical acknowledgement
is allowed only when that fresh lineage still proves the exact original request,
never by silently substituting a different accepted context.
