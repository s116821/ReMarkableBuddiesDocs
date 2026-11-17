# Capacities prepared note export design

The adapter accepts an access credential from its caller. It compares `GET /space` with the explicitly selected space UUID before reading or writing. Both create and update read `GET /space/structures` and require exactly one writable `content` property on the Page structure. Create additionally verifies writable title and, when selected, tags; each configured tag is a known same-space `RootTag` object ID. One typed create stores the title, selected tags, a stable identity marker and readable Markdown content under a managed GroupBlock. Later updates replace only that verified group. Legacy version1/2 records retain their literal Markdown CodeBlock interpretation and original readback behavior.

The existing ExportAssociation namespace gains a separately versioned Capacities payload under the schema-two export envelope. Its record key deterministically includes provider, space, conversation and the portable correlation. The portable correlation remains in the provider evidence and in the remote identity marker. Structure, source scope and the association key remain immutable. Each attempt carries its own operation identity and exact payload digest. Existing Mem record keys, serialized payloads and dispatch semantics remain intact. The Store already reserves domain schema three for notebook records, so this increment uses the existing export envelope and preserves the installed Store contract files.

A fresh Ledger preparation authorizes at most one polled write. The caller shares the existing Store export owner and cancellation boundary. The preparation receipt binds an effect ID to its first scope within the Store. An explicitly selected different space needs a fresh effect ID. A valid create response provides a candidate ID. Commit that candidate before readback, then verify the exact object, structure, exact attempt marker and exported payload through a same-space `GET /object`. Only verified readback binds the native ID. Candidate IDs cannot be reassigned. If an accepted create has no durably retained ID, later attempts stay unresolved. Search and cursor listing cannot prove identity or absence strongly enough to authorize another write. The shared Ledger governs dispatch within this Store. The provider gives no cross-Store deduplication guarantee.

The existing Writer and notebook flows retain their ExportOwner through Capacities dispatch. A provider-specific dispatch boundary selects the existing conditional-version destination or the Capacities adapter; it does not invent a numeric Capacities revision or reacquire the Store owner. Writer admission compares the portable correlation and effect ID within the provider evidence, and validates the provider-scoped association key. It retains the selected draft/source guards, original deadline, cancellation, and immediate pre-write currentness check. Pending checks use the selected provider and space before starting another generation. Original-only reconciliation reads the original association and never changes its provider or space. Legacy Mem entrypoints and record meanings remain compatible.

Saved destination selection adds the explicit `capacities` choice without changing absent or explicit legacy Mem settings. The portable product preference contains only the backend choice. A separate local `capacities_export` configuration contains version one, the selected space UUID, a stable enrollment grant UUID, and an ordered unique list of at most 16 tag UUIDs. The initial object type remains Page. Importing portable preferences cannot create a connection or copy these account-bound identifiers.

Each successful OAuth enrollment receives a grant UUID that survives token rotation but is not reused for replacement consent. A bounded private credential record lives at the fixed `capacities-grant-<grant UUID>.json` name within the existing credentials directory. It binds its version, grant, space, public client ID, resource, granted scopes, expiry, and OAuth tokens. Secrets are not logged, serialized into preferences or sent to the Manager renderer. A credential read validates the exact selected identity and freshness; missing, expired, mismatched or unsupported records refuse without borrowing the current account. OAuth publication, rotation and confidential transfer require their separately implemented ownership boundary; reading an existing record does not create or refresh a grant.

Configured exports bind the enrollment grant in operational Capacities evidence and the Writer intent as well as provider, space and type. Unconfigured adapter fixtures may retain no enrollment identity, but cannot qualify authenticated command reconciliation. New command work resolves its explicit destination and required credentials before Store creation or model invocation. Original-only command reconciliation opens an existing compatible Store without initializing one, finds exactly one matching conversation/correlation association through the existing bounded index, and uses that record's provider, space and enrollment. Ambiguous legacy-plus-Capacities matches, conflicted rows and missing original credentials refuse. The selected current backend, space, tags and writer-enabled flag do not redirect historical reconciliation. Existing ready notebook stores remain supported without admitting an unrelated selected runtime mode.

The API assigns object IDs and provides no conditional revisions, transactions
or idempotency for these writes. The reviewed update policy changes only the
app-managed GroupBlock. Compare its exact last-verified identity/content subtree
before dispatch; an observed edit inside that group conflicts. One targeted
`PATCH /blocks/block` replaces its children while retaining its group ID/type.
Omit title, tags, marker and outside siblings. Compare desired semantic content
on readback, then retain the new verified descendant identities as the next
baseline. No automatic retry follows a possibly sent write. A concurrent edit
inside the same group between read and write can still lose under provider LWW;
this limitation is explicit and is not presented as conditional-write safety.

