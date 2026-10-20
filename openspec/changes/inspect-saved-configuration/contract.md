# Saved configuration inspection wire v1 (proposed, unimplemented)

## Invocation and bounds
Fixed command: `reader-buddy --configuration-operation inspect`. Existing REMARKABLE_BUDDIES_CONFIG must name an explicit absolute config file. Host uses its fixed trusted config path in the existing clean child-process environment, never renderer-supplied paths or commands. No --configuration-input or --config selector is added. Inspect must not read stdin or wait for EOF. Reject mixing it with ANY runtime/simulator/other maintenance/input flags before I/O. CLI usage errors are nonzero with no valid report; host maps them to unsupported/invalid response, never ok.

Read at most1048576 config bytes inclusively, checking regular-file type before open and bounded take(limit+1); invalid selector, absent/unreadable/nonregular/unsafe file or read failure returns unavailable. Only selected-file admission and ancestor metadata are permitted. No declared-root metadata/content probing. No Store open/recovery/lease/init/write, credential lookup, dotenv, provider/model/environment resolution, worker, running Buddy API or service/native call. REMARKABLE_BUDDIES_CONFIG is the ONLY environment selection consumed by this operation.

Encode a complete report before its single writer, at most131072 bytes including one LF. Never truncate, retry emission, append a second error report or log raw errors/data. Write failure returns nonzero; a prefix is invalid. Host transport deadline is at most30s, preserving the existing tighter2/8/12/13/14-second channel/collector/Python/Node/browser hierarchy; this operation does not lengthen any shared timeout. Stdout cap131072 and stderr cap8192; cancel/timeout/nonzero/extra trailing material/invalid UTF8/duplicate JSON keys/unknown fields/partial response refuses the entire view. No automatic retry, SFTP fallback or remote staging. Existing product wired identity checks remain required when device execution is later authorized.

## Admission and status
Deserialize actual Config directly from the same bounded raw bytes first (deny unknown/duplicate fields and wrong types); recursively duplicate-check before deriving any origin Value map; reject repeated namespace values. Call Config::validate_values only. Do not call Config::load, Config::validate, StorePaths::validate or config::resolve.

Statuses are exactly ok, unavailable, invalid-input, unsupported. No partial data: every non-ok has snapshot=null. Malformed UTF8/JSON/duplicates/unknown fields/wrong types/out-of-range numeric types or invalid supported values -> invalid-input. Structurally typed config_schema_version !=1 or personalization.schema_version !=1 -> unsupported (check versions before pure value validation). Missing selector/file/read denial/nonregular/over input cap -> unavailable. Old binary rejecting the selector is unsupported at host transport, not a producer report. No raw path/error/unknown key/value echoes. All report statuses exit0 after successful complete emission; transport/CLI/writer failures are nonzero and never treated as a report success.

## Exact report shape
All keys required, deny extras recursively. Top-level ordered fields:
`{report_version:1,operation:"inspect",status:STATUS,runtime_activation:"unverified",snapshot:SNAPSHOT_OR_NULL}`.
Successful snapshot ordered fields:
`{schema_version:1,config_sha256:LOWER_HEX64,byte_basis:"saved-file-bytes",validation_basis:"typed-values-only",declared_roots_validated:false,fields:FIELDS,unsupported:UNSUPPORTED}`.
config_sha256 is SHA256 of exactly the bounded raw file bytes, including whitespace. Host-private observation identity only; strip it from renderer DTO/state/logs. It grants no CAS, freshness, reload, credential validity or runtime authority.

FIELDS is an object with EXACTLY25 flat literal keys from the table below. Dots in keys such as `paths.data` and `personalization.text_bytes` are literal characters, not nested objects; comma-separated table entries each name a separate flat field. Every field is `{origin:ORIGIN,value:VALUE}` with no extras. origin is default, declared or declared-null. A leaf absent because it or an ancestor was omitted is default; present nonnull is declared; explicit JSON null is declared-null ONLY for the existing Option fields. Null for nonoptional object/leaf is invalid-input. StorePaths requires all three members if paths is present; do not invent per-child defaults. Explicit empty memory/sync/personalization objects use their existing leaf defaults and default origins. Explicit null optional values remain distinct from omitted defaults even if their projected values match.

| Exact field key | VALUE (saved declarations/defaults only) |
| -- | -- |
| config_schema_version | integer1 |
| model, base_url, model_credential | boolean presence, false for None/null; never raw text/reference |
| trigger_corner | null or UR/UL/LR/LL |
| log_level | null or off/error/warn/info/debug/trace |
| debug_dump | null or boolean |
| paths.data, paths.cache, paths.credentials | boolean true for typed path present, including defaulted paths; no raw path/existence/validity claim |
| memory.enabled | boolean |
| memory.profile, memory.selection | boolean presence only; no UUID/group/binding/pins |
| sync.enabled, sync.media, sync.create_new | boolean |
| sync.namespaces | lexically sorted unique array drawn only from conversation, export-association, handwriting, source, subject-memory; at most5 |
| sync.max_media_bytes | integer0..268435456 (existing default33554432) |
| sync.poll_seconds | integer5..3600 |
| sync.batch_items | integer1..128 |
| sync.collection | boolean presence only; no UUID |
| personalization.schema_version | integer1 |
| personalization.enabled | boolean |
| personalization.text | boolean nonempty; no contents or digest |
| personalization.text_bytes | integer0..16384; origin follows original text leaf |

