# owned-data-inspection

## Purpose

Define bounded read-only inspection of existing Buddy-owned storage and its CLI report, without runtime or native authority.

## Requirements

### Requirement: Nonmutating owned-data inspection
Inspection SHALL read only validated existing Buddy-owned paths and current supported
ownership/formats through the file/CLI contract. It SHALL NOT initialize, recover,
clean, chmod or write the Store, create a lease file, resolve provider credentials,
contact a provider, start a runtime/device, stop a service or access native documents.
An existing read-only nonblocking OS lease SHALL distinguish busy writers without
changing stored bytes. Missing/unsupported/changed ownership or current generation
SHALL be explicit rather than treated as an empty Store.

#### Scenario: Missing store or concurrent writer
- **WHEN** the selected Store does not exist or its existing stable lease is owned by a writer
- **THEN** inspection returns unavailable or busy, creates nothing, leaves every existing file unchanged and reports no fabricated zero category or native readiness.

#### Scenario: Unsupported or changed input
- **WHEN** owner/format/path checks fail, selected schema is unsupported or identity/CURRENT changes during inspection
- **THEN** inspection defers with an explicit unsupported/partial issue and does not repair, initialize, follow reparse paths or claim a consistent complete snapshot.

### Requirement: Honest bounded category and shared-byte accounting
The versioned report SHALL distinguish owned conversation/source/export/memory/handwriting metadata, present referenced media, cache and retained/structural storage, and SHALL separately account the unassociated-feedback domain in report2 when a feedback marker, format3 or new-domain state is observed. It SHALL charge each known stored file once per generation/path and distinguish additive apparent file lengths from nonadditive namespace media references. Missing/omitted/shared/unknown resources and bounded incomplete scans SHALL be reported explicitly; no allocated/reclaimable space, logical liveness, media integrity, display state or native-page health SHALL be inferred from file presence or sizes. Source: existing accounting contract and the new independent retention domain.

#### Scenario: Shared content and retained generations
- **WHEN** multiple namespaces or retained revisions reference the same stored media object, or another generation contains identical content
- **THEN** one physical file is charged once, namespace references remain labeled nonadditive, another generation's file is counted separately and no cleanup permission follows.

#### Scenario: Missing media or bounded partial inspection
- **WHEN** a required object is absent, media is deliberately omitted, metadata cannot be classified or an entry/JSON bound is exceeded
- **THEN** the report preserves observed accounting and explicit missing/partial status, leaves complete totals absent and never substitutes a zero or a retained logical association.

#### Scenario: New feature accounting
- **WHEN** supported feature3 and its structural/observation files are inspected
- **THEN** report2 accounts the sixth domain and structural files within real bounds, while malformed/foreign/incomplete features cannot produce a complete total.

### Requirement: Inspection-only CLI admission
The CLI SHALL emit unchanged report_version1 JSON for supported legacy1/2 state and report_version2 for observed feedback3/new-domain state, through a route before normal Store, provider, sync, Workflow or device startup. Report2 SHALL retain all prior disclosure restrictions and add bounded current_generation_format (null or1/2/3) and sorted unique retained_generation_formats (supported observed noncurrent formats1/2/3) evidence, with unknown formats explicitly incomplete without runtime authority. The route SHALL reject incompatible execution flags, avoid secret/metadata-content echo and preserve the normal Reader interface outside inspection. Report emission SHALL NOT imply installed Manager integration or a healthy/qualified native runtime. Source: original inspection-only route and explicit versioned feature support.

#### Scenario: Inspect without model credentials
- **WHEN** a caller selects a valid existing nonsecret configuration and requests owned-data inspection without provider credentials
- **THEN** the real CLI produces the report without provider/device initialization or Store changes and does not disclose a protected sentinel value.

#### Scenario: Legacy and feature report separation
- **WHEN** an unchanged legacy layout or supported feature3 layout is inspected
- **THEN** legacy report1 shape/domain restrictions remain intact and feature report2 is explicit; unknown/invalid feature state is partial/unsupported rather than a fabricated empty category.
