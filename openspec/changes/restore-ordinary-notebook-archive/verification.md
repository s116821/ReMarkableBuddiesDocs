# Verification and remaining delivery gates

Implementation: [Buddy PR127](https://github.com/s116821/ReMarkableBuddies/pull/127),
source `f2ac3011fe7db1fe13e5f77c8d51f9bb17c8cf60`.
Paired [Docs PR138](https://github.com/s116821/ReMarkableBuddiesDocs/pull/138).
Merge implementation before the completed synced/archived Docs delivery. The
parent restore roadmap remains open; this increment is same-actor/local only.

| Requirement/scenario | Implemented path | Actual evidence or remaining gate |
| --- | --- | --- |
| Complete same-actor archive | explicit version2 selectors; existing notebook validator and OS custody | Windows maintenance and actual CLI success, preserved media/reopen |
| Unsupported/changing input | existing-only notebook admission, actor/hash/config/mode/history guards | Windows wrong actor, legacy archive, corrupt/missing objects, config/base drift, busy lease and existing target controls |
| Additive exact readback | shared History with actor validation; existing notebook writer with original target; verified desired closure | Windows recovery of missing archived facts plus unrelated current records; CLI media retained |
| Lost/interrupted publication | attempted-CURRENT flag; phase-specific outcome; read-only original Status | Windows Before/AfterActivation faults, source-absent status and no replay; incomplete capabilities refuse without repair |
| Legacy request | unchanged version1 selectors/admission | All five existing Windows ordinary restore CLI cases pass; legacy notebook refusal asserted |
| Real notebook lineage/media | maintained simulator fixture followed by actual CLI | Linux-only test extended; Windows filtered run executes zero tests; final Linux CI pending |
| Output custody/privacy | existing report shape with notebook flush under held OS lease | Windows write/flush custody test and bounded actual subprocess frames |

Windows `restore_maintenance` passes 10 tests; `ordinary_restore_cli` passes 6.
All-target/all-feature Windows check passes with existing platform warnings.
The unchanged legacy storage unit filter executes zero Windows tests because its
suite is Linux-gated; it is not a passing legacy storage execution claim.
Initial new CLI assertion incorrectly demanded conflict after source removal;
actual safe refusal was unavailable. Corrected that assertion, preserved the
failure locally and reran the actual CLI suite successfully.

Strict OpenSpec validation passes all 116 current items. Canonical requirements
are synced; this active change intentionally remains unarchived until the exact
source Linux required checks and coordinated independent review are complete.
Root owns independent review/integration and subsequent archival gate; author
owns resolution of returned source findings within this pair. No native/model
experiment, tablet operation or host package installation is required or claimed.
Local test logs are private development evidence without public download links;
public PR comments report results and limits. No report UUID/page/native authority
is inferred from fixture success.
