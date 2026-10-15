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

Required new PR CI and independent source review remain pending at this checkpoint.
SDK's final PATCH has no notes/body input and was directly audited as unaffected;
no speculative SDK change is included. Root retains publication observation and
the REM-56/human-note closeout. Source basis: actual new hosted logs, pinned
maintained source, current narrow diffs, owned control output and Root's explicit
recovery decision.
