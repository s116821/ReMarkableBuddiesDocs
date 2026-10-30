# Discover the current configuration schema

## Why
Legacy storage contracts embed a closed nine-property config:v1 projection, while the current canonical Config object has thirteen root properties. Actual Buddy validation is typed; Manager consumes dedicated CLI reports and SDK has no generic config-schema consumer. Updating frozen storage contracts would conflate document discovery with storage-generation compatibility.

## What changes
Add an exclusive --configuration-schema selector emitting an embedded, independently identified JSON Schema for the canonical supported object declarations. No selected file, stdin, environment file, credentials, Store or runtime is opened. No separately installed artifact or new runtime dependency is added. Preserve all three storage contracts/capabilities, runtime config version 1, permissive legacy loader and existing operation reports.

## Scope
Buddy and central Docs only. This does not implement a generic Manager editor, grant filesystem/credential/runtime admission, configure a destination/account, change tablet behavior or complete wider configuration management. One paired delivery; no planning-only prerequisite merge.