UNSUPPORTED is exactly the ordered array `["reader-enablement","writer-enablement","retrieval-policy","research-policy","mem-destination","handwriting-settings"]`. These settings have no representation in the inspected schema; they are neither false nor absent valid defaults. Existing memory/legacy sync booleans are saved declarations only, not active selected mode or cloud health. Optional model/backend null/default never claims an effective default model or unset runtime environment.

## Pinned default projection and consistency
This synthetic FIELDS example is the complete version1 projection for saved input `{}`. It is a design vector, not captured CLI evidence. All25 origins are default; strict consumers pin these values for default-origin fields rather than deriving future defaults.

```json
{
  "config_schema_version": {
    "origin": "default",
    "value": 1
  },
  "model": {
    "origin": "default",
    "value": false
  },
  "base_url": {
    "origin": "default",
    "value": false
  },
  "model_credential": {
    "origin": "default",
    "value": false
  },
  "trigger_corner": {
    "origin": "default",
    "value": null
  },
  "log_level": {
    "origin": "default",
    "value": null
  },
  "debug_dump": {
    "origin": "default",
    "value": null
  },
  "paths.data": {
    "origin": "default",
    "value": true
  },
  "paths.cache": {
    "origin": "default",
    "value": true
  },
  "paths.credentials": {
    "origin": "default",
    "value": true
  },
  "memory.enabled": {
    "origin": "default",
    "value": false
  },
  "memory.profile": {
    "origin": "default",
    "value": false
  },
  "memory.selection": {
    "origin": "default",
    "value": false
  },
  "sync.enabled": {
    "origin": "default",
    "value": false
  },
  "sync.media": {
    "origin": "default",
    "value": false
  },
  "sync.create_new": {
    "origin": "default",
    "value": false
  },
  "sync.namespaces": {
    "origin": "default",
    "value": []
  },
  "sync.max_media_bytes": {
    "origin": "default",
    "value": 33554432
  },
  "sync.poll_seconds": {
    "origin": "default",
    "value": 60
  },
  "sync.batch_items": {
    "origin": "default",
    "value": 32
  },
  "sync.collection": {
    "origin": "default",
    "value": false
  },
  "personalization.schema_version": {
    "origin": "default",
    "value": 1
  },
  "personalization.enabled": {
    "origin": "default",
    "value": false
  },
  "personalization.text": {
    "origin": "default",
    "value": false
  },
  "personalization.text_bytes": {
    "origin": "default",
    "value": 0
  }
}
```

Only model/base_url/model_credential/memory.profile/memory.selection/sync.collection presence fields and nullable trigger_corner/log_level/debug_dump may use declared-null. For presence fields, default or declared-null is false and declared is true. Nullable trigger_corner/log_level/debug_dump use null for default or declared-null and only the table's nonnull typed values for declared. Paths are always true with default or declared origin and never declared-null. Other nonoptional fields are default or declared only; a default origin requires the pinned value above. All keys and value types are required, with no extras/nesting.

personalization.text and personalization.text_bytes have identical origin and text presence equals text_bytes>0; their default pair is false/0. memory.enabled=true or memory.selection=true requires memory.profile=true. sync.create_new=true requires sync.collection=true. Reject sync.enabled=true combined with memory.selection=true, or combined with memory.enabled=true and subject-memory in sync.namespaces. These are projected consistency checks, not proof of hidden identity equality, safe paths, credential validity or runtime compatibility. Producer typed validation still checks the underlying full values; the reduced view cannot reconstruct private identities.

## Consumer view and lifecycle
Reduced renderer snapshot preserves schema_version, byte_basis, validation_basis, declared_roots_validated, fields, unsupported; omits config_sha256 entirely. Strictly validate both producer and reduced DTO. Display Saved configuration, per-field declared/default/null origin and unverified runtime note in both hosts. No edit, enable, provider test, credential entry, path browsing, reload or service buttons in this slice; reference existing personalization/saved-mode features without importing their authority.

Explicit inspect only. Clear prior view at start, cancel, disconnect, target/boot change and explicit refresh (even same IDs); reject late completions by both host and controller observation generations. Register new external maintenance method in shared forget invalidation BEFORE command dispatch; clear stale prepared reference under existing host rules. Never turn cancellation/unavailable/unsupported into a default successful config.

## Acceptance specimens
Main publishes actual CLI bytes for default {}, explicit null Options, nested omitted/default origins, safe scalar declarations, all supported namespaces, endpoint/model/reference/path/personalization/identity sentinels, unsupported versions, duplicate root/nested/namespace entries, malformed/unknown/wrong type/oversize input and bounded writer failures. Credentials and declared roots get inaccessible/untouched sentinel fixtures; MustNotRead proves no stdin dependency; injected loader/probe guards establish no declared-root probing. Compare files before/after. Consumer verifies exact specimens, strict report/reduced-view schemas and byte caps, then both actual browser/Electron paths and same-ID/late invalidation. Synthetic tests do not qualify physical USB/device, provider or active-runtime behavior.
