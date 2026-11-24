---
name: reader-buddy-testing
description: Verify installed Buddy Reader on an authorized development tablet, from the physical trigger through the live model to the answer visible on the next page. Use for attended product testing and authorized unattended observation.
---


This shared workflow is maintained only in Docs. Run Cargo, scripts and device
commands from the selected Rust checkout; resolve component paths there.

# Reader Buddy tablet testing

This document is also a manual checklist for contributors using ordinary Git,
Cargo, SSH/SCP and a screenshot viewer; it does not require Codex, connectors or
private Linear access. Use available public acceptance criteria and discussions.
Follow [development validation](../../../CONTRIBUTING.md#development-validation):
when an authorized development tablet is available, build the changed software
and run it on that tablet, exercise the actual workflow and relevant edge cases, inspect the
result, and fix/repeat as needed. Leave automated component/regression suites to
existing CI; host tests, ARM builds and emulation are not tablet acceptance.
Local simulation/emulation is for parallel work while another worker owns the
tablet, or contributors without authorized hardware. Record unperformed native
cases for maintainer acceptance; do not imply hardware was tested.

Coordinate with the person at the tablet for a finger gesture or a visual check.
Unattended device access requires an authorized idle development tablet and full
SSH access. During an attended test, use only the observation or changes agreed
with the person using that development tablet.

Resume from the current branch, saved edits, build artifacts, service state and
evidence before repeating work. A saved successful build or screenshot proves
only its recorded state. Record the source revision or diff and binary checksum
for each hardware test batch; distinguish earlier results from the current build.

## Device and service coordination

- Identify the device and firmware from live state. Authorization for a development
  tablet does not extend to a paired personal tablet. Announce device changes and
  honor the user's existing scope; this skill grants no new mutation permission.
- Use the single installed Buddy service with its normal configuration and live
  provider. Verify the running build before the test. If the service cannot start,
  diagnose startup and repeat the affected flow once it runs. Exercise one-shot
  binaries, scripted input and model stubs off the tablet in the existing CI
  pipeline or simulator.
- Check free space on both the installation and notebook filesystems. Measure the
  notebook filesystem again after staging. The tablet can refuse to add a page
  while it still reports free space. Stage on a suitable writable partition, retain
  a verified rollback, set executable permissions, then replace atomically. Reload
  service definitions only if changed. Verify the installed binary checksum and
  actual restart behavior; a successful upload alone is not installation evidence.
- Check credentials by presence/permissions or a bounded authorized request, never
  by printing values. Keep keys out of arguments, logs, artifacts and commits.
  Distinguish task-authorized paid API tests from purchasing or redeeming account
  capacity/reset credits; a restriction on the latter does not prohibit the former.
  On missing credentials or a repeated unchanged connectivity failure, finish
  independent checks and report it; do not loop through credential retries.

## Exercise the reading workflow

Use a disposable, authorized test document. For PDF acceptance, use an actual
technical paper with a selected concept and a verifiable question. The circle
selects the topic; surrounding page content and model general knowledge are valid
supporting context. Do not impose a source-only restriction. Paper-specific values
must still match the paper rather than be invented or replaced from memory. Preserve its
original bytes and page order; compare hashes and inspect native annotations.
For an installation with automatic answer-page creation, start with one disposable
notebook page. An existing example with handwriting works. For example, circle a
calculation and write “What is the answer to this?” next to it.
With the page open, hold one finger in the configured corner (lower-right by
default) for three seconds and release. Follow that request through the live
provider and automatic insertion. Confirm that the adjacent page visibly answers
the question and the original ink is intact. A blank successor supplies different
starting data and skips automatic insertion. Test the standalone archive separately
when that distribution is the subject of the task. [Installation modes](https://github.com/s116821/ReMarkableBuddies/blob/main/README.md#using-reader-on-the-tablet)

Validate capture → question recognition → relevant concept explanation → next-page
placement, then a different question appending to the same answer page. Check
the visible question transcription and answer, not just the process exit status.
Use source-specific numbers, uncertainty and units to distinguish reading the
paper from supplying a remembered value. Verify actual rendered operators and
exponents; a correct API response does not prove correct keyboard output.

Include representative connected cursive and shorthand, varying slant and spacing,
plus ambiguous/illegible and absent-question cases. Preserve failures. An abstract
summary after misreading a question is a failure, even if every source fact is true.
The app independently rereads the page without the proposed answer before writing; uncertain
or differing readings should decline the request. Agreement reduces risk but is
not proof of correct recognition. Record conservative false rejections too.
Retain the failing handwriting when diagnosing a miss. Record whether Buddy saw
the actual gesture, received a provider response, saved the page, and displayed
the answer. If a finger press produced no request, record the failed trigger.

Check a short tap versus a held trigger, an occupied successor page, and navigation
back to the source. Inspect UI state between dependent actions: selecting an eraser
and opening its menu can require separate taps. Confirm old ink is gone before
drawing another fixture. Keep printed content separate from editable test ink.

## Capture and evidence

The normalized screenshot is useful for navigation but can lose dense PDF digits.
Inspect native detail as well. Full-width overlapping strips preserve entire
question/text lines; left/right crops previously split a readable question.

Record the expected and observed result alongside the relevant sanitized log.
A direct observation or a single-page screenshot is sufficient for visibility.
Keep affected editable data when needed for recovery. Record failures and subsequent
repairs without relabeling old evidence as a pass on a newer build. Read the existing
CI results for the changed revision and verify the final installed build on hardware.
Do not equate an architecture build with hardware validation on that device.

For a PDF input, use the [reference document](https://github.com/s116821/ReMarkableBuddies/blob/main/docs/validation/README.md#reference-document).
Exercise it through the installed service and physical gesture described above.

The tablet operator owns cleanup for each completed or rolled-back run. After
verifying the retained package and evidence, remove that run's obsolete installer
copies, extracted staging files and temporary captures from the tablet. Keep the
active installation, its rollback, needed evidence and the user's documents.
Check the free space recovered on the notebook filesystem and name an owner and
review point for any staging files still needed. [Development hygiene](../development-hygiene/SKILL.md)

Before stopping, restore the agreed service state, leave the test document in a
known state, and stop test processes created for this work. Report
what passed, what failed or remains untested, the installed build, and the next
concrete step. Firmware changes, pairing/sync, extra providers and new features
remain outside a compatibility test unless separately authorized.

## Bounded service diagnostics

For local simulation use the separate [simulator testing skill](../reader-simulator-testing/SKILL.md).
For an already authorized native run, see [journal and RUST_LOG guidance](https://github.com/s116821/ReMarkableBuddies/blob/main/README.md#viewing-logs-with-journalctl).
Prefer a bounded relevant capture such as:

```sh
journalctl -u reader-buddy.service --since "10 minutes ago" -n 200 --no-pager -o short-precise
```

`-f` follows continuously; end that observer when the test finishes. `RUST_LOG`
controls application log emission; journal priority filtering is not guaranteed
to reflect env_logger's Rust levels. For extra detail, set the documented scoped
filter for the authorized test process or service, preserving the prior environment
and restoring agreed service state afterward. Do not dump the entire environment
or credential-bearing configuration. Inspect logs/debug images before publishing;
they may contain document text even when secrets are omitted.
