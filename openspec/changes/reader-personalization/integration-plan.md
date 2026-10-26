# Ordinary Reader integration proposal

This is pre-code reconciliation scope, pending independent review. Existing source branch caf4ee5 and specification d3816fc remain historical candidates. No source implementation, model call, deployment or completed qualification is implied.

## Current-main dependencies

Source main 6e33bfd already provides the immutable validated preference snapshot, two-pass question verification, acknowledged image re-read, exact interpreted-question persistence and ordinary publication guards. It also provides bounded local memory query/result types. It does not expose the old branch's memory answer helper or Reader optional-memory wiring. The accepted personalization delta c2dc54e changes ten files; its complete inherited branch is not the integration unit.

Reuse those current-main implementations. Preserve its Cargo manifest/lock and SDK32b pin, release/CI policies, storage, native bridges and selected Reader boundaries. Do not import the old selected Attempt helpers or Provider::require_selected_reader merely to compile an ordinary preference path. No SDK source or native behavior changes belong to this proposal.

## Proposed receiving boundary

Capture one validated startup preference and clone it for the prepared request. The first two recognition requests remain unchanged and contain no preference. Only after independent question agreement and exact interpretation may a third answer request include the preference. Unset, disabled or empty preference without usable memory preserves the current two-call sequence.

For this ordinary runtime, optional memory accepts only the actual LocalMemory type, through an ordinary-only setter taking Option<Arc<LocalMemory>>, not arbitrary selected providers. Startup constructs it only when memory.enabled is true and no selected-memory identity is configured. Enabled selected memory refuses before device startup and before provider invocation; disabled memory does not trigger that refusal. It must not silently fall back to global facts. This is a newly explicit ordinary-runtime boundary, not selected Reader admission or a new permission.

Ordinary capture has no verified document association, so its local query keeps document=None. Current unavailable/failed retrieval and partial results with no usable facts refuse contextual answer publication. Absent/disabled and successful complete-empty retrieval permit preference-only generation. Partial retrieval with usable facts may join the same single answer request. The existing Source/Store and native output guards remain; no selection authority is synthesized from a query result.

Port the accepted bounded receiving answer policy and tests onto current types. Keep CURRENT_REQUEST, original images, optional author-asserted memory and exact JSON-escaped preference separately labeled. Current explicit request and fixed source, operation and ASCII output contracts outrank style preference. Preserve exact Unicode/CRLF preference bytes, but never use preference in recognition or invent visible transcript turns. No model-driven confirmation or training occurs.

## Preservation and implementation plan

Keep the existing PR49/41 branches and use ordinary merge history, never reset/rebase/force. Retain their old complete heads as immutable ancestors and preserve all other active native, memory, export, source-cache and held transcription branches/workspaces/evidence. Before resolving inherited differences out of the new candidate tree, independently review the exact preservation map.

The intended candidate is current main plus this explicitly reviewed receiving capability and its controls/guidance. Source paths are the accepted ten-file feature scope, memory module registration, the existing local-development paragraph and minimal historical simulated image. Adapt assertions to actual current APIs; do not copy an entire selected/native parent. Preserve every unrelated main entry and all current safeguards. Keep original evidence tied to its original commits and distinguish new source/host qualification.

Compose current Docs main 0f900e3, preserving current Manager and all other canonical/archive/active changes. Edit only this named active change and directly necessary public guidance. Do not sync or archive while live semantic qualification remains open. The earlier spent mathematical recognition experiment is separate and cannot qualify this Reader capability.

## Required checks and remaining gates

Capturing-engine controls cover default identity/sequence, exact question and images, once-only preference, disabled/empty and local-memory combinations, current-request framing, disagreement, provider failure, cancellation and unchanged output guards. Actual filesystem/CLI checks prove selected-memory refusal before device/provider initialization. A bounded loopback HTTP check uses synthetic responses and dummy credentials only. Run current-head ordinary CI and review actual logs after source integration.

No additional live call is admitted by this proposal. A later exact question, fixture, model, expected facts and budget need separate review. Host tests do not prove provider obedience, native output, verified running restart/reload or Manager active state. Keep broader Reader/Writer routing, selected memory/sync and whole personalization requirements open.

Source basis: current public PR49/41 discussions and reviews, accepted c2dc54e delta, current-main Git object reads and dry integration checks. The ordinary-only reconciliation is proposed behavior, not implemented evidence.
