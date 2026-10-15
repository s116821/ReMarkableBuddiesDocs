# Exact-note serialization follow-up

## Observed actual main outcome

Manager source `959205e73210bdc2fec73faf6bd5b6c3328997d1`, candidate v0.4.1,
[push CI38711594306](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/38711594306)
passed checks, candidate, build and both retained-artifact integrations. Final
publish job `116347881067` created the annotated tag/draft, uploaded the original
build bytes and completed same-ID/all-remote-byte verification. The final
request-action input parser then failed before PATCH with `end of the stream or
a document separator is expected (3:7)` at the notes' `Source:` line.

The recorded draft is `413626090`/v0.4.1. It remains unpublished failed evidence;
Root explicitly selected normal new-main publication after the source repair,
without manual finalization, retroactive source substitution or an old-byte rebuild.
The original workflow/run cannot adopt this successor code by rerunning failed jobs.

Buddy [push CI38711588008](https://github.com/s116821/ReMarkableBuddies/actions/runs/38711588008)
at `1d1b480db048bd7fab8e336c03822babf41d1221` had passed checks and frozen v0.2.1.
Root canceled while build alone was active. Terminal build/integration/publish
statuses are canceled; CI result is failure, not a passing gate. A read-only Git
ref API request for Buddy v0.2.1 returned 404 after cancellation. No tag or complete
artifact integration is inferred from that interrupted build.

## Narrow source and owned control

- [Buddy PR47](https://github.com/s116821/ReMarkableBuddies/pull/47), exact source
  `b67686156c31bf0a9c4268a1f7102ad6372888f2`, parent `1d1b480d...`.
- [Manager PR20](https://github.com/s116821/ReMarkableBuddiesManager/pull/20), exact
  source `bb6c65316428c829e91caed90e6514cb1122f172`, parent `959205e7...`.
- Paired central [Docs PR39](https://github.com/s116821/ReMarkableBuddiesDocs/pull/39)
  starts at `9fe07b460d3a868a82dc0e7db7e08ba82d74e6eb`; precode was committed
  as `40729117fd95ed73a4ce9d1e38c92edf31c476fd` before implementation.

Only two source paths per repository change: `.github/workflows/pipeline.yml`
encodes the final body with `toJSON`, and `release/fixtures/actions.test.mjs`
extends the existing actual maintained-Action control. No dependency, package,
candidate, tag, draft-ID, verification, uploader, application or native code changes.
The unchanged request Action pin is `b91aabaa861c777dcdb14e2387e30eddf04619ae`.
Its actual source calls YAML.load on each input; a JSON string is a YAML scalar
whose parsed value is the exact original notes text.

The owned Node 24.21 Windows run executes that pinned Action against loopback:
raw multiline notes fail before any PATCH and keep the draft true; JSON-encoded
notes produce one PATCH whose body preserves LF, colons, quotes and Unicode;
the returned body equals the original. A production-expression assertion prevents
the fixture from passing while the workflow still supplies raw notes.

RED against the original workflow is retained (one failure, 2.751 seconds): it
reaches the expression assertion after the raw-refusal and encoded-roundtrip
assertions have passed. After the one-line workflow repair the same affected
control passes (one test, 2.448 seconds). Outer stdout/stderr logs are retained in
the owned tool directory; no separate raw child execution receipt or independent
native/production test is claimed. No unrelated matrix was rerun locally.

The initial checkpoint awaited new PR CI and independent source review.
Subsequent independent source reviews found no source issue at those exact heads:
[Buddy review5530992550](https://github.com/s116821/ReMarkableBuddies/pull/47#pullrequestreview-5530992550)
and [Manager review5530992703](https://github.com/s116821/ReMarkableBuddiesManager/pull/20#pullrequestreview-5530992703).
Their conditions are required exact-head CI and this own Docs lifecycle.

The actual hosted Manager uploader job `116350300948` on merge `3b73424...`
rebuilt the same qualified bundle and passed all four metadata-Action controls;
the expanded exact GraphQL/request case passed in 0.781 seconds. The unchanged
four uploader controls also passed. This proves the repaired owned-loopback
serialization control, not production recovery of the retained failed draft.

Docs checkpoint `37969a2e09a7aa162db31de5f2505efc9e3975a4` passed
[CI38713693772](https://github.com/s116821/ReMarkableBuddiesDocs/actions/runs/38713693772)
on merge `5a7f996...`: portable 12 tests passed in 0.390/1.914 seconds, both hosts
verified guidance 19/126, and strict validation passed 21 prearchive items. Source
CI was still in progress then; no earlier PR/main result substitutes for that gate.

## Final source gates and named lifecycle

Buddy source `b67686156c31bf0a9c4268a1f7102ad6372888f2` completed
[CI38713428967](https://github.com/s116821/ReMarkableBuddies/actions/runs/38713428967)
and its title check successfully. Hosted merge
`7ecd9b5f960409d9156fe6bf06f9ba26fa41eb04` built artifact `11962656383`, outer
SHA-256 `c3e0a9111d7bddf8964dbbec9ceb5237877825af5af1e5b73de51add5fe5ba32`.
Integration `116355813985` downloaded that exact ID/digest and executed both
retained ARM binaries, reporting 0.2.1 under pinned emulation with native explicitly
unqualified. PR publication correctly skipped.

Manager source `bb6c65316428c829e91caed90e6514cb1122f172` completed
[CI38713434097](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/38713434097)
and its title check successfully. Hosted merge
`3b73424e46d6c69ee3afdc94af7dab3495cc2c85` built production artifact `11961399111`
(outer SHA-256 `2c8d2045189217bce79f65258f685ef037754bb351636753652f0f96049f0f5d`)
and CI-only development artifact `11961249381`
(`69cf3ebadbc5c3189b0cfdbd324673a7276b147f96768842bd46252e0bcc61d0`).
Both host integrations consumed those exact IDs/digests, exercised development
Tailwind and retained browser/Electron/packaged/wired fixtures at 0.4.2 and verified
the production packages afterward. PR publication correctly skipped. This is
hosted PR evidence, not a new-main publication or recovery of the old draft.

Completeness: all four bounded implementation tasks are complete. Only the five
own files are archived at `2026-10-15-release-notes-input-serialization`.
Correctness: the one modified canonical publication requirement retains its three
existing scenarios and adds the exact-text scenario; actual pinned Action controls
and required exact-head CI passed, with independent reviews linked above.
Coherence: no maintained library, dependency, artifact or release identity behavior
was replaced. Original main failure/cancellation and failed draft remain evidence.
Final archive-only Docs CI/readback is recorded in the PR handoff; this report does
not claim future main publication already succeeded. Root retains that observation
and overall issue/human-note closeout. No native or provider qualification follows.

SDK's final PATCH has no notes/body input and was directly audited as unaffected;
no speculative SDK change is included. Root retains publication observation and
the REM-56/human-note closeout. Source basis: actual new hosted logs, pinned
maintained source, current narrow diffs, owned control output and Root's explicit
recovery decision.
