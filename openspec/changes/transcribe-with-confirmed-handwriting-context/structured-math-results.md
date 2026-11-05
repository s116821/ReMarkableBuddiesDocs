# Structured mathematical transcription implementation

Implementation revision:
[`7398569`](https://github.com/s116821/ReMarkableBuddies/commit/7398569235bd9c329b832d06bdbae188502651da).

This successor implements the separately reviewed version 3 boundary in
[structured-math-contract.md](structured-math-contract.md). It adds no automatic
consumer, confirmation, renderer, source allocation, training or native action.
Historical math failures remain NOT MET; the separate six-case legacy-policy
regression remains attributed to source 5403ae1 and its original receipts.

The isolated parser and complete standalone prompt/context were independently
prepared, then integrated into the actual operation, normalizer and report.
The accepted design preceded code. Root reviewed the parser's shared page
budgets, closed forms, exact ordered child roles and opaque unknown children.
The new literals have explicit LF checkout rules. Neither target labels nor
expected target trees appear in the production prompt.

Actual Windows production checks pass 28 transcription tests, 10 parser module
tests and both CLI subprocess tests. The production tests cover v3 admission,
exact provenance and unknown-child round trips, legacy receiver refusal,
duplicate/trailing/deep/oversized replies, selected Store ownership through
cancellation and report overflow, and the existing literal outcomes. Module
controls exercise shared span/node/text bounds, every arity, depth, exact Unicode,
inert strings and positive structure. Wrong source glyphs and attachments can
still be valid syntax; those tests explicitly preserve that limitation.

Six independently serialized identity vectors exercise real prompt/profile
recipes with absent, selected, reordered and revision-changed context. Existing
valid v1/v2 vectors and all their expected report bytes remain unchanged. The
first run passed 27 tests and failed one obsolete unsupported-version fixture
that still used version 3. The three unsupported-version requests now use 4;
their refusal expectations and hashes are unchanged. The failed run is retained
separately from the successful rerun, not relabeled as passing.

Prompt SHA-256: `c92df4e91e326044cdefa4ced9978301dd5ba18da75ab28c8a6af47503651c5e`.
Context SHA-256: `1ff470ebb912e42bc7ac081b0e1661292a485ff8796d9fbfccfc4f60322505ac`.
The synthetic identity fixture is in Buddy at
`tests/fixtures/structured-math-identity-vectors.json`.

Independent read-only source review found no actionable v3 implementation issue
and independently reconstructed all six identity vectors. It also accepted the
three unsupported-version fixture updates and the new LF checkout rules.
Windows default-feature Clippy completed with `-D clippy::all`; existing dead-code
warnings remain outside this change. The separate Windows all-feature check with
`-D warnings` failed in unchanged native/Writer platform paths (missing gated
helpers and dead code). That failure remains recorded; it is not a passing check
or a substitute for the required hosted Linux validation.

Exact hosted checks and a fresh reviewed live comparison remain required before
delivery. A prospective four-cell method
preserves the prior source glyph and attachment criteria, target/context image
bytes, model and call bounds. Tree capacity does not repair incorrect recognition
or permit regrading old output. No new model request has run at this checkpoint.
Keep the change active and unarchived until its actual acceptance gates pass.
