# Export an ordinary owned archive through a bounded producer

## Why and source facts
Actual source8c90edabf2c30f6c20e2c2df6b0e34c2df1af9e7 provides Store::export (format1), but the maintenance archive CLI exposes only inspect/export-selected (format2). The delivered ordinary restore intentionally accepts only format1. Provide an explicit guarded export entry paired with that ordinary restore without inventing selected restore activation.

## Scope
Prepare/apply/status for a new destination outside all owned roots, existing ordinary unconfigured/local-only Store only, same legacy export copy/backup.json writer with original config/path/actor/mode/generation/full-history/snapshot/destination conditions. Preserve source and any partial destination; verify complete exact archive bytes and closure. No paths/configuration values/credential references appear in reports. No initialization, source cleanup, selected activation, new device, provider/runtime/service or tablet action.

Main owns this independent producer; the basic companion retains its existing owner. Docs base99fa30467bbe082ce60e60546216afef7c9094aa preserves prior deliveries. Concrete review precedes source edits; one linked Docs/source delivery includes tests, independent review, sync/archive and separate actual-main/publication observations. This precode is unimplemented. Future consumer UI and physical qualification remain separate.
