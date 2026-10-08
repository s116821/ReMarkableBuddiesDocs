# Development capture observation consumer integration

Status: development consumer source implemented; independent consumer/artifact
review remains open. No target packet or qualification.
SDK plan/source authority is `f0e6ff4ccb37b887f7f278b0b820a7d047de1559`,
`openspec/changes/establish-native-platform-contract/capture-observation-plan.md`.
Consumer starting revisions are Buddy `89fd9d23e13bb81493239d28e67e39afcebad754`
and Docs `33a294618b37789a6827df0ea40a25e89e71b714`.
Implemented consumer checkpoint: Buddy `42e4b02f81a5433ce3d6b9503036761ae82a16a3` (supersedes `0d70596837da54cfc7ef5c73b72fdc75b1f7b086`).
Main operates the tablet; Astra owns SDK source investigation; Sol owns consumer
implementation and review. Shared storage/domain work is outside this integration.

## Scope and admission

Integrate the SDK's default-off development capture option into the existing
READ-FACTS development workflow. Preserve the original setup120000/read5000,
host150000, rollback180s and restoration240s clocks and their original origins.
The distinct capture request does not publish facts or renew setup time. Successful
capture returns to the remaining original setup wait; failure or unknown ends the
attempt with restoration still owed. No second capture, input, heap fallback,
fixed sleep, debugger or general command endpoint is introduced.

Use a separate fixed-purpose capture publisher and strict completion decoder.
Bind the request to the exact nonce, candidate process/start, root device/inode,
payload and executable hashes, original waiting profile and current closure state.
Use private no-follow files, held directory identity, exclusive temporary creation
and no-replace publication under the existing admission lock. Ambiguous publication
is never retried. Reject stale, wrong-purpose, replaced or duplicate requests.
During atomic publication only the identical held-inode temporary alias is
permitted; observed release is sticky. Final facts publication requires temporary
absence. Legitimate SDK image/completion phase advance after a known capture link
does not itself make token publication unknown.

The decoder consumes only the SDK plan's exact version1 field set and types,
including all five false authority/order flags. Validate expected document and
expected order[index] without presenting caller order as observed order. Require
unchanged begin/end epoch, monotonic capture times, completion strictly before
both accepted+5000 and original setup120000, bounded dimensions/encoded bytes and
the SDK-owned SHA256 of the exact PNG stream. Independently hash the retrieved
native-resolution PNG and match its dimensions and byte count. Header inspection
is format sanity, not a full PNG decoding or visual proof.
Begin/end epochs are positive canonical decimal strings, at most20 digits and
within unsigned64 range; the new capture epoch starts at1. Require each image
dimension to equal the corresponding window dimension times DPR rounded to the
nearest integer with positive half values rounded upward. A backend returning
another size refuses this diagnostic continuation rather than weakening binding.

Main must review the complete retrieved image against the expected opened fixture.
A library thumbnail, byte equality, token publication, engine readiness or a
successful grab cannot substitute for this review. Persist the explicit visual
decision with completion/image hashes and candidate identity. The selected facts
publisher requires this positive decision and exact completion/image binding;
mere file presence is insufficient. Keep ordinary legacy facts mode unchanged.
The fixed fifteen-field local decision includes kind/version, candidate/root
identity, document/page/index, completion/image/request SHA256, explicit
visual_open_fixture boolean and reviewer Main. Its hash is supplied independently
from Main's local artifact. The final wrapper has a source-only literal placeholder;
Main freezes that exact recipe only after full decoding/visual review and requires
the remote decision bytes to match the literal. The initial packet records the
wrapper template hash and does not enable or transfer the final recipe.

Main preselected one logical90,260/native164,1396 input for later preparation.
Both native axes must differ from the released kernel seed; otherwise consume and
refuse, without alternate point or replay. The expected fixture is document
e7f661f1-db6f-4dfc-854a-b38aff7f75de, first page
a7181850-3f03-4bb0-8b9e-01acfc20032e/index0 of the existing six-page order.
The selected facts publisher and collector require index0. No fresh nonce, build
or target trial is selected by this recipe decision.

SDK owner invalidation remains sticky through visual review and final facts
delivery. The consumer never refreshes that witness or grants native/render
authority. Final observed facts must agree with captured document/page/index.
Transport uncertainty, changed candidate/root, late completion, malformed output
or negative visual review prevents facts publication and preserves evidence.

## Evidence preservation and verification

Record verified saved copies before subsequent live guards, so a later refusal
does not erase knowledge that bytes were preserved. Delete a generated image only
after verified local bytes/hash or positively established absence; unknown output
or transport retains its exact owned path. Restoration and fixture hash checks
remain independent duties even after admission expires.
Preservation covers the PNG, completion, request/temporary alias, visual decision
and separately prepared final facts recipe. The exact-name cleanup is reached only
after matching local byte/hash copies or positive absence. Unknown output retains
the stage after stock restoration. Ordinary transport is capped10s, copies5s,
existing live observations3s; a returned late copy can be preserved before a later
live guard refuses it. New config source explicitly binds capture=true/input=false.

Meaningful host fixtures cover missing/extra/wrong-type completion fields, identity
and expected-page mismatch, epoch change, exact deadline boundaries, nonmonotonic
times, image dimensions/digest/bytes mismatch, stale/cross-purpose/duplicate token,
candidate loss before/after copy, negative/missing visual decision, and one facts
publication only after the actual selected gate. Exercise the source workflow
with mocked transport; never run it against the device from Sol's lane.

Host fixtures establish parser and admission behavior only. The retained50d Qt
and heap images visually show the PDF's first page but lack this owner witness;
da8's document-open logs plus My Files capture do not qualify render freshness.
SDK tasks2.9 and consumer task4.11 remain open pending real native evidence and
the complete OpenSpec lifecycle. No canonical sync/archive or shipping claim.

Executed consumer checks: proof156, mocked transport collector40, actual source
integration15, publisher26 host and vendor/QEMU cases and a real wrapper local-hash/replacement
fixture. SDK focused25 plus actual entry/publisher interleaving1 passed vendor
Qt6.10.3/QEMU offscreen; Main and Astra independently reviewed SDKf0 and Astra
reproduced those cases. These are source/host checks, not native render proof.
Consumer independent review and Main's native artifact/packet gates remain open.

Source basis: current repository source and SDK plan pinned above; retained50d
local images inspected directly; da8 evidence summarized in the owning
`qt-input-observation-plan.md`. Consumer source is implemented and tested as stated,
with no hardware verification or qualified capture claim at this checkpoint.

### Independent review correction: raw duplicate keys

Main identified that PowerShell ConvertFrom-Json can collapse duplicate names
before the exact field validator sees them. The collector now bounds the raw
completion to 8192 UTF-8 bytes and enumerates System.Text.Json object property
names with ordinal uniqueness before decoding. JSON escapes are decoded during
this check, so escaped aliases of the same name also refuse. Neither duplicate
case receives capture_verified or saved-copy knowledge; remote unknown outputs
remain retained under the existing preservation rule. No schema changes.

Actual mocked raw completion regressions cover identical and escaped duplicate
version names. Collector40 and source integration15 passed after this correction;
Main separately reported independent proof156, prior collector34/source15,
vendor ARM/QEMU publisher26 and actual wrapper replacement refusal. These are
source/fixture checks only; device qualification and task4.16 remain open.
