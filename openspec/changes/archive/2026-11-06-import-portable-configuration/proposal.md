# Why

The backend exports and validates a strict version1 portable preference artifact but cannot apply it to another existing saved configuration. Manual JSON editing bypasses conditional publication and gives no truthful original-intent reconciliation.

# What Changes

Add an explicit private inspect/prepare/apply/status import protocol for the existing product_settings, personalization and research_policy declarations. Apply only present declarations, preserve omissions and unrelated destination values, and reuse the existing conditional Config publisher and consuming custody. Keep the exported artifact and existing selectors unchanged. Specify exact destination/artifact binding, supported storage families and failure outcomes before implementation.

# Scope

This is local saved-preference maintenance only. It excludes reset/clear-all, new portable domains, archive integration, cross-actor storage restore, cloud authentication/synchronization, Manager UI, credential maintenance, provider calls, service reload and native effects. It requires one coordinated implementation/spec delivery with qualification, canonical sync and archival; this proposal alone is not delivery.