Before either create or update, require exactly one RootPage structure and one
`content` property definition with `writable: true`. Create additionally checks
the title and selected tags. A content-only update does not require those omitted
properties to remain writable. The provider's structures documentation lists
block-map IDs in property definitions, but its current type enum has no block-tree
type; this check deliberately does not invent one or equate richText with blocks.
Missing or ambiguous content capability refuses pending provider qualification.

Readable content uses the maintained `pulldown-cmark` parser, pinned at 0.13.6
without default features. Map supported paragraphs, emphasis, links, code, lists,
tasks, quotes, equations and rules into writable provider blocks under one group.
Headings use separate bold text with documented Base/0 hierarchy; heading levels
are deliberately flattened. Do not invent undocumented hierarchy values. Ordered
lists initially require a starting value of one. Unsupported images, HTML,
tables, footnotes or formatting combinations refuse before mutation without
fetching any referenced content. Keep source characters unchanged, with smart
punctuation disabled. Bound input by existing200000-byte content/256KiB payload
limits, with at most4096 blocks,16384 tokens and nesting depth32. The semantic
projection has a fixed mapping revision and excludes provider-assigned IDs;
identity baselines additionally bind those IDs. Recognize only explicitly defined
equivalent defaults: absent/false supported text-style flags and absent/null list
or toggle metadata. This is the mapper's normalization policy, not a promise of
provider serialization. Other unfamiliar fields or token segmentation
conservatively fail verification.

Introduce explicit representation evidence version3 for managed groups; retain
versions1/2 with their original Markdown CodeBlock interpretation and hashes.
Historical CodeBlocks are never converted or replaced silently. Their original
readback/reconciliation remains available, while changed content requiring a
format migration reports unsupported. A fresh association cannot begin with an
update: its baseline must descend from the verified original association. After
a crash that leaves an update Prepared despite a possible PATCH, exact-target
readback may persist the missing candidate transition and then completion; it
never resends. A newer pending update does not replace an older requested
operation's retained result. Provider normalization and actual tablet acceptance
remain pending in this change. Private attachments remain outside scope.

The Manager is an OAuth consent broker; the tablet redeems the authorization code and owns token bytes from their first receipt. Both Manager hosts share a bounded `oauth4webapi`-based S256/state callback implementation. Production metadata discovery is pinned to the Capacities HTTPS issuer and validates the required endpoints, resource and API scopes; advertised MCP registration or another client's public ID does not authorize REST access. Maintainer registration must supply a verified public client ID and exact redirect before consent is enabled. The proposed common redirect is `http://127.0.0.1:48761/oauth/capacities/callback`; no ephemeral-port or alternate-URI fallback is allowed without provider registration.

Consent belongs beside the existing Reader/Writer destination setting, with Connect, Reconnect, Disconnect, verified space and requested tags. The browser host redirects from a protected same-origin action; Electron main opens the external browser. Application renderer messages contain sanitized state, never the code, verifier, callback parameters or tokens. Bind one private host-side flow to its original tablet/connection/boot, config digest and enrollment operation. The callback has a one-use random state, exact method/path/host/peer checks, bounded lifetime and clean response. Use the existing confidential wired pattern for a dedicated code/verifier command, not a general remote command or arbitrary-file interface.

The tablet durably fences a possible code exchange before one token request, validates grant scope/expiry and `GET /space`, publishes the protected grant, then commits its local config pointer against the original digest. Lost replies resolve through original-operation status only. A verified staged grant can finish the same local commit while the original config remains current; an uncertain token exchange cannot replay the code. A tablet-side per-grant owner serializes CLI/daemon credential use, refresh and revocation. Pending rotation must be durable before refresh; publish replacement bytes before reopening the grant. A lost refresh response requires reconnect, never retry of the revoked old token. Every credential reader must honor these lifecycle fences before real OAuth is enabled. Manager never refreshes a second copy.

The grant custody foundation uses a permanent private per-grant lock inode and
nonblocking OS ownership. All configured exports retain that owner alongside
their provider destination. Pending exchange, staged, active, pending rotation,
local disablement, pending revocation and confirmed/unconfirmed retirement are
closed local states. Visible record bytes alone cannot report durable settlement:
status, staged activation and access first sync the credential directory and
recheck the same record digest. Refresh/revocation lend their token once from a
live permit; the consumer must retain it through the actual request and result.
A publication error leaves the original operation unresolved until durable status
reconciles the visible record; it does not authorize a retry.

