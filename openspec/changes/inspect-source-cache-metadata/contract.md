# Proposed source-cache inventory report_version1

Precode review only; this is not implemented behavior.

## Command and platform
`reader-buddy --inspect-source-cache` is a parameterless boolean route before
logging, normal Config/environment overrides, Store/provider/runtime startup.
Existing explicit REMARKABLE_BUDDIES_CONFIG selects one existing absolute nonsecret
Config; no ordinary default fallback, stdin, file/UUID/filter/paging input or
alternate command is accepted. Conflicting execution/config override modes refuse
through CLI parsing before protected startup. On non-Linux targets, return the
fixed unsupported report before any Config/root/lease admission or stdin read.
The API itself has no Read argument. Existing reports/commands stay unchanged.

## Existing-only admission
Reuse current private Linux header/lease custody: existing safe/disjoint configured
roots, data/identity.json<=1024bytes, data/CURRENT<=128, current generation's
format.json<=64 (ordinary supported1 only), cache/owner.json<=1024 and
normalized-sources-v1/owner.json<=1024. Config uses the existing bounded strict
reader. Require strict ownership markers/nonnull matching actor, nonnil generation,
namespace format1/kind, existing stable regular store.lock then cache.lock leases,
nonblocking custody and held/named device-inode identity. Never construct/open/
recover Store, initialize/chmod/repair/clean/publish or enumerate durable trees.
Credentials root is only a validated/disjoint configured path binding; no marker,
credential filename discovery, resolver or credential contents are read.

Enumerate only the fixed namespace, at most18 entries total: exactly the existing
owner.json/cache.lock plus at most16 canonical nonnil lowercase hyphenated
UUID.json regular files. Unknown names/types, staging, reparse paths, unsupported
markers, over-capacity and per-slot metadata length>33554432 refuse. Each admitted
slot's apparent length is0..33554432; zero is metadata, not a valid empty payload.
Never open, hash, decode or validate slot payload contents. No original document,
durable payload, other cache domain, source title/text/key or native API access.

Hold both leases through consuming output/failure. Recheck current Config/path/
resolved roots, marker hashes/actor, supported current format/generation, namespace
and named/held lease identities. Compare two sorted observations of slot IDs,
regular-file identity and apparent length; changes refuse as conflict, with no
partial entries. I/O or ownership/format failures map to fixed unavailable or
unsupported; an occupied existing lease is busy. No retry, fallback or repair.

## Closed report
Exactly these keys:
- report_version:1
- operation:"inspect-source-cache"
- status:"ok"|"unavailable"|"unsupported"|"busy"|"conflict"
- runtime_unverified:true
- cleanup_authority:false
- entry_payloads_read:false
- entry_payloads_validated:false
- source_freshness_verified:false
- byte_basis:"apparent-file-length-per-owned-slot; no-allocated-or-reclaimable-claim"
- actor:canonical nonnil UUID on ok, null otherwise
- generation:canonical nonnil UUID on ok, null otherwise
- entries:sorted array on ok, null otherwise
- total_apparent_bytes:checked integer sum on ok, null otherwise

Each entry is exactly `{document:CANONICAL_UUID,apparent_bytes:INTEGER}`. Sort by
canonical document ASCII bytes, no duplicates, max16 entries; sum<=536870912.
An admitted empty namespace is ok with [] and0, distinct from uninspected/refusal
nulls. No partial or success-looking array survives conflict/refusal. Maximum8192
UTF8 bytes including newline. Exit0 means one complete bounded report, including
refusal; exit1 means output/transport failure. CLI parse errors remain ordinary
parser failures and never start another operation.

## Authority and compatibility
This observer discovers candidate IDs/lengths only. It does not attest entry JSON,
key/freshness/health/reclaimability or authorize deletion. A later cleanup always
requires a fresh separate selected-slot inspect/prepare and explicit original
intent under the existing cleanup contract; inventory state is not a token.
Future Manager integration must preserve both browser/Electron behavior and wire/
physical session qualification; neither consumer is implemented by this slice.
