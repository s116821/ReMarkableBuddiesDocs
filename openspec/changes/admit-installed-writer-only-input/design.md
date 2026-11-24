# Installed Writer input

Use the same verified output profile and supervised service as the combined app. A stationary three-finger hold opens or reuses a blank page after all fingers lift. It uses the existing page owner and makes no model request.

For refinement, select a request already queued in the current service activation. Buddy first publishes the complete request under its queue lock, then records the boot-clock second by which it was visible. That second must precede the timestamp of the kernel touch frame that reported the release, on the same clock. A delayed poll or a stalled write cannot attach a new refinement to an earlier gesture. If the input driver cannot supply that clock, the ordinary Reader and blank-start gestures remain available. An older or interrupted refinement without a publication time stays untouched until expiry. A three-second hold started after successful queueing orders the two events.

Immediately before claiming a refinement, Buddy reads the open page and its order again and checks the current draft and conversation. It rechecks the complete request and its expiry under the queue lock. A different page, stale draft or replaced request leaves the slot available. Where the ordinary service also supports generation from the current target, the same corner gesture can select that queued action. Buddy records the activation and request digest at selection and checks both when taking the request for the captured page. The existing queued path leaves Writer-only mode listening when the hold has no queued request. Reader-only mode skips the Writer queue. Shared intent routing supplies the user-facing source action described below.

In combined mode, a valid Reader corner hold still opens Reader if the optional Writer queue cannot be read and the service remains healthy. In Writer-only mode, that case returns to listening. If clock setup loses the first touch frame, discard that new listener and wait for a fresh gesture on a newly seeded descriptor. A later input loss retains the usual failure handling. Keep Reader-only input, history and cancellation behavior. Hardware acceptance uses the installed service, real finger gestures and visible page results.

## Shared submission

The lower-right hold starts shared source intake in combined and Writer-only mode, including when the internal queue has no request. The intake reads the captured image and a bounded recent range from the bound conversation's model context. Included turns retain their original text. Generated drafts that have yet to be published are outside that context, and an over-budget range is refused intact. A reading question proceeds to the existing Reader verifier and answer flow. Writer receives the original request and resolved source scope. A continuation uses the conversation submission key combination. Ambiguous export requests require clarification under the existing destination rules.

## Current-page note

Keep current-page generation distinct from the queued current-target route. When shared intent routing identifies an explicit request for a note about the current page, capture the observed source page with the existing SDK. Use that exact image and its page position for handwriting normalization. Retain the captured document and page in the conversation's source evidence. Honor cancellation during recognition and generation and recheck the page and its order before generation and placement. A blank or unreadable source cannot start note generation.

Use the existing Writer note preset and draft runner. Keep its system instructions out of the visible conversation. Reuse the conversation bound to the source or start one for the captured source. Existing guarded placement opens or reuses the adjacent Buddy page.

## Circled-only note on a fresh source

The same source submission can explicitly request a note from the circled part. Bind the interpreted request and selected geometry to that submission's original capture. Keep the exact request as one Writer turn. The regional runner masks pixels outside the selected geometry before recognition and saves its existing regional provenance and About description with the draft. Place the draft on the verified adjacent Buddy page, including when a fresh one-page notebook needs its first Buddy page. Ambiguous or missing geometry cannot select the current-page path.

## Whole-notebook source admission

The shared hold recognizes an explicit whole-notebook note request and retains its wording. The current installed capture supplies pixels from the open Reader window and samples the document and page order. Those facts alone cannot prove full-page content or supply pixels for the rest of the notebook. The notebook Writer runner verifies coverage of the supplied normalized units. It needs a supported acquisition result for the same notebook with every original source page accounted for in order, including blank pages. Existing Buddy conversation pages must be distinguished from the notebook's source pages.

Until that input is available, report that complete notebook coverage is unavailable. Keep the present page and existing conversations intact. Context, the open page and a normalized archive whose complete source cannot be verified cannot substitute for the requested notebook. [Installed capture contract](https://github.com/s116821/ReMarkableOpenSDK/blob/a0c6480be6785480c2e0da76a3c06697a18efae4/openspec/changes/archive/2026-11-05-integrate-resident-native-adapter/native-capture.md) · [Notebook Writer contract](../../specs/large-writer-notebooks/spec.md)
