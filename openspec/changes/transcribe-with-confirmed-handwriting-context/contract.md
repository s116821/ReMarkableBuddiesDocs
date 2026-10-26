# Proposed transcription contract version1

All JSON objects reject unknown/duplicate fields and wrong types. UUIDs are canonical nonnil lowercase hyphenated strings. Strings preserve exact Unicode; no normalization, whitespace repair or coercion. No paths are accepted.

## Input
Exclusive CLI `--handwriting-transcription` consumes exactly one stdin object, at most12582912 bytes plus one rejection byte:

```json
{"transcription_version":1,"invocation":"00000000-0000-4000-8000-000000000001","document":"00000000-0000-4000-8000-000000000002","page":1,"target_png":"<strict-standard-padded-base64>","context":null}
```

document is a caller-asserted canonical nonnil UUID and page is a positive u32. Target PNG is bounded by the existing notebook decoder to8 MiB/4096 per side/8,000,000 pixels; selected examples retain512 KiB/2048/4,194,304 bounds. Complete prompt descriptor is at most24 MiB and text-only prompt content at most32 KiB; aggregate target-plus-three-examples bounds are9.5 MiB compressed/20,582,912 pixels, decoded sequentially without image transformation. context is required nullable. Non-null shape is exactly `{ "profile": UUID, "examples": [{ "correction": UUID, "revision": UUID }] }`, one to three distinct correction IDs/revisions in the provided order. No implicit latest lookup. Null context does not open/create a Store. Non-null context refuses if configured sync/selected mode, unavailable ownership, unsupported history, nonunique/current-mismatched head or unavailable verified sample. Every selected example also passes notebook static PNG complete framing/CRC/IEND checks with no trailing bytes or APNG. Ineligibility under those stricter checks returns context-unavailable before invocation with context=null; the retained correction remains unchanged and is not reclassified as invalid storage. No network/provider call on admission refusal. Config is selected through REMARKABLE_BUDDIES_CONFIG; no additional config CLI flag.

## Model reply and normalized result
Reuse the existing notebook reply exactly: `{ "pages": [{ "page": REQUEST_PAGE, "status": "transcribed", "text": STRING }] }`, or status blank/unreadable with text="". Exactly one target entry; example images are not target pages. Strict unknown/duplicate field/page/order rejection remains. Nonempty transcribed text is at most4096 UTF-8 bytes and not whitespace-only. Existing control-character policy applies: only newline/carriage-return/tab controls are permitted. Preserve exact admitted wording without trimming. Reply at most16384 UTF-8 bytes; no markdown stripping, prefix/suffix repair or partial salvage.

The result, present only on normalized, is the existing exact NotebookText shape: document {document,format,source_sha256,extractor_revision,units}, images, profile, blank_pages, authority, prompt_sha256, prompt_bytes,response_sha256. Format=notebook and the target source remains caller-asserted/unverified. One target page produces one unit, including empty text only for declared blank. The no-context path preserves current protocol1/profile/prompt identities and authority. The with-context profile protocol2/prompt_revision and confirmed_context recipe are fixed in design.md; authority=unverified-historical-page-image-ocr-with-confirmed-examples. Unreadable returns result=null and never installs a cache or a source record.

## Public report
Exactly these fields, all present:

```json
{"transcription_version":1,"invocation":null,"status":"refused","failure":"invalid-input","provider_attempt":"not-called","target_sha256":null,"context":null,"result":null,"confirmed":false}
```

- invocation is null until a complete strict request is decoded; otherwise the caller UUID, without durable receipt/replay meaning.
- status is normalized, unreadable, refused, canceled or failed. failure is null only for normalized/unreadable; otherwise one fixed code below.
- provider_attempt is not-called or called. Called means execute_with_progress was entered and remote outcome may be unknown on failure; it does not prove network acceptance. It can coexist with refused for invalid provider output after invocation.
- target_sha256 is null before successful target admission, otherwise lowercase64hex over exact decoded PNG bytes. No original image is returned.
- context is null for no requested context or failed context admission. After successful admission it is exactly `{ "profile": UUID, "examples": [{ "correction": UUID, "record": UUID, "revision": UUID, "sample_sha256": HEX64 }] }` in requested order. These are captured selected facts, not transmission/current-head receipts. No examples' text or image bytes are returned.
- result is nonnull only for normalized; confirmed is always false, including successful transcription. No operation/transaction/native/learned-state field is synthesized.

Fixed failures: invalid-input, input-limit, invalid-version, invalid-image, context-invalid, context-stale, context-conflict, context-unavailable, ownership-busy, unsupported-mode, storage-unavailable, prompt-limit, credentials-unavailable, canceled, provider-failed, invalid-response, output-limit. Map Store/decoder/provider details to these codes; never echo their raw content. Refused covers input/context/mode/credentials/prompt/invalid-response/output-limit; failed covers storage-unavailable/provider-failed; canceled requires canceled. Only normalized/unreadable require called. Every not-called failure is a no-invocation assertion, not a durable authorization for retry. Context admission failure erases incomplete descriptors. After valid capture, later refusal/failure keeps captured descriptors and target digest honest.

Serialize a single complete report plus newline into at most32768 bytes before any write. Overflow returns a fixed bounded output-limit report retaining invocation/attempt/digest and the at-most-three admitted descriptors; never truncate successful facts. A stdout error returns nonzero without a second stdout report/provider call. Invalid/refused/failed/canceled process statuses are nonzero; normalized/unreadable are zero, with unreadable explicitly not successful recognition. Guard lifetime covers actual serialization/write/flush/error/drop.

## Outcome matrix

| Boundary | status / failure | attempt | result | captured context |
| -- | -- | -- | -- | -- |
| Input cap or strict/canonical envelope failure | refused / input-limit or invalid-input | not-called | null | null |
| Unsupported version or target image | refused / invalid-version or invalid-image | not-called | null | null |
| Context/mode/ownership admission failure | refused (storage-unavailable uses failed) / fixed corresponding code | not-called | null | null |
| Valid capture then prompt/credential refusal | refused / prompt-limit or credentials-unavailable | not-called | null | retained if selected |
| Cancellation before invocation | canceled / canceled | not-called | null | retained only if complete capture |
| Cancellation/provider failure after invocation entered | canceled / canceled or failed / provider-failed | called | null | retained if selected |
| Malformed provider reply | refused / invalid-response | called | null | retained if selected |
| Strict normalized or unreadable reply | normalized or unreadable / null | called | present only normalized | retained if selected |
| Complete report overflow | refused / output-limit | unchanged | null | retained if selected |

Envelope decoding validates all required fields/types, canonical nonnil UUIDs and positive u32 page before echoing invocation. Version is then checked before PNG decoding; target digest becomes available after full target admission. Do not echo unvalidated invocation strings. A no-context successful report has context=null. Unknown provider/server failure details never become report fields. Canceled requires a refused progress callback; an arbitrary provider error is not relabeled cancellation. Arbitrary LLMEngine implementations are cooperative: the default callback runs once before execute and cannot preempt an implementation that ignores later progress. Only the configured OpenAI transport provides owned worker cancellation/joining through its existing progress path. Post-return cancellation checks suppress stale results without claiming earlier interruption; no wrapper worker or automatic retry is added.
