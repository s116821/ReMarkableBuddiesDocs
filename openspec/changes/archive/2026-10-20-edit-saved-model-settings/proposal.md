# Edit supported saved model and endpoint declarations

## Why and scope
Management requires deliberate model/backend configuration. Current Config already supports model and base_url, but the delivered general inspector exposes only their presence and the basic editor is deliberately limited to three other fields. Add only explicit set/clear of these two supported saved declarations through a separate bounded producer. Do not invent unsupported backend types, retrieval policy or model discovery.

Reuse the existing declaration-preserving serializer and guarded configuration writer/current ordinary-or-selected custody. Keep the basic wire unchanged while its separately owned companion is implemented. Preserve unrelated raw values/absence/null, no-op bytes, original whole-file/path conditions and exact disk readback. Reports never echo old or newly pasted model/endpoint strings, including credential-like userinfo/query/fragment/control text. No credential/reference/file, provider call, DEFAULT_MODEL, precedence, service, runtime or device behavior changes.

## Source facts and boundaries
At actual ea1324f713a9807dbe9141cb540d897e5502377b, validate_values checks only nonblank model/256-byte and base_url/2048-byte limits; it does not parse URLs, remove controls or trim values. resolve chooses model from CLI/file/default, and endpoint from CLI/environment/file. General inspection intentionally returns presence only. The new producer keeps those exact value rules and privacy boundaries; it cannot claim endpoint syntax, auth, capability, effective settings or runtime readiness. Invalid/unsupported whole documents refuse rather than being repaired.

## Ownership and delivery
Main owns this producer/central change; Root reviews. SCRAPPY retains the separate basic-settings companion. Docs base is actual e37ebef82ef20d52a981591edb10768b3f7404e8; preserve later independently verified deliveries during composition. Ordinary restore publication remains separately tracked, not reopened by this work. This active precode is unimplemented; review precedes source changes and one linked Docs/source delivery includes meaningful tests, verification, sync and completed-scope archive. Future both-host API/UI/private-patch lifetime requires its own concrete precode. No extra human permission, provider or tablet authority follows.
