# Inspect Buddy-owned storage without changes

`reader-buddy --inspect-owned-data` emits a versioned JSON inventory of existing
Buddy-owned data and cache files. It does not start the Reader, initialize or
repair a Store, clean temporary files, read provider credentials or native
documents, contact a provider, or change a service.

The backend is available in the source increment paired with the active
[inspect-owned-data change](../openspec/changes/inspect-owned-data). Browser and
Electron integration remain future REM-42 work; this does not provide a Buddy
admin listener or establish working tablet transport.

## Manual invocation

From a built application, use the normal known nonsecret configuration:

```text
reader-buddy --inspect-owned-data
```

For a selected existing configuration on Linux/macOS:

```sh
REMARKABLE_BUDDIES_CONFIG=/absolute/path/config.json reader-buddy --inspect-owned-data
```

For a host fixture in PowerShell:

```powershell
$env:REMARKABLE_BUDDIES_CONFIG = 'C:\absolute\path\config.json'
.\reader-buddy.exe --inspect-owned-data
```

The command does not read `.env` or resolve model credentials. Simulation,
provider/key/model, trigger and `--debug-dump` options conflict with inspection.
Invalid configuration produces a sanitized unavailable report, not private
parser values or an attempted ordinary startup. No directory or lock is created.

## Read the report

`report_version: 1` identifies the schema. Exit zero means a report was emitted;
inspect `status` to understand the result:

| Status | Meaning |
| --- | --- |
| `complete` | The declared data/cache inventory and reference accounting completed under the cooperating-writer lease |
| `partial` | Some input was missing, omitted, unsafe, unreadable, unexpected, inconsistent or beyond the global scan bounds |
| `unavailable` | Required configuration, ownership, CURRENT or the existing lock was unavailable |
| `unsupported` | Paths, ownership/format or locking are unsupported; no repair or fallback followed |
| `busy` | An existing writer holds the stable lock; the command does not stop it or retry with write access |

The running Reader normally owns the lock for its lifetime. A caller may need
separately authorized maintenance before a coherent inventory can run. This
command does not perform that maintenance.

`observed_apparent_bytes` is the sum of known file lengths, each owned relative
path charged once. `complete_apparent_bytes` is JSON `null` unless the declared
inspection completed. These are neither allocated filesystem blocks nor bytes
that may safely be deleted. Identical content in another retained generation has
another path charge; hardlink/reflink allocation deduplication is not claimed.

`storage` separates structural files, record metadata, media objects, unclassified
objects, retained generations, cache, owned diagnostics and staging. Current and
historical retained files remain stored bytes; their presence is not live logical
membership or cleanup permission. The reserved external diagnostic location,
legacy cache, native documents and credentials are explicitly outside this scope.

`observed_domains` separates Conversation, Source, ExportAssociation, SubjectMemory
and Handwriting metadata. Declared and physically present media-reference bytes
are unique within a namespace but nonadditive across namespaces. Shared files
receive one storage charge. Missing, uninspected, length-mismatched and deliberately
omitted references remain distinct; an omitted selected reference stays omitted
even when retained metadata leaves its bytes physically present.

Only bounded JSON metadata is parsed. Media content is not read or hash-verified,
and no native health/current page, logical liveness or complete recovery is inferred
from a matching filename or size. Fixed issue codes/counts disclose incomplete
states without saved text, unexpected filenames, raw parser errors or credentials.

## Limits and evidence

The scan shares existing global entry/reference and parsed-JSON limits, plus
per-file record limits; reaching a bound yields incomplete status instead of
truncating into an exact total. Symlink/reparse and configured-root alias checks
preserve known-path boundaries. Current supported Store generation formats are 1 and 2,
with the existing actor/generation feature marker. Conversation schema 2 uses the
current typed validator rather than the older embedded schema's constant 1.

The read-only existing-file lock coordinates normal Store writers. Unix identity
checks use device/inode; stable standard-library Windows file-ID access is unavailable
at the supported compiler, so its handle/path metadata bracket is weaker. Neither
is an atomic guarantee against an out-of-contract external writer. Read access can
update access timestamps; nonmutation checks preserve content, paths and modification
times rather than claiming immutable atime.

Current local checks use real temporary Stores and actual CLI subprocesses;
hardware, Manager UI/transport and whole-feature release verification remain separate
gates. See the owning change for exact source revisions and observed results.
