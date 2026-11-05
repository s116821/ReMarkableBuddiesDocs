# Proposed opt-in mathematical layout profile

This is a prospective addition to the existing paired change. Both four-cell
MathWriting comparisons remain NOT MET. The generic prompt preserves wording
and reading order but does not define mathematical layout serialization. A new
explicit policy asks for unambiguous notation without changing the parser or
claiming that notation instructions solve recognition.

## Request and compatibility

Accept one additional exact policy value, `partial-math-transcription`, only in
the existing strict `transcription_version:2` envelope. The established
`partial-transcription` value retains its exact prompt, profile and behavior.
No new field, version, saved setting, implicit selection or migration is added.
Version 1 and the default notebook normalizer remain byte-for-byte compatible.
Other policy values/types, a missing policy, duplicate fields and a policy in
the version 1 envelope continue to refuse at the existing pre-admission boundary.
Admitted math requests retain the version 2 report and its required nullable
partial field. Invalid envelope/page ordering and later failure facts stay as
specified in the existing v2 contract.

## Prompt, profile and source identities

Reuse the existing partial-v2 base prompt as the first text part. Insert the
exact [math layout addendum](prompt-math-layout-v1.txt) as the second text part
only for the new policy. Then append the unchanged confirmed-context instructions
and selected examples, when present, followed by the unchanged manifest and
target image. Do not modify images, labels, selected context, provider options
or model. The original prompt/addendum files are not edited. The new multiline
literal uses LF bytes on every host, enforced by scoped Git attributes in both
repositories, so Windows checkout conversion cannot alter its pinned digest.

| Field | New policy value |
| --- | --- |
| Profile protocol | `3` (unchanged profile shape) |
| No-context prompt revision | `transcribe-partial-math-v1` |
| Selected-context prompt revision | `transcribe-partial-math-confirmed-examples-v1` |
| Extractor prefix | `notebook-ocr-partial-math-v1:` |
| Manifest protocol | `2` (unchanged reply shape) |

Append the existing SHA-256 of exact serialized Profile bytes to the extractor
prefix. Compute the prompt digest from the actual ordered part serialization,
including the addendum. Target-only source and PNG identities remain unchanged.
The six [identity vectors](math-layout-identity-vectors.json) cover no context,
one/two examples, order, revision-only and text changes. A revision-only change
still changes profile/extractor identity without changing prompt bytes.

## Representation and limits

LaTeX remains inert text in the existing transcribed or known-span string. Do not
parse, render, execute, repair, simplify, normalize, confirm or concatenate it
across uncertainty markers. JSON escaping preserves its backslashes and braces.
All existing page/span/string/report limits, content custody, cancellation and
one-call/no-retry rules remain in force. No source/export/confirmation consumer
is added. Mathematical strings are semantically unverified even when their JSON
is valid; this change cannot enforce visual fidelity through the parser.

The existing textless uncertain span cannot express an unknown child of a
mathematical attachment tree. Each known fragment therefore must be independently
complete. Where an unknown glyph or attachment prevents this, the prompt asks to
mark the smallest complete enclosing expression uncertain and retain independent
readable content. It forbids unclosed LaTeX arguments spanning an uncertain run
and invented placeholders in known text. This conservative result can still fail
the unchanged positive-structure criterion. No AST or relaxed criterion is hidden
in the text contract.

If this leaves no independently complete known text, the prompt explicitly asks
for unreadable with empty text. It does not authorize an all-uncertain partial
response; the unchanged parser continues to reject that variant.

## Implementation and verification

Carry a private `PartialMath` policy from strict admission through the existing
Prepared operation. The normalizer shares the existing partial parser for both
partial policies; only prompt composition and explicit profile identity differ.
The report and selected-context capture code remain shared.

Verify all existing legacy and partial-v2 vectors unchanged alongside the new
six vectors. Add production-path tests for exact opt-in routing, invalid/version
precedence, full/partial LaTeX byte preservation, target-last/context isolation,
distinct profile identity and unchanged target identity. Reuse existing bounds,
Store/output/cancellation tests and test the new policy through actual CLI
admission with no live provider. Include the no-independent-known-text unreadable
outcome and refusal of an all-uncertain partial response under the new policy.
No extra cache, dependency or renderer is needed.

After independent source review and current checks, a separately bounded fresh
four-call math packet may use the same two upstream-default PNGs, model, context,
order and strict rubric. Only the policy/prompt/profile and their consequential
identities change. Independent scoring remains condition-blinded. The unchanged
Hunter, Howe and blank fixtures in both context arms require a separate six-cell
regression packet before delivery. Do not enlarge a reviewed execution packet,
repeat unchanged calls, reuse the ambiguous historical numeric oracle, insert
sample-specific answers or reinterpret previous failures.

These prospective checks do not authorize execution by themselves. Existing
human API authority can support a concrete reviewed run without another user
permission request. Positive live evidence remains distinct from native testing,
automatic Reader/Writer integration, learning efficacy and whole-feature closure.

## Implementation record

Source `a25d1bc6f1f7c7f3c1d1765766d2a96093884734`, tree
`00db852a937dc57010a1660abd28bc4d6432b714`, implements this contract in the
existing admission and notebook normalizer. The literal and six vectors match
the reviewed precode. The private policy carries through admission; old default
and partial-v2 request bytes, reply schema and bounds remain unchanged. LaTeX is
an inert returned string, with no renderer, parser, repair or execution added.

Windows checks on the implementation passed: 23 focused transcription tests,
two actual CLI tests, formatting and all-target Clippy. Clippy retains six
pre-existing Windows-only dead-code warnings in unrelated Writer test helpers;
this is not a warnings-as-errors or Unix execution claim. The actual Store and
normalizer tests cover old/new vectors, exact context/target assembly, full and
partial string preservation, unreadable/all-uncertain outcomes, output bounds,
cancellation, lifetime and unchanged data. CLI controls cover version/policy
precedence and refusal before credentials/model dispatch. Existing Unix SIGINT
controls are not claimed as locally executed math-policy tests.

Independent source review found no blocking issue and recommended one additional
prompt-budget control. The added test holds the examples constant: legacy text
parts total 31,336 bytes; the math addendum raises them to 33,310, exceeding the
unchanged 32,768-byte limit. Actual admission refuses before a second model call.
The first fixture used too much example text and exceeded both budgets; its
failed log is retained. Reducing only that fixture to the independently checked
boundary produced the final 23/23 pass. No production limit was changed.

Evidence digests:

- Final focused test log: `01fd63da97fbb2fc3e3e343cb3fa495a223eb0044b4dd9aec0d2c7fcb5716e3e`.
- Actual CLI log: `8fb1937573782195d982a5eee4cc8b493ed433db8c3c3c388a33072efe9edf97`.
- Clippy log: `f13307e5558714d4739465db70e4681e115ef81d38e217fa2fa0ee94a6088ed1`.
- Independent source review: `dd9ab2be8933477475e8f612d67b6b4fb33b1d0316ba6a900766de12dc5a30d5`.
- Independent boundary follow-up: `80a1edcfe756db600e5a3984ee320d7a0f425351558ce4347cd64a42e536dddf`.

Hosted checks, the fresh four-cell semantic comparison and separate six-cell
regression remain delivery gates. Prior failed recognition results are unchanged.
