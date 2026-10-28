# Explicit native capture setup

The existing version-1 single-Observe experiment remains unchanged. A version-2
native candidate may additionally select a capture plan: expected document UUID,
page UUID and complete ordered page UUID list (one through seventeen entries).
These are independently selected fixture intent, not observed Reader authority.
The existing reviewed profile/library hashes remain compiled into the observer.
Both examples now require `--features development-resident-bootstrap`; the
separate diagnostic CI build supplies it. Normal release packages do not.

The actor and observer each end their launch input admission explicitly. They
exchange durable records bound to the candidate digest, nonce, observer process
and complete resident runtime incarnation. Setup-ready is published only after
both admissions ended. Only then may a separately reviewed developer setup driver
open the disposable source. Product code performs no menu setup. The unchanged
native library contains no fixture-opening hook.

Setup-complete must echo that exact binding. It is a completion signal for the
setup action, not a claim of page readiness. Both participants acquire fresh input
observers exactly once and require quiet/released input. Neither resets a canceled
guard. Each waits for the other's fresh-admission record while continuing its own
quiet checks. Duplicate, preexisting, partial, changed, stale or misbound records,
process replacement, service/context changes and deadline expiry abort the run.
Records are exclusively created and synced before a separate completion marker;
readers retain file pins through capture. Failed attempts are never replayed.
After the reviewed developer setup has ended, the fixed
`resident_bootstrap_control setup-complete NONCE` entry verifies the candidate,
original actor and stopped services, both ended-admission records and the ready
binding, then publishes completion exclusively. It performs no UI action.

The observer uses one overall 180-second bound from entry, at most 60 seconds for
launch, at most 120 seconds for setup, and at most 10 seconds for its single
CaptureSource request, each capped by the original overall deadline. Setup cannot
renew any deadline. Existing actor/PID1 and independent recovery bounds remain.
The runtime, artifact and inactive-service checks continue throughout setup;
transport readiness never substitutes for Reader identity. Capture itself proves
both native source/full-order joins through the SDK. There is no preliminary
Observe, repeated request, page insertion, navigation or writing in this mode.

After both fresh admissions, explicitly reconnect once to the same verified child
before sending CaptureSource. The initial connection may have reached the SDK's
30-second idle retirement while setup was in progress. Reconnection and capture
share the same at-most-10-second request bound and all fresh guards/pins. This is
not a retry after capture failure. Test idle retirement with the actual owned
runtime/peer, proving one new handshake, unchanged child, one CaptureSource and
zero Observe/effect commands; guard refusal or expiry must send no capture.

Always shut down the owned child before reporting capture or setup failure. Save
the validated PNG and its identity/hash metadata as historical evidence only.
Original uncertain mutation history remains untouched. Stock-first independent
recovery remains mandatory even when preservation or capture fails.

Source preservation remains byte-exact before setup and for candidates without
the following explicit policy. An optional version-2 opening-metadata policy may
carry the exact original UTF-8 bytes of the selected document's `.content` and
`.metadata`, at most 64 KiB each. Their SHA-256 values must match their original
entries in the complete backup manifest. Paths are derived from the canonical
selected document UUID; callers cannot exempt arbitrary paths.

After a durable setup-ready record is verified against both ended-admission
records and the original candidate binding, actor and recovery may accept only
these typed activity changes in those two files:

- `.metadata.lastOpened`: a canonical decimal timestamp string, nondecreasing.
- `.metadata.lastOpenedPage`: an integer equal to the original index or the
  selected fixture index within the complete original order.
- `.content.cPages.lastOpened.value`: the original remembered UUID or selected
  fixture UUID, both within that original order.
- `.content.cPages.lastOpened.timestamp`: a canonical `client:counter` string
  with the same client and a nondecreasing counter.

Monotonic comparisons are against the original backed-up values at each
checkpoint, not a claim about every intermediate write. A changed remembered UUID
requires an advancing register counter; a changed remembered page index requires
an advancing `lastOpened` timestamp. Retain both original and sampled resulting
metadata bytes in the private evidence, including rejected samples.

The policy declares permitted incidental activity; it does not claim that
opening necessarily changes these fields or that remembered values prove the
actual displayed page. Strict recursive parsing must reject duplicate keys.
Every other key, typed value and array order must match the original JSON. No
protected numeric token may be rounded before comparison: preserve its exact
JSON text, including integers beyond `u64`, precision and exponent notation.
Equivalent alternate numeric spellings may conservatively refuse. No
addition/removal of keys, file or directory is permitted. `lastModified`,
`sizeInBytes`, page `modifed`, `.local`, PDF, ink and thumbnails remain protected.
Both source files must still be regular protected files, read under retained
pins, and their bytes must match the sampled inventory. Every other file remains
byte-identical. No on-device metadata rewrite or restoration is introduced.

The actor uses this same rule at completion as recovery uses after restoring
stock. A missing setup-ready signal leaves byte-exact policy in force; malformed
or mismatched phase evidence refuses the allowance. Preservation failure still
withholds Buddy while stock restoration comes first. A whole-directory exemption
is forbidden. Source/host checks do not qualify actual opening or create a runnable
native packet: freeze and review the setup driver, artifact set and fresh source
admission separately before selecting the bounded native capture.

Owned host tests must cover the two-participant barrier, delayed/partial records,
wrong binding, replacements, input cancellation, expiry and single-use admission.
These model process coordination only; actual UI setup and persistence remain
native acceptance requirements.

## Copied-reader visual setup helper

The existing screenshot helper assumes a stock process named `xochitl`. The
resident launcher instead copies the executable into the candidate-owned
`/run/rsdk-bootstrap-<nonce>/session/reader` and launches that path. Developer
setup MAY use an explicit process-bound screenshot mode under the existing
development-resident-bootstrap feature. It SHALL require the complete boot/PID/
start tuple, canonical candidate nonce and expected executable SHA-256. Ordinary
stock discovery and its process-name checks SHALL remain unchanged.

This mode SHALL derive the exact copied-reader path from the nonce, require the
running executable link to that path, and verify a bounded executable hash before
reading memory and again before publishing pixels. Closing content verification
SHALL NOT rely solely on file timestamps, which can be too coarse to distinguish
same-size writes. It SHALL retain the executable file handle and compare the
original file identity, ownership, permissions, length and modification/change
timestamps through capture. The admitted process name may be `reader` or
`xochitl`; neither name alone confers authority. A changed executable, path,
process identity, mapping or allocation header SHALL refuse publication. The
existing ambiguity and framebuffer-layout rules remain unchanged.

The helper SHALL neither rename a process nor send a signal or input. Its pixels
remain visual setup context only. Each developer input selection requires fresh
visual inspection, and any selected tap requires a successful tap result plus a
successfully retrieved and inspected after-image before setup completion. A
failed or uncertain tap SHALL prohibit completion; before-only completion is
permitted only when no tap was selected. The original setup deadline remains.
