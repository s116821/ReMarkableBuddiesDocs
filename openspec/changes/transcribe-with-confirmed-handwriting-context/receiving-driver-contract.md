# Local receiving comparison driver

This increment supplies a test-only driver through the existing same-Store
Writer image receiving and explicit confirmation methods. It adds no public CLI,
provider, registry or native ingress. Its only engine is the existing synthetic
test engine; real-provider execution is unavailable in this driver.

Before any receiving operation, admit exactly one seed and one to three target
original PNGs. Reject repeated seed/target or target/target image hashes, invalid
images and an empty or oversized target set. These checks establish byte
separation only, not same-writer provenance or semantic disjointness.

Use one ordinary-local Store and its actual Ledger/Dispatch owners throughout.
Run each target once with enabled empty-profile selection, then receive the seed
once, resolving its actual NormalizedText correspondence. Exercise one distinct
caller-asserted explicit confirmation intent with frozen operation/input and
expected heads through the existing confirmation API. Do not add authentication
infrastructure or claim a synthetic fixture is a real human/native UI event.
Run each target once more with the confirmed seed selected. All receiving uses
the production normalizer/request builders and downstream Generate path. Keep
operation/source/turn identities distinct, preserve reports through output, and
do not retry failed model calls, confirmation or receiving operations.

The bound is seven Writer operations and fourteen synthetic model calls: three
empty-profile cells, one seed, three confirmed-profile cells. Fewer targets reduce
this bound. The fixed baseline-first order is a mechanics control; a later live
comparison must independently review ordering and corpus admission rather than
claim randomized or blinded efficacy from this driver. Frozen target truth must
never be a driver/request input. Synthetic replies are explicitly test data.

Focused controls cover the full six-cell path, actual normalized-source
confirmation/provenance, example presence only in normalization, stable seed
identity, duplicate/oversize refusal before calls, and first-call failure without
retry or confirmation. Existing runtime controls retain coverage for captured
ownership through errors, stale revisions and replay refusal. Passing these
controls establishes receiving mechanics, not handwriting benefit, pen input,
native confirmation, representative learning or the frozen mathematical gate.

A separately reviewed corpus must identify supported seed transcription,
caller-asserted explicit confirmation provenance, distinct same-writer pages and
evaluator-only target truth before any real-provider comparison is selected.
Missing corpus does not block this local driver. The active change remains open
for its uncompleted recognition, learning, native and coordinated delivery gates.
