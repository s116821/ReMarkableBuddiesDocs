# Required inventory controls

| Fixture | Expected behavior |
| --- | --- |
|0/1/16canonical slots|ok [], one or16 sorted IDs/lengths; exact checked total|
|empty/corrupt/unreadable payload contents|metadata can be listed without opening content; no payload validity claim|
|17slots or metadata>32MiB|unsupported, entries/total null, no repair|
|unknown/staging/type/reparse/nil/noncanonical slot|unsupported, preserved rather than skipped|
|unknown/bad/oversized ownership/current headers|unsupported/unavailable, no adoption/recovery|
|missing/busy/replaced lease|explicit refusal, no create, no success array|
|Config/roots/actor/generation/namespace/slot identity or length changes|conflict/refusal, no partial current list|
|known-header read allowlist|slot contents, credentials and durable payload reads/enumerations denied|
|output partial write/failure|both leases held through failure; no retry or filesystem mutation|
|Windows and other non-Linux targets|unsupported before Config/fs/input; no local support inference|
|extra value/conflicting mode/overrides|CLI parse refusal before protected startup; no sentinel echo|
|clean actual CLI|separate source/tree/executable and raw stdout/stderr hashes|
|all existing cleanup controls/vectors|unchanged wire, intent digest, custody and uncertainty behavior|

No provider, real Config/key, account, tablet, service or package execution is part
of these synthetic controls. A new current-source capture never relabels an older
run. Existing retained cleanup captures and failures remain immutable.
