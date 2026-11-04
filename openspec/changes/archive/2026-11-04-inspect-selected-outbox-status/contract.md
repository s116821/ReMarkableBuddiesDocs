# Selected outbox status wire contract v1

`reader-buddy --inspect-selected-outbox` is an exclusive flag with no
arguments, request JSON, or stdin read. It uses the existing configured
local Store path resolution with no caller-supplied path or provider
credential argument. Combining it with any other application action or
override is a CLI refusal before config/Store access. Hold the existing
Store lock across the report lifecycle. No service is stopped or started.

Emit one compact UTF-8 JSON object followed by one LF, at most 1024 bytes,
with exactly these fields in this order:

```json
{"report_version":1,"operation":"inspect-selected-outbox","status":"ok","counts":{"pending":1,"withdrawn":1}}
```

`counts` has exactly `pending` then `withdrawn`, nonnegative JSON integers
with total at most 4096. Empty valid custody is `{"pending":0,"withdrawn":0}`.
The complete counts include every validated actor-owned original journal
row, including historical or stale rows. Pending is the recorded local
intent state. It conveys no network, current-token, remote-work or retry
status.

| Status | Counts | Meaning |
| --- | --- | --- |
| ok | exact object | Entire admitted journal validated, or absence established under valid existing custody |
| busy | null | Existing Store lock owned elsewhere |
| unavailable | null | Config or owned Store not available, or inventory I/O unavailable |
| corrupt | null | Present journal metadata, identity, schema, fingerprint or filename failed validation after admission |
| unsupported | null | Unsupported Store/platform/lock/layout, notebook format 4 or marker, or journal type/limits outside the contract |

A non-ok report has the same four fields and `counts:null`; e.g.

```json
{"report_version":1,"operation":"inspect-selected-outbox","status":"unsupported","counts":null}
```

A completed frame exits zero for any listed status. CLI parse refusal and
serialization/write/flush failure exit nonzero. No second report after a
prefix write or flush failure. No mutation, retries, metadata repair,
live-provider use, worker startup, credential contents, or native authority.