The first tablet command increment covers exchange and original status/resume.
It reuses the protected stdin-only CLI and existing config publication/CAS,
requires an existing compatible Store actor and current boot/config binding,
and caps its request body at32KiB and original monotonic allowance at30 seconds.
Each fixed metadata/token/space HTTP operation is limited to10 seconds or the
remaining original allowance, whichever is smaller. No redirect, proxy fallback
or automatic retry is allowed. Production registration remains absent, refusing
new exchange before Store/grant mutation or HTTP. Resuming a staged publication
also requires the approved client to match its original enrollment, and its
exact staged expiry must remain viable before config CAS and activation.
An independent armed signal watcher stays responsive during synchronous disk
settlement; the actor rechecks cancellation and config currentness at the actual
token-request poll and before starting publication/activation. The bound USB connection digest
is supplied by Manager's trusted transport; the tablet does not claim to observe
host USB identity. No code or verifier is persisted or returned. The actor stages
private verified bytes, commits the config pointer last, syncs and rereads that
exact config before activation. Status/resume cannot create a Store, repeat a
pending exchange or replace an unrelated config revision. Refresh/revocation CLI
integration and the confidential Manager transport remain separate unfinished
steps of this same change.

The additive read-only `capture` selector accepts contract version1, a bounded
budget and only the Manager connection digest and expected boot in its binding.
It returns `captured` with the actual existing Store actor UUID, current boot,
echoed Manager connection digest and exact durable saved configuration SHA256.
It never creates a Store, configuration or enrollment and never contacts the
provider or scans unrelated commit/object payloads. Missing or incompatible state returns sanitized `unresolved`. Existing
exchange/status/resume request and receipt shapes remain unchanged. The trusted
host obtains identity through this protected command rather than parsing raw
configuration files or traversing unrelated owned data.

The confidential transport holds the existing MaintenanceIO owner and validates
the fixed installed executable, boot and USB connection. Before sending the
code/verifier, it repeats capture and executable metadata checks on the same SSH
transport; the earlier UI currentness check is not authority to send secrets.
Only stdin carries the proof. Neither command arguments, renderer messages,
temporary files nor error logs contain it. The fixed exchange command selects
an attestation prelude in the running Linux actor. Before reading stdin, config
or Store state, that actor opens its own `/proc/self/exe` once and hashes the
exact regular file with an eight-second,128MiB bound. It flushes one fixed
digest line; Manager compares it with the original capture without disclosing
the expected digest to the remote command. Only then may USB/deadline checks
permit the confidential frame on that same SSH channel. The running ELF remains
the measured recipient across atomic path replacement, and Linux excludes
ordinary in-place writes while it executes. This protects normal trusted
installation concurrency; it does not attest against malicious root code.
The private port consumes its original
handoff once and permits later status only against that original binding.
A later status read reporting an absent grant does not settle a possibly sent
exchange: its original remote process may still be running before its durable
fence. Only the original settled receipt or positive original terminal evidence
can retire that uncertainty; absence never permits replay.
Conversely, a normally closed trusted child that positively reports refusal
before its first confidential send, or a proven local no-child failure, can
settle the original handoff as not dispatched. Timeout, termination and partial
delivery cannot use that disposition.
Structured receipts require full stream settlement and matching identity; an
empty receive buffer is not EOF or proof of completion.

Capture/current/status use child12s and host13s. Exchange uses child60s, host61s
and broker62s, still inside the original five-minute consent lifetime. These
up-front exchange caps reserve setup separately: a recent protected tablet sample
took10.688s before remaining owner checks, so an8s setup allowance is insufficient.
After its
last identity gate and channel admission/open/exec, before the first confidential byte, the child must have all30s of
actor allowance plus4s for postflight remaining or refuse without sending.
Provider metadata retains its10s operation bound. Callback currentness and
exchange have separate phase clocks without renewing consent; unrelated
operation budgets remain unchanged. Hosted source checks and installed tablet
qualification remain separate acceptance steps.

Disconnect disables local use first and records remote revocation separately. Keep a private revocation-only token until confirmed or deliberately retired. After uncertain rotation, a successful response for an older token cannot prove the unknown successor revoked; guide the user to the provider's Connections page. Reconnect creates a new enrollment and cannot settle an unknown note export or redirect its original association. No grant/code/verifier is part of portable preferences, backups or device clones. Source fixtures can exercise the protocol before a verified client exists; they do not qualify real consent, tablet egress or installed behavior.

Official contracts [OpenAPI](https://developers.capacities.io/openapi.json), [concurrency](https://developers.capacities.io/api/overview/concurrency), [objects](https://developers.capacities.io/api/concepts/objects), [properties](https://developers.capacities.io/api/concepts/properties), and [REST OAuth](https://developers.capacities.io/api/overview/authentication).
