# Wire and custody

Use the existing archive selector with one explicit operation name.

```text
reader-buddy --archive-operation export-notebook --archive-input FILE
reader-buddy --archive-operation inspect-notebook --archive-input -
```

The request is exactly one JSON object with an absolute `path`. The file and
stdin request cap and the LF-terminated report cap are each 16 KiB. Export
uses the configured local Store and a new destination under an existing
trusted local parent. Canonical path checks keep the destination and all
configured owned roots disjoint, including case aliases on Windows.
Inspection reads only a detached, quiescent archive.
It ignores Store configuration. The operation names do not select another
format when admission fails.

The existing v1 report carries the explicit operation name and a complete
format-4 inspection summary on success. Activation is always false. A
refusal has null data. After a destination attempt fails, the archive root
or marker may exist. Recovery requires an explicit detached inspection.
The command makes one write and flush attempt. An output failure, including
an observable witness change after flush, fails the command without a second
frame. A caller must require a successful exit before using a report.

Manifest count, unique object count and current commit entries are each
limited to 4,096. Committed manifest reads use at most 16 MiB cumulatively.
The archive marker and unique record metadata retain their 8 MiB bounds.
Manifest object references are limited to 16,384 and an individual object
to 256 MiB. Unique objects may total at most 1 GiB. Content work is limited
independently to 8 GiB, combining metadata and media across validation,
copy, readback and marker checks. Fixed readiness reads reserve their
existing upper bounds. Limit exhaustion refuses the whole operation.

The existing Store lock fences cooperating writers. Detached inspection
compares the marker and inventory witnesses across validation and output.
This assumes a trusted local filesystem and a quiescent detached archive.
The archive contains the existing optional configuration snapshot when
present. Credential contents remain excluded.
