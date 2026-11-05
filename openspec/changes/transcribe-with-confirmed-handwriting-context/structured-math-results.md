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

The exact-source Linux host Checks job passed in
[run 42103299628](https://github.com/s116821/ReMarkableBuddies/actions/runs/42103299628).
All three Docs checks passed on `79620ff`. Application Build/Integration and the
remaining delivery gates are separate from those host results.

## Finite live comparison

The fresh four-call Terra experiment completed once under the prospective method
`245c4ec8c9cb789ca1030e30cc9847b4cc69f6b18cdb9f873669968590f2a61c`.
It preserved the prior source glyph/attachment criteria, target/context image
bytes, original condition order and call bounds. All four calls returned complete,
technically valid structured reports; Store remained unchanged. No retry, output
repair, altered reference or replacement cell occurred.

**Semantic criterion NOT MET: strict usable structure 0/4; full expression
fidelity 0/4.** Two reviewers independently froze their arm-blinded scores before
mapping disclosure and agreed on every criterion and outcome. Sample identity and
historical failures were known; this was not outcome-naive or sample-blinded.

| Sample / context | Retained output | Semantic failure |
| --- | --- | --- |
| A / absent | Union, below-limit, T subscript 0 and final-Q script | `=` replaces `:=`; `<=` replaces membership |
| A / selected | Union, membership, below-limit, T subscript 0 and final-Q script | Required colon omitted |
| B / absent | Fraction and radical with opaque radicand | Required subscript outside the radical, inside the denominator omitted |
| B / selected | Fraction with known numerator and opaque denominator | Required radical, radicand and external subscript relationships absent |

Both B outputs are safe partials only in their retained assertions; neither
preserves the required usable structure. Both A outputs declare complete coverage
but contain recognition errors. No foreign technical-context content was observed.
Representation capacity and valid syntax do not establish correct recognition or
causal context improvement. Historical v2 math 0/4 and legacy 6/6 remain unchanged.

Reproducibility identifiers:

- Source `7398569235bd9c329b832d06bdbae188502651da`; paired Docs at execution
  `79620ff73ab3d1abf5ef57a1c96dcb317f415212`.
- Packet `6c631d3d8e783fdbbdf07ef21ac43bd792319bb3d5c88f3054114c52475f014d`;
  actual candidate `58e1f61f02326e84a59285ab5fb47cb4b59ee009fb9e11d258c3ee6c66894f0c`.
- Collection binding all raw/report/meta/terminal receipts:
  `86158ca375992ee6e0ac812cf02ba0306fa6e59aaf630f7700d83cd9927c6ac3`.
- Root blinded score `50ac0bc43661f66ce8c971a9b27053b3a40e7350fe00727968e9ff3b8913e1cc`;
  independent score `0f3423408a6338a2faeb08984d7737844a34a950744d1c581277114e09c816d8`.

Keep this change active and unarchived. A successor must address the demonstrated
recognition failures and satisfy the existing acceptance criteria; this completed
experiment and all historical failed packets must not be replayed.
