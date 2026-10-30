# Proposed report3 wire contract

This contract is unimplemented precode. schema.json is the exact closed shape.
The selector is `reader-buddy --inspect-owned-data-v3`, no input or private argv.
Output is one compact JSON object plus LF, at most32768UTF-8 bytes including LF.
Unknown/duplicate keys, trailing content, bad UTF-8 and truncated/nonzero/late host
results refuse; raw stderr is not public output.

All26top-level keys are mandatory. report_version is literal3. JSON numeric
tokens for that version and generation formats must use canonical unsigned
integer spelling; 3.0/3e0/4.0 refuse before normal JSON value coercion. status is exactly
complete/partial/unavailable/unsupported/busy. owner_actor/current_generation are
null or canonical nonnil UUID strings; they are observations, not action grants.
current_generation_format is null or integer1/2/3/4; retained_generation_formats
is a sorted unique list of observed supported noncurrent formats with max4items.
Unknown formats produce issues and incomplete status; absence from this list is
not proof of absence during partial traversal.

Counter is canonical ASCII `0|[1-9][0-9]*`, at most u64::MAX. Nullable byte
aggregate is Counter|null. FileUsage is exactly files:Counter and
apparent_bytes:Counter|null. DomainUsage has the same eight named accounting
concepts as the old contract: observed_record_files, observed_record_bytes,
declared_media_bytes, present_referenced_media_bytes, missing_references,
uninspected_references,size_mismatched_references,omitted_references; byte fields
allow null on overflow, count fields do not. Issues map exact known codes to
positive Counters, never zero or unknown strings.

storage keys are the existing8 storage kinds. observed_domains admits exactly the
existing6namespace names. observed_notebook_records admits exactly the3delivered
notebook record kinds and uses FileUsage. Partial maps may omit uninspected keys;
complete maps include all6domains and all3notebook kinds with explicit zero where
actually exhaustively absent. Notebook metadata bytes are already in the
namespace and physical-file accounting. notebook_record_totals_additive=false
and reference_totals_additive=false are mandatory.

Complete implies no issues, nonnull owner/current/known format and complete total,
domain_accounting_complete=true, cache_inspected=true and complete_apparent_bytes
exactly equal observed_apparent_bytes. Any other status has complete total null
and domain_accounting_complete=false. Busy/unavailable/unsupported do not label
empty maps/observed counters as a healthy empty Store. Partial preserves only
actually observed facts. Scope fields remain literal false for media-content
verification,logical liveness,credentials and native documents. Exclusions and
byte basis remain explicit. lease_identity_check is device-inode for admitted supported
Linux custody, or unavailable when no such custody was established; unsupported targets return an explicit unsupported report without
claiming a weaker platform guarantee.

Source/Conversation schemas are not changed by this report. Required source
archive descriptors count their present/missing/omitted media honestly. The report
cannot authorize delete/purge, restore, sync, adoption, provider work or native
runtime activation. Manager must validate semantic invariants in addition to
schema.json: decimal range, sorted formats, totals/status consistency, positive
issues, complete key sets and known-zero versus uninspected distinctions.


# Relational admission rules

These rules apply before either host displays report3; JSON Schema alone cannot
express all of them. Compare counts using exact decimal/BigInt arithmetic.

- The sum of storage.files equals observed_files, which is at most4096. The sum
  of all known storage.apparent_bytes equals observed_apparent_bytes when both
  are known. An overflowed category makes the overall byte aggregate unknown;
  a total-only overflow also produces null plus byte-count-overflow. No saturation.
- shared_media_files cannot exceed observed_files; known shared bytes cannot
  exceed known observed apparent bytes. Nonadditive declared reference bytes
  need not equal or fit physical bytes when referenced media is absent.
- Archived-source notebook file/byte counts are a subset of Source metadata.
  Plan+stage counts are a subset of Conversation metadata. Do not infer model
  requests, successful generation, visible turns or feature activation from them.
- Complete requires all eight storage kinds, six domains and three notebook
  kinds present, all byte aggregates known, nonnil observed identities, no issues,
  supported current format, matching complete/observed total and device-inode
  custody. Partial requires at least one explicit issue and no complete total.
- Unsupported/busy/unavailable never become healthy empty categories. An absent
  kind in an incomplete map is not zero. A complete legacy-format v3 result may
  show zero notebook records without claiming notebook feature activation.
- A schema3 notebook record under legacy format1/2/3 is invalid, even though the
  record kind is known. Retain its physical file observation as unclassified,
  with incomplete semantic accounting; do not silently grant generation4 support.


# Protected content boundary

Bounded owned envelope/manifest metadata is read and hashed/decoded for structure.
Legacy inline Source2, Writer stages or feedback metadata can contain protected
text; do not describe those reads as text-free. No text/content is emitted in the
report, forwarded to a model/provider or used to infer semantic quality. Archived
source/media object payloads, original documents, credentials roots and native
files are not read. Apparent media lengths and reference coverage are metadata
observations; media_content_verified remains false.


Unreferenced/unclassifiable owned objects stay in the unclassified-object physical
bucket with unclassified-object issue/partial semantic accounting; the observer
must not read arbitrary object payloads looking for a category. Complete also
requires zero missing/uninspected/size-mismatched/omitted reference counters. If no
current/retained supported generation4 was observed in a complete scan, all three
notebook-kind counters must be zero. Those relations are producer/host admission
checks, not conclusions drawn from a successful JSON parse.

The fixed consumer sends no private argv and discards stderr. Rejection of
incompatible global CLI flags is before effects; existing arbitrary/manual argv
parser diagnostics are not newly promised to be universally secret-redacted.


Counter lexical validation uses whole-string/full-match or an absolute end
condition. A dollar anchor alone may accept a final newline and is insufficient.
Reject trailing LF/CRLF/space and every other extra scalar code point. Per-media
descriptors remain bounded by the producer's actual MAX_MEDIA=268435456bytes;
MAX_ITEMS=4096bounds declared reference sets. Huge arithmetic test values belong
to opaque file buckets and are not valid enormous media-descriptor fixtures or
reachable-filesystem evidence. Aggregate overflow requires multiple individually
valid lengths; one u64file length alone cannot overflow u64.
