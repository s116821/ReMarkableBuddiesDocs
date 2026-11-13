# Portable preferences in ordinary isolated backups

Implemented and exercised in local Windows fixtures at Buddy `54fc5a2`. The
first increment prepares and inspects a local package. The offline fixture
exercises the existing destination maintenance operations.
Cloud binding, upload, download, Manager orchestration, additional archive
generations and runtime activation are outside this increment.

## Composition and compatibility

Use the existing ordinary data-only format-1 archive and the existing strict
portable configuration V1 artifact. A separate package directory has three fixed
entries.

- `data/` contains the unchanged `backup.json` and its existing
  `objects/<sha256>` inventory. The archive is ordinary format 1 and its
  `config_snapshot` is null. The package requires nonempty committed history.
- `portable-configuration.json` contains the existing V1 portable artifact.
  Keep the existing three-key allowlist and raw declaration semantics. A valid
  saved configuration with no portable declarations contributes the normal
  V1 artifact with empty settings.
- `isolated-backup.json` is the sole package completion marker. It is strict
  JSON with exactly the fields in the example below. Each length is an integer
  and each SHA-256 is the lowercase hex digest of the exact file bytes.

```json
{
  "isolated_backup_version": 1,
  "data_backup": {"bytes": 1234, "sha256": "<64 lowercase hex characters>"},
  "portable_configuration": {"bytes": 123, "sha256": "<64 lowercase hex characters>"}
}
```

Names are fixed by V1. The marker cannot redirect either path and carries no
source Config hash, actor/device/account/backup identity, provider root, or
mode epoch. Provider custody belongs outside the package. The data marker's
existing manifest and object references cover the data closure. The portable
reference covers its exact bytes, including any accepted encoding differences.
The package identity is the raw SHA-256 of the outer marker. An explicit
inspector can report this identity, component identities, counts and media
completeness without exposing the preference text. These digests establish
correspondence; trusted transport and separately verified provider binding
establish provenance.

A legacy inspector or restore invoked on the package root refuses because its
required `backup.json` is absent. An operator can explicitly select the
`data/` child with an existing reader. That is a data-only operation and
cannot inspect or apply the package's preferences. No old archive discriminator
or format-1 schema changes.

## Capturing one package

The caller supplies an explicit saved configuration path that is bound to the
source Store. Reuse safe paths and canonical disjointness for the destination,
the saved file and all Store roots. Read the actual saved bytes and validate
the entire duplicate-free document with `config::inspection::document`. Use
the parsed paths to verify the source Store association. Reuse the existing
raw-declaration projection and V1 validation over those bytes, and keep
the Config and its raw source digest in memory only. The boot-time typed
`config.snapshot.json` materializes defaults and is unsuitable as the
source of declaration presence. Environment/model resolution and credential
loading are outside this path.

Under the existing archive mutex, verify the live same-Store isolated lease
and current generation, capture the archive inventory, and pair it with one
exact saved-file observation while that history remains pinned. Recheck the
saved path and exact-byte digest before publishing the outer marker. A change
refuses the attempt; there is no rebase onto a second config capture. This
gives a stable observed pairing while archive history is pinned. It does not
claim the file could never change after the check or that captured preferences
were effective in an already-running process.

Empty history returns no work before reading the configuration or creating a
destination, even when portable preferences have been declared. There is no
configuration-only isolated publication in V1. For nonempty history a
missing, invalid, foreign, or changed explicit saved file fails the package.
The standalone data-only snapshot remains available through its own existing
path and is never substituted as a successful package.

Reserve a new private package root with the existing archive path protections.
Write and verify the existing data child and the portable artifact before the
outer marker. Keep `backup.json` and `objects/` construction on the existing
writer, and verify both staged components against the bytes to which the
outer marker refers. A fault before outer publication leaves incomplete
staging. If publication may have happened, inspect that exact original root
and expected marker digest. Do not reuse the directory for a fresh attempt.

The explicit package reader accepts only its fixed regular files/directories
and content-addressed inventory under the existing safe-path rules. Bound
the outer marker to 16 KiB, the data marker and closure to the existing
ordinary inspector limits, and the portable input to its existing 128 KiB
limit. Reject duplicate/unknown fields, unsupported version, missing or
swapped components, size/hash mismatch, a non-null config snapshot, invalid
portable fields, or missing/corrupt promised objects. Check and parse the
same bounded marker/artifact byte captures rather than validate one file
read and parse another. An intentionally omitted sample remains visible as
incomplete media in the data inspection. Do not offer a valid package result
when either required component fails verification.

## Explicit destination maintenance

The future Manager flow stages one exact package over the wired connection,
verifies its marker digest and both components in private custody, and
binds each chosen command to the corresponding verified content. Do not
resolve children again from an untrusted or replaceable download path.
Recheck the package and data marker against the original restore intent
before conditional ordinary Prepare/Apply. Reuse the existing data restore
validation, CAS and activation, preserving the destination's distinct
actor and all device configuration. Imported native references stay
historical. Recheck the exact portable bytes in staging and pass their
validated V1 value to the existing portable import Prepare/Apply/Status.
The package component hash pins raw bytes; import still pins the existing
serialized artifact digest plus destination Config path/base/target hashes.

The operator may decline preference import or inspect/confirm it after data
restore. Use the present-only overlay: omitted fields stay as declared at
the destination, supported null is a declaration, and existing no-change
behavior leaves exact destination bytes untouched. The portable import keeps
its existing supported ordinary destination family, absent/LocalOnly mode,
and stopped, exclusively owned Config/Store preconditions. Data restore and
preference import have separate outcomes and original Status on uncertain
acknowledgment. A corrupt or stale preference operation cannot roll back a
previously verified data restore or silently apply a different artifact.
No configuration action changes destination actor, paths, credentials,
connection settings, mode or runtime activation.

## Implementation and evidence

Use `src/storage/recovery.rs` for the existing locked archive collector and
writer, a focused child module for package composition and inspection,
and `src/config/portable.rs` for a small internal projection entry point.
Extract the existing bounded ordinary archive parser from its path reader
only if needed to validate the already hashed marker bytes. Use the current
ordinary restore and portable import interfaces in the fixture. Keep the
existing public archive/portable commands and behavior; this first package
producer/inspector is callable from the future worker and Manager adapter.

Exercise one nonempty real Store through package preparation, offline
inspection and existing restore to a distinct actor. Retain exact records
and media, sparse values, supported nulls and Unicode text. Prove no eligible
settings and empty history are distinct. Cover invalid whole source input,
foreign path, changed config at the marker boundary, old-reader refusal at
the outer root, wrong/unknown outer version and fields, hash/size substitution
of both components, promised missing media, true omission, and an interrupted
outer marker. Demonstrate actual portable Prepare/Apply separately, with
private destination settings preserved, plus stale/different artifact and
already-restored data unaffected. Report host fixture evidence separately
from later provider, wired, tablet and runtime qualification.

The final Windows build passed the four package tests. Its restore fixture
used the strict package reader's verified artifact value and the actual
portable import Prepare, Apply and Status calls. It verified exact screenshot
bytes and history for a distinct destination actor, unchanged destination
Config through data restore, and preservation of private and omitted
destination settings through import. The package fixtures also exercised
original-marker observation, pre-rename Config change, exact membership,
invalid preferences under a matching hash, and incomplete media reporting.
The Linux rename-acknowledgment fault is present in the fixture. Windows
exercised post-publication readback and original-only observation.
