# Reader receiving increment: local results and open gates

## Revisions and scope

Central precode e4e452d was published before implementation. [Buddy PR49](https://github.com/s116821/ReMarkableBuddies/pull/49) reuses accepted configuration6254092 as the single four-file cherry-pick4e947c1 over accepted ordinary-mode sourcea3b1c75. New receiving source is c2dc54e3e14598585b7dc417ea502c2bd30a797b; successors6097a31 andbe95c29 add only public live-check guidance and one minimal simulated screenshot. [Docs PR41](https://github.com/s116821/ReMarkableBuddiesDocs/pull/41) owns this active change. These remain stacked draft candidates, not source-main deployment or completed REM-53.

## Actual local evidence

Windows, Rust1.98.1, locked/offline/all-features, one Cargo job:

- Existing optional-memory/default workflow check: one pass16.39s before the new matrix.
- Final affected subject-memory workflow suite: four passed34.39s. The new control covers enabled/disabled/empty preferences, absent/empty/populated memory, recognition disagreement, exact-once JSON framing, original images/question, no fake transcript turn and immutable snapshot after a later configuration edit. Scripted replies do not establish model semantics.
- Accepted configuration integration suite: five passed7.43s, including actual maintenance CLI with no credentials/device, multiline readback, disable/clear, bounds, conflicts and snapshot behavior.
- Final actual HTTP loopback test: one passed0.21s, with two branches covering unchanged memory-only framing and separate multiline Unicode preference framing. Dummy credentials and synthetic replies; no external provider.
- Maintained `personalized-answer.json` executed through the actual CLI: three model calls, unchanged source, one navigation, two text operations, no errors or assertion failures. Report identifies `scripted-offline`; answer PNG was viewed and shows one readable simulated answer block. Bitmap punctuation/case is approximate, not native typography.
- Final all-target/all-feature strict Clippy passed17.75s; formatting/diff checks passed. Private raw logs remain under the existing task evidence directory as `rem53-reader-{workflow,protocol,scenario,clippy}-r1.log`.
- Central validation:19 guidance files/126 preserved source blobs verified; all19 strict OpenSpec items passed. Hosted checks and independent review are not replaced by these local results.

![Scripted simulator answer, not live model or tablet output](https://raw.githubusercontent.com/s116821/ReMarkableBuddies/be95c29/docs/validation/images/rem53/personalized-answer.png)

## Open gates

The launching process and scoped ignored local configuration have no provider credential. No real-model result is claimed. The maintained `live/personalized-reader.json` and public setup guide supply the concrete representative run; actual preference, explicit-request and fixed-output precedence must be assessed before merge. Independent source/spec review and final hosted checks remain open. Keep this change active and unsynchronized/unarchived until its required gates are satisfied.

Only ordinary Reader startup consumes the preference in this increment. No Writer, routing, gesture preset, running reload, controlled service restart, effective running-config receipt, Manager active state, selected sync or native output qualification is claimed. Disk maintenance continues to report restart-required. Whole REM-53 remains open.

## Current-main reconciliation preparation

The existing Reader branch is being reconciled with current main under the independently reviewed ordinary-only integration plan. Source caf4ee5 and its earlier provider/simulator evidence remain historical. Precode245a010 and7bdf708 add the ordinary LocalMemory-only boundary, early selected-configuration refusal and selected-result helper refusal before source changes. No new model or tablet call has occurred.

Normal Docs integration composes actual main0f900e3 while preserving all819 main entries outside the six owned active Reader paths. The complete original Reader/parent heads stay in merge ancestry and all other active branches/evidence remain intact. Existing source/Docs branch names already target main; actual base commit, full integrated tree and fresh hosted checks still need verification.

The integrated pre-code tree passes92 strict OpenSpec items and guidance25files/126preserved source blobs. A full cached diff check against the old stacked HEAD reports two blank-at-EOF lines in main-owned conversation-layout-projection and sanitized-conversation-feedback specs. Both files are byte-identical to actual main and are intentionally preserved, not silently repaired under this change. The scoped Reader diff against actual main passes. These are specification/preservation checks, not source, provider, runtime or native qualification.

## First integrated source failure

Sourcefb61144 normal merge preserves originalcaf4 and current main6e33 with533 entries and520 unrelated main entries exact. Docsceb6992 preserves all819main entries plus six own active files and passed all3hosted jobs40332500247 (bothOSportable12-test groups;92strict specs). Source40333967860 passed format/strict all-target/all-feature Clippy, then failed library tests:547passed/1failed/3existingignored. Build/integration skipped; later external protocol/CLI controls are not credited executed. Full failed logs are retained.

The new withholding/cancellation control reaches its first withholding case, then fails the persisted terminal-user expectation: current Ledger::advance_fact disallows Interpreted→Failed/Canceled, so recording the contextual failure refuses and leaves the verified user interpreted. No preliminary answer or assistant was published in that reached case; later loop cases are unexecuted. The proposed ledger refinement preserves the expectation and requires new exact-head tests. No actual provider/tablet action occurred.

## Repaired integrated host qualification

Source successor ea13cbc285a776fd393630a4b4e586aa85604d1f implements the independently accepted narrow fact-only terminal transition; the workflow failure expectation is unchanged apart from its case diagnostic. The normal40338517090 pipeline completed successfully at exact reviewed treec46d610d8933c89624f29c7543f0c64db2016ba2: title, Checks, package Build and Integration passed; PRRelease was skipped. Its actual checkout115cfe70238f1ece3cf7c702f6be72bd1bcfeb7d has parents6e33+ea13 and the same tree.

The completed Checks job121626566616 raw log confirms548library tests passed/3existingignored and11binary tests passed. All eight new named controls individually pass and are included in their suite totals: three ordinary workflow controls (preference isolation/default-memory/withholding and cancellation) and five external controls (two-branch actual loopback framing, selected-config early CLI refusal, actual selected-query engine exclusion, nine actual ledger terminal/replay/reopen/refusal cases, and actual CLI maintained scripted preference scenario). Internal parameterized cases are not additional top-level counts. Earlierfb61144 failure, inherited EOF diagnostics and the separate owner-created delta EOF correction remain preserved.

Docs652ca2f normalized only the owned new ledger delta ending and passed all three hosted40338966572 checks plus local92strict/25guidance/126preserved and own diff checks. A further normal Docs integration now composes delivered mainec94b0c after the independent Manager credential consumer delivery; all unrelated current-main entries must remain exact. The Sourceea13 qualification is unchanged and is not rebuilt for this Docs-only update.

These are host/scripted/local HTTP and emulated package checks, not actual provider semantics, hardware, selected/native output, service restart/reload or full personalization acceptance. The existing live Reader criterion is still open. A draft single-case three-call proposal is preparation only, not a budget or execution admission; its maintained simulator report records returned question/answer and classified trace/counts rather than every raw wire message. Preserve that evidence distinction and obtain the exact reviewed execution packet before any new model call. No canonical sync/archive or merge/release acceptance is claimed.
