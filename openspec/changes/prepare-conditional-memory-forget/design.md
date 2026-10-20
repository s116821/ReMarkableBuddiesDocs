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

## Risks and verification
Own successful mutation changes target selected pins; blindly checking old pins before receipt lookup breaks legitimate unknown-outcome reconciliation. Conversely, fresh substitution would permit a second mutation after later values. Exact original envelope/predecessor matching must precede any new mutation path; receipt-only never falls through. Original mode/config/store changes refuse reconciliation rather than quietly moving it. A cloned actor/mode tree is not sufficient host target identity.

## Delivery
Publish/review exact contract and coordinate consumer before implementation. Verify meaningful real CLI/domain faults and actual corpus separately from synthetic host cancellation; then canonical sync, own archive, final independent review and Docs-first/source-second squash, actual main/publication observations. Current inspection publication remains separately tracked; broad memory/Manager/native scope remains open.
