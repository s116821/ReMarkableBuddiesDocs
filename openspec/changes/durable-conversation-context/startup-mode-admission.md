# Application startup and selected receiving mode admission (before code)

## Exact available inputs and ownership

Main source base is `4d539b80a743f5c5e515ff460f5c0d35fb73e161`, Docs base
`4ef142cbf58ebe5857526c5a4958729f895d4ac0`, existing checkouts on focused
`feature/rem-37-mode-admission` / `docs/rem-37-mode-admission` branches.
Preserve all nine working inputs and committed SDK d01. No new checkout,
account/transport/tablet action or SDK API/facade is selected.

Generic mode implementation is the independently accepted repaired source
`7987da337a78be32d4ed3a41524e3853e925abcf`, with Docs
`df7cb0e267e2347ba69286e689798f0d938c1929`. Reuse only its relevant mode module,
Store lifetime plumbing, existing Drive ID validator visibility and legacy
publisher composition. Preserve Main's bounded-read helpers and domain code;
do not merge whole Cargo/config, unrelated outbox/transport or archive changes.
Record exact blob/hunk provenance and independent acceptance before adoption.

Main read the current REM-52 description and all 63 timestamped comments. The
latest mode-history repair and separate read-only slot review supersede earlier
unaccepted c572/pointer states. Whole provider/bootstrap/worker/native gates and
the later human 1% reserve remain separate. SCRAPPY confirmed the precise
[accepted lifetime boundary](https://github.com/s116821/ReMarkableBuddies/pull/31#issuecomment-6134542171).

## Concrete problem

The executable currently understands `reader.selection` but does not read the
persisted sync-mode choice before deciding ordinary versus selected startup.
It can therefore attempt ordinary credentials/device setup even when the Store
has an explicit nonlocal mode requiring another implementation. Selected current
inspection also has no configured shared-mode lifetime pin through its writer.

The existing `LegacySyncLease` protects ordinary data versus selected publication;
it is not a mode lease. `LegacyPublisherLease` freezes old publisher lifetime and
requires mode metadata absent. `SyncModeLease` accepts only explicit IsolatedBackup
or SharedGroup; it must not be acquired as a fabricated local application lease.
No accepted LocalOnly/None read-mode lifetime guard exists. Keep live ordinary-loop
mode switching/epoch fencing explicitly unfinished; a startup check is not proof
of whole-operation mode admission.

## Frozen startup routing

Resolve final dotenv/config selection as already implemented. For an existing
owned Store, validate safe nonblocking admission and the actual mode snapshot
before credentials, model or device setup. Retain the admitted Store handle for
ordinary startup rather than reopen it behind an unrelated lease. If no Store
exists and no selected runtime is requested, preserve ordinary deferred creation
after credential/config validation; absence must not invent a shared group.

Use a real startup decision carrying either the admitted ordinary Store or the
existing fixed report. It replaces the current check/return/drop boundary, not a
second facade/registry. Fixed failures retain report version/status/private-output
rules. Normal owned Store recovery/metadata writes remain disclosed and separately
bounded; missing selected state is never bootstrapped.

- Mode absent: unconfigured legacy compatibility. Preserve existing ordinary
  startup and old publisher policy; do not call it shared mode. Explicit selected
  metadata inspection/startup remains the existing compatibility path, without
  asserting a configured provider/group or native authority.
- LocalOnly: ordinary local history/memory stays usable when legacy sync is off.
  A contradictory enabled legacy publisher refuses before model/device setup.
  Do not use an old publisher lease to make local-only reads work.
- IsolatedBackup: its matched application publisher/runtime is not implemented
  here. Refuse unsupported ordinary/nonlocal startup instead of sending through
  all-history fallback or inventing an account/root binding.
- SharedGroup: require explicit selected runtime configuration and matching group/
  binding. Retain the existing real shared-mode lease while validating selected
  domain state/startup availability. Root ID remains chosen metadata, not bootstrap
  or provider permission. Missing/mismatched selector refuses before credentials/
  device; matching startup still honestly reports committed SDK NoNativeAdapter.
- Corrupt/unsupported/foreign mode history: unavailable, preserving original bytes;
  never reinterpret it as mode absence or rewrite it to defaults.

Freeze fixed report mapping: LocalOnly plus an explicit reader selector is
Unsupported for startup/inspect/context, never an ordinary fallback. LocalOnly
without that selector proceeds locally only with sync disabled; contradictory
sync enabled is Unsupported. IsolatedBackup current startup/inspect/context is
Unsupported. SharedGroup missing/mismatched reader group/binding is Unsupported.
Malformed/foreign mode metadata is Unavailable; actual Store/mode contention is
Busy. Responses preserve existing fixed/private schema and echo no mode IDs,
provider root or credential data.

Absent or safe completely empty default roots may defer ordinary creation.
Partial, non-owned, symlinked or nonempty unsupported state must refuse before
credentials/device; do not equate it with absence. The admitted ordinary ArcStore
survives credential resolution into the actual Ledger/memory/Worker once, with
config/effective-source snapshots still after credential validation. No local
mode lifetime fencing is inferred from this startup reuse.

Fresh ordinary admission specifically requires cache and credential roots to be
absent or safe completely empty directories too. A regular auxiliary file,
nonempty foreign directory or stale owner marker refuses before credentials and
before creating data/identity/lock. Repeat that startup-only check at deferred
creation if auxiliary state changed. This does not change legacy maintenance
initialization's independent ownership policy. Focused controls must preserve
foreign auxiliary bytes with both absent and empty data, plus a safe-empty
positive and changed-after-admission negative.

## Selected current and historical commands

Current inspect/context receiving in configured SharedGroup retains the existing
matched mode lease alongside domain admission/Store lease and cumulative selected
budget through actual report consumption. Recheck group/binding/current epoch
within actual writer admission. The lease alone grants no catalog/provider/native
permission; current token/raw custody and strict domain validation remain required.

Both inspect and context retain the same private current report admission through
actual consumption. Context's no-data ChoiceNeeded response must also carry the
private token/raw-custody/budget/matched-shared-lease pins; an early unguarded
return cannot satisfy this promise. Public context data remains absent and no
model-ready or native authority is asserted.

Unconfigured selected compatibility remains explicitly non-shared. Explicit local
or isolated mode cannot silently authorize shared receiving: surface unsupported
for the selected current commands until a distinct local-selected policy exists.
Do not relabel a local data lease as an epoch pin.

Original pending recovery remains historical and token-free across later mode/
binding/root choices. It allocates nothing, publishes no operation, takes no live
shared-mode handoff permission and performs no provider/native/model work. Keep
its independently bounded original-request/custody validation and changed/missing
semantics. Mode choice must not erase the stored historical receipt.

Historical recovery bypasses current mode/epoch admission even if current mode
metadata is corrupt, provided the original Store/custody validation is otherwise
valid. Configuration scope and complete original request validation still apply;
this bypass grants no mode permission. All CLI pure input validation precedes
Store/mode admission: malformed or foreign input returns InvalidInput even when
the Store is held; only valid requests can report Busy.

No mode setter, account onboarding, root bootstrap, sender/apply integration,
new IPC service or live mode switching is enabled by this increment.

## Focused actual behavior and remaining gates

Verify through real temporary Stores/actual executable and writer: absent-mode
compatibility; local-only history with sync disabled; contradictory legacy publisher;
isolated/shared startup refusal before poison credential/device setup; matching and
wrong group/binding; malformed mode history; original recovery after leave/rejoin or
root replacement; current report's mode lease blocking transition until consumption/
drop; domain stale/replacement and exact raw custody remain guarded. Include owned
Store reuse and missing-default versus missing-selected state distinctions.

Reuse accepted generic mode/corruption fixtures in required suites, without treating
their prior execution as new Main domain evidence or duplicating remote matrices.
Source/spec independent review, exact committed SDK proof, paired publication and
required lint failures remain explicit. No new native authority follows. Full
ordinary-loop epoch fencing, native ReaderSourceAdmission/effects, current root/
account/app qualification, matched publishers, tokenizer and full lifecycle remain
open. The precise held 8112 operation is not replayed or broadened into a blanket
ban on unrelated permitted work.
