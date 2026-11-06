## ADDED Requirements

### Requirement: Explicit successor observer preserves released reports
The component SHALL expose a separate explicit bounded report3 inspection route
for supported formats1/2/3/4before runtime startup. It SHALL preserve the existing
selector and report1/2shapes/format restrictions, with no enum widening or automatic
storage adoption. Source: merged producer generation4 and released report1/2.

#### Scenario: Old and new request paths
- **WHEN** a legacy inspection or explicit v3 inspection is requested
- **THEN** only its defined version is emitted; legacy4refusal remains truthful and no Reader/provider/device starts.

### Requirement: Complete metadata accounting grants no mutation authority
The observer SHALL hold existing-only read custody through bounded output, validate
current/retained feature composition, account exact notebook metadata and descriptor
references without archived-media/original-document/credential-file reads, and preserve nonadditive
references. Every count SHALL be observed or explicitly unknown; overflow/bounds/
changed/foreign state SHALL withhold complete totals. Source: existing file/lease
accounting and delivered Source3/Conversation3descriptors.

#### Scenario: Mixed generations and shared source media
- **WHEN** generation4and older retained history share repeated descriptor references
- **THEN** each stored generation/path is charged once, notebook metadata remains a nonadditive subset, and no call/liveness/media-integrity/native-ready claim follows.

#### Scenario: Missing or changed feature and partial traversal
- **WHEN** required metadata/media is missing, unsupported, unsafe, changed or beyond a declared bound
- **THEN** inspection retains only observed facts, emits explicit issues/unknown totals and leaves all files unchanged without recovery or repair.

### Requirement: Lossless versioned counters and closed disclosure
Report3 SHALL use the exact closed schema and canonical unsigned decimal counters,
null unrepresentable byte aggregates, finite UTF-8/framing limits and strict status/
completeness invariants. It SHALL expose no protected content and SHALL keep backup,
restore, sync, provider and native readiness separate. Source: report1/2exclusions
and cross-host safe counter requirements.

#### Scenario: Large bytes and invalid numeric spellings
- **WHEN** a valid u64count exceeds JavaScript's exact-number range or a counter uses exponent/fraction/sign/overflow spelling
- **THEN** the valid count remains exact through both hosts and malformed input refuses rather than rounding into a healthy value.
