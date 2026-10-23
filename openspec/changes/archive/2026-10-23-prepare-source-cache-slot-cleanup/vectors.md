# Required executable vectors before source acceptance

All fixtures use synthetic owned roots and sentinel source/durable/credential
files. No real Config, key, provider, account, tablet or package execution.

| Case | Required result / preservation |
| --- | --- |
| present valid slot inspect/prepare | ready/prepared; byte+metadata snapshot unchanged; both leases held through output |
| literal dash / equals-form aliases / held stdin | literal reads EOF; aliases refuse without reads |
| strict object/duplicate/nil/noncanonical/oversized/extra JSON | invalid-input before any filesystem access |
| absent slot | absent; no token/create/mutation |
| changed Config/path/root/actor/generation/marker/namespace/entry identity or bytes | conflict/refusal, no deletion |
| missing or busy/replaced Store or namespace lock | unavailable/busy/unsupported; no lock creation |
| unknown/schema/over32MiB slot / capacity / unknown name / staging / reparse | unsupported; every entry preserved |
| prepared exact apply | only selected UUID.json removed; directory sync+absent readback; applied |
| repeated apply after absence | absent, no retry or historical-success assertion |
| post-remove sync/readback failure | unknown possible_effect; no rollback/retry |
| output short write/failure | custody retained through failure; no success receipt/retry |
| status original/absent/changed | unchanged/absent/conflict; no mutations |
| other domains/durable/source sentinels | exact bytes and metadata retained throughout |
| Linux actual CLI | executable SHA, source/tree, per-record raw hashes and bounded no-secret reports |
| Windows actual CLI, held stdin and nonexistent/poison Config | unsupported before reads/path/locks; no applied/deletion/directory-sync claim |
| dedicated admission with denied durable read/enumeration hooks | no generation enumeration/commit/object/quarantine/sync access; no Store construction/recover |
| missing/corrupt/inaccessible durable payloads, valid bounded headers | same cache preview/apply admission; payload bytes and metadata preserved |

digest-vectors.json freezes exact digest-domain/canonical encodings including a
changed-one-field control. Source implementation must independently consume and
verify them; these are not a claim of filesystem qualification.
