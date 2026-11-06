# Bounded receiving qualification entry

## Scope and pre-dispatch gate

Extend the existing simulator with an explicit combined-qualification mode. Keep
the original scripted combined scenario and all association/deduplication/refusal
controls unchanged. The new entry uses actual Dispatch Reader, ordinary Writer
Generate/Refine and notebook map/reduce/Reader paths with real temporary Stores.
Only completion observation is simulated; no native navigation/rendering or
external export is attempted. Optional subject memory is disabled in the current
ordinary Dispatch receiver; this entry does not silently enable or qualify an
additional memory-backed route. Its existing separate receiving contracts remain.

Scripted mode uses the same entry and assertions without credential resolution.
Live mode alone resolves the explicit saved Config through existing protected
credential selection, then uses the existing OpenAI adapter. Review the exact
source/build/fixture/config identity and offline request trace before dispatch.
This implementation handoff does not execute a live request.

Use an absolute REMARKABLE_BUDDIES_CONFIG path and the separately reviewed
RMB_COMBINED_QUALIFICATION_CONFIG_SHA256, RMB_COMBINED_QUALIFICATION_MODEL and
RMB_COMBINED_QUALIFICATION_HTTPS_ORIGIN environment pins. Require exact saved
model/HTTPS origin and a protected model_credential reference before resolving
the key. Use existing Config::resolve with empty CLI/environment overrides;
ambient API-key substitution is not admitted. Scripted mode does none of these
reads. The pre-dispatch reviewer supplies those nonsecret identities privately;
the report includes the Config digest/model/origin but never a key.

## Fixed evidence and exact requests

Use only docs/validation/images/selected-memory/source-page.png, SHA256
0d780409f24a5411f24727bc81777a2eec8f6fdc5ab8186eae96d3721ee0e820.
It is synthetic printed physics, not handwriting qualification. Initial requests
and history do not disclose its mass, acceleration or force. The independently
read image shows2kg and3m/s², yielding6N; expected facts belong to review/assertion
metadata, not the initial model payload. No second image is required because the
existing multi-image/association/deduplication controls remain maintained.

One shared conversation receives four requests:

1. Reader: `From the Source A diagram, identify the mass and acceleration and calculate the net force. Show the units.`
2. Writer Generate: `Create a concise study note about Source A from the diagram and our conversation. Label the source and retain physical units.`
3. Writer Refine: `Refine this draft by adding one dimensional-analysis sentence. Preserve the original Source A facts and provenance.`
4. Reader: `Using the latest refined note and the original Source A diagram, explain the calculation again and identify what the refinement added.`

The supplied ordinary source unit identifies Source A without its numeric facts.
Each actual returned Reader/Writer response is recorded before the next step;
Writer drafts remain generated/selectable after simulated visibility and handback.

A separate ready notebook conversation then receives three model calls:

5. Notebook map: the supplied comparison text is `Source B: a separate cart has mass 5 kg and acceleration 2 m/s^2. Calculate its net force and retain the Source B label.`
6. Notebook reduce, using the original notebook request: `Create a comparison note for Source A in the historical diagram and Source B in the supplied text. Keep each source's facts separate, calculate both net forces, and compare them.`
7. Reader: `Using the comparison note and its original sources, explain which source has the greater net force and why. Keep the source labels distinct.`

The notebook operation uses one map plus one reduce. Maps receive no historical
images/associations; reduce receives the ordered original image associations and
encoded attachment digests. Its exact parts must match the persisted reducer
input digest. The actual notebook note enters Reader history without consuming
its draft. Source B gives10N; source separation is reviewed independently rather
than accepted through arbitrary wording equality.

## Bounds and evidence

Exactly seven calls are selected; reject scenario allowances other than seven
before credential access. Refuse an eighth execute, stop permanently on any model
error, disable transport retries/redirect replay in this opt-in mode, retain the
existing4000-output-token cap, cap each request at90s and the complete run at12min.
Progress cancellation must enforce the overall deadline during the real adapter.

Persist a fresh bounded report even on sequence failure, with original received
text parts, exact image identities/association payloads, actual returned replies,
stage/count/status and checks. Do not put credentials in traces/errors. Store
facts and simulated completion evidence are not native authority. Keep live
semantic judgment, offline policy assertions, transport checks and hosted CI
separately attributed. No automatic retries or new calls follow from a failure.
