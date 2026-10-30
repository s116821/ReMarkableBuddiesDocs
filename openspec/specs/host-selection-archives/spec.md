# Host selection archives

## Purpose
Explicit selected-history export and independent offline archive custody inspection.

## Requirements

### Requirement: Explicit selected archive export
The application SHALL expose a one-shot selected-history export using existing custody policy and valid existing owned storage. It SHALL exclude configuration/credentials/runtime trees, preserve source data and publish only a verified new external archive. It SHALL retain Store/current-mode lifetimes through output without normal initialization, repair, service stop or ordinary export fallback.

#### Scenario: Preserve selected historical custody
- **WHEN** a selected Store with winner, retained history/media and unrelated committed scopes is explicitly exported
- **THEN** the new archive preserves the existing verified custody closure and media-completeness truth while source selection/data remain unchanged; no live selection or restore authority is returned.

#### Scenario: Busy or unsafe destination
- **WHEN** storage is unavailable/unsupported/Busy or a destination exists or overlaps an owned root
- **THEN** export refuses without replacing storage, stopping its owner or overwriting the destination.

### Requirement: Independent offline archive inspection
Inspection SHALL use the existing complete format1/2 archive validator without runtime configuration, live Store opening or archive mutation. It SHALL return bounded counts/media completeness only and SHALL NOT convert missing/corrupt/incompatible input into empty success or current membership.

#### Scenario: Historical format2 archive
- **WHEN** a compatible selected archive is inspected with no runtime configuration or Store
- **THEN** exact history/object closure is validated and counts/completeness are reported without creating owned roots or importing native/group authority.

### Requirement: Bounded input and uncertainty-preserving output
Archive commands SHALL accept strict inclusive16KiB JSON from an absolute regular file or exact-dash stdin with caller-owned EOF/deadline/cancellation, before runtime initialization. They SHALL produce one bounded report-v1 JSON line with sanitized status and activation_performed=false. Export SHALL execute once and retain ownership through its consuming output; partial output or uncertain I/O SHALL NOT trigger another report, automatic retry or cleanup of a possibly complete archive.

#### Scenario: Failure after marker publication
- **WHEN** export or output fails after backup.json may have been published
- **THEN** uncertainty remains explicit, source/destination are not automatically replayed or deleted, and deliberate inspection of the original destination can establish archive custody without activating it.

#### Scenario: Input or prefix-write refusal
- **WHEN** input is unsafe/malformed/oversized or a writer accepts a prefix then fails
- **THEN** unsafe input does not open storage/create a destination, and output failure appends no replacement JSON or repeated export while held guards release.
