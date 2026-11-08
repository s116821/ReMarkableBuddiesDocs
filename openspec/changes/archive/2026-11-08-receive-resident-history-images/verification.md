# Resident historical receiving verification

Implementation revision: `2555cd6bd4602954626620426e39187c7b4e9045`, tree
`6cf993e6bc34458132141a951d690270916661d9`, based on delivered
`cf568ae05af6a585babf349c1df8507febcfce32`. The subsequent source head
`5f6a873a62121a0d9b78deb157b7bd990fb8d8d4`, tree
`3f942684bfe1f0acc62f06626dd28bdf76c69d29`, changes one sentence in
`docs/simulator.md` only. Compiled evidence remains attributed to `2555cd6`.
The Docs change starts at `a1f446b8c4857e4f17726a0cb40ed62b8048b71a`;
the exact paired Docs commit is recorded at delivery, avoiding a self-referential
commit identifier here. The finite correction is synced and archived in this
paired delivery after independent source and live-result review.

## Regression and implementation checks

The before-fix actual Reader receiver test reached its model payload and failed
because zero historical attachments were supplied instead of four. Its raw log is
`before-reader-second.log`, SHA-256
`461039cd5393fe1bbcca6234a6513e44e687939e229e8b5ceeb8c8cc533b3ed8`.
The earlier `before-reader.log` is a separate fixture-setup failure caused by
reused operation identities; it is retained separately and does not prove the
receiving defect. `before-reader-inputs.sha256.json` pins the before inputs.

The corrected actual Reader regression passes. The final combined module run
passes all 15 tests, including real Reader/Writer/notebook receivers, seven-stage
resident qualification, exact frozen-context reuse after a source-head change,
cross-capture/ImageUse digest deduplication with all nine source associations,
false derivative recipe refusal before all three receivers, missing/corrupt media
refusal during Writer refinement, and cumulative proof admission before missing
object reads. The initial cumulative-byte test fixture did not exceed the bound;
that separately retained failure was corrected by declaring repeated shared
provider-image work without exceeding the unique attachment allowance.

Existing attachment limits remain twelve unique images, sixteen MiB and 256
associations. Resident proof admission uses checked accumulation before object I/O:
twelve captures, sixty-four MiB original-plus-derivative declared bytes counting
repeated work, and twelve times the existing SDK original-pixel bound. The existing
resident validator checks original/derivative bytes and exact recipe derivation;
only its validated provider derivatives are attached. No shared capture interface
or acquisition authority changes.

Affected integration suites pass: `simulator` 44, `source_request_context` 76,
and `writer` 41 tests, totaling 161. Strict all-feature/all-target Clippy and the
final formatting check pass. Docs verifies its manifest, 36 guidance files and
126 preserved source blobs; strict OpenSpec validation passes all 127 items.
The exact compiled-input manifest is `source-inputs.sha256.json`, SHA-256
`caa24712a661ec2fa325e630c22610c292215f9ed7471cfc28761a4f4877fb59`.

## Maintained offline executable case

The real CLI ran the maintained `combined-qualification-resident.json` scenario
with only its output destination changed. It completed in scripted-offline mode,
reported no credential resolution, and recorded attachment counts
`[4, 4, 4, 4, 0, 4, 4]` across the ordinary Reader, Writer Generate, Writer Refine,
Reader handback, notebook map, notebook reduce and notebook Reader handback.
Exact history, retained drafts and reducer input digest checks passed. Native
effects and external exports were zero. The original remains provenance only.

The report records clean source `2555cd6` and build
`dev.v0.77.0-2-g2555cd6`. Its SHA-256 is
`5d62112792aea10fde84a8e1f97d05796efadb57e6f35a3a9fb6513c3ee380f8`.
The Linux executable has SHA-256
`fa4f5238d160405691201825028d16732b8f3f4dafc8b7109f8a3548fd2a221e`
and size 481481664 bytes. No metadata-only rebuild reattributes this evidence.

Raw logs and manifests are retained for the delivery evidence comment; they are
not duplicated as execution archives in the reusable source diff.

## Current Windows build and live qualification

A new Windows build at clean `5f6a873a62121a0d9b78deb157b7bd990fb8d8d4`
used the locked dependencies without incremental data or debug symbols. Its
53,211,648-byte executable has SHA-256
`055e64083ea1c6298951429d1757961c1c0827e151e1383b29fe8ae2ca32c6c4`
and embeds `dev.v0.77.1-2-g5f6a873`. Its separate scripted seven-stage smoke
completed with no credential resolution, native effect or export. That report
hashes to `3d9ae96a2f17fcd9c62680b4cf42eac97faee404d53ccee6366cc6f8c75da844`.

The independently reviewed, freshly selected resident live case then used the
same executable and original fixture with `gpt-6.1-terra`. Only the maintained
scenario's output destination changed. Seven requests returned in 29.188 seconds;
the child exited zero, with no outer timeout or retries. Each request was capped
at ninety seconds and 4,000 requested completion tokens. A hard 720-second
operator process cutoff supplemented the runner's cooperative deadline; late
results or outer timeouts would not count as success. Prompt and image tokens
are additional to the requested completion-token cap.

Independent raw-result review confirmed:

- Reader recovered Source A as 2 kg times 3 m/s² equals 6 N from the retained image.
- Writer preserved the source label and units; Refine added the requested
  dimensional-analysis sentence, and Reader handback identified that addition.
- The image-free notebook map calculated Source B as 10 N and explicitly declined
  to invent the unavailable Source A values or comparison.
- The reducer received the exact map reply plus Source A's four derivatives,
  calculated the correct 4 N difference, and kept source attribution distinct.
  Final Reader received that note verbatim and correctly attributed Source B's
  numbers to the note rather than claiming direct original-text access.
- Ordered attachment and encoded digests, byte counts, dimensions, source IDs,
  ordinals and attachment indices matched across the relevant stages. Counts
  were `[4, 4, 4, 4, 0, 4, 4]`; each independent conversation retained its own
  source identity. The original PNG was not an attached derivative.
- Exact history, two ordinary drafts, one notebook draft and the independently
  recomputed reducer input digest were retained. Memory queries, native effects
  and external exports were zero.

The original live report SHA-256 is
`c2ab6105c342ae13ea883eb6f5090a5a1c4c0e28502e4b0ffe8cbbda86f82a16`.
Its terminal manifest SHA-256 is
`69dcebf439556fe03fdad998970ceec82406d099b7e8337ff690d9118a09425c`.
The consumed run's packet, selection, spent marker, exit, output and report remain
original evidence; the selection is not reusable. The executable and build cache
are reproducible outputs whose retention ends after this evidence review.

Current source [CI 42428900243](https://github.com/s116821/ReMarkableBuddies/actions/runs/42428900243)
passed Checks, application Build and Integration. The paired delivery is
[Buddy #146](https://github.com/s116821/ReMarkableBuddies/pull/146) and
[Docs #158](https://github.com/s116821/ReMarkableBuddiesDocs/pull/158).

This accepts the finite ordinary receiving correction with a synthetic historical
fixture. It proves neither native acquisition, currentness, tablet output,
handwriting recognition nor aggregate integration. Those parent obligations
remain unfinished; earlier ImageUse evidence was not substituted for this run.

The parent ordinary-memory checkbox is reconciled using the separately delivered
[ordinary memory verification](../2026-11-06-integrate-ordinary-memory-callers/verification.md)
and its canonical subject-memory requirements. Other parent integration tasks
remain open.
