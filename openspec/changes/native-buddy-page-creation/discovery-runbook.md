# Prepared discovery handoff — not executed

This is an offline checklist for the sole tablet coordinator after dispatch. No command here has been run on a tablet for REM-25. REM-9 currently owns hardware. Do not launch SSH, transfer probes, load extensions or operate the UI merely because this checklist exists.

## Pass 1: bounded passive inventory

Coordinator first records that the authorized development tablet is idle and the previous lane is complete. Use the existing authorized connection; no new credentials or account setup. Each inventory command gets a 10-second host-side deadline and no automatic retry. Missing utilities or inaccessible paths are recorded as unavailable, not installed as a side effect.

Read-only command candidates, run individually in the coordinator's existing device session:

```sh
cat /etc/hwrevision
cat /etc/os-release
uname -m
pidof xochitl
```

Require exactly one positive numeric PID before substituting `<PID>` below. Capture identity before and after the pass; a changed PID/start time invalidates the result. Do not expand a multi-PID string into these commands.

```sh
cat /proc/<PID>/stat
readlink /proc/<PID>/exe
```

Hash the exact observed executable path with `sha256sum` if present. Inspect only mapped Qt library filenames from `/proc/<PID>/maps`; do not read process memory or environment. Record executable/library build IDs or version strings from available read-only ELF metadata, not guessed Qt version from firmware. Do not use `ldd` on an unknown binary or run the binary with speculative options. Firmware, executable hash and Qt ABI are separate evidence fields.

Record whether `/home/root/xovi` and the known broker pipe paths exist, plus file owner/mode and installed module filenames. Do not write to or read from a FIFO: even reading can consume another client's reply. Do not invoke xovi/start, stock, rebuild_hashtable, a service restart, arbitrary QML, or a candidate native method in this pass. File presence does not prove an active extension. A dynamically loaded discovery probe belongs to a separately dispatched experiment with its own safety/rollback plan.

## Pass 2: host-only source/resource inspection

Use already authorized exported local evidence when available. Any new export is a separate coordinator decision, scoped to required non-secret metadata/resources. Keep proprietary firmware/resources local; publish only permitted observations, signatures and hashes. No account files, credentials or complete unrelated library exports.

On a local copy, inspect ELF symbols using the matching architecture's `readelf`/`nm` without executing the executable. Inspect legally available QML resources for active document/page model names, method signatures, insertion/save/close/navigation signals and lifetime boundaries. Record an actual signature before proposing an invocation. A string resembling addPage is a lead, not evidence of arguments, ownership or completion. Do not copy a fixed address from another firmware.

Deliver discovery output as: exact platform fingerprint; discovered objects/signatures and source locations; owner-thread/event-loop expectations; exact native document/page identity source; save completion observation; unresolved facts; and one bounded next experiment. The coordinator and reviewer inspect this before any mutation probe.

## Disposable fixture inventory to prepare later

| Fixture | Required contents | Baseline record |
| --- | --- | --- |
| N1 | Multipage native notebook with handwriting, native text and a blank page | Document/page UUIDs, order, templates, scene/content/metadata hashes |
| P1 | Multipage PDF with original ink, highlights and native text where supported | Original PDF byte hash, native IDs, redirection mapping, annotation semantic snapshot |
| P2 | Disposable copy of P1 with a tablet-created inserted blank page | Native before/after file inventory and mapping difference; distinguish PDF page index from native page ID |
| U1 | Unrelated nonblank successor and visually blank page with off-screen/layer content | Proof blankness guard refuses adoption without changing content |
| B1 | Existing bound page, including edited/scrolled/moved variants | Binding source/target UUIDs and conversation ID, not just header screenshot |

Fixture creation, native manual insertion, backups, restoration and any device navigation remain coordinator-owned future actions. No menu-click automation. Archive the complete fixture-owned file set with file hashes and verify restoration on disposable copies before mutation experiments; copying an open UI's files alone is not a consistent backup proof. Legacy/cPages variants are included only when legitimately available, never fabricated as native evidence. Cloud remains unpaired/untested and original personal documents remain outside the fixture scope.

No additional native feasibility result follows from completing this document. Candidate A-F and Q0-Q10 remain open.
