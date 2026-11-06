# Portable preference export and offline inspection

## Why
REM-52 requires an explicit portable configuration allowlist, including REM-53's personalization preference, while excluding device/runtime/account bindings. Selected archives currently exclude configuration; ordinary notebook snapshots preserve full local review configuration. Neither is an allowlisted portable preference artifact.

## What Changes
Add explicit read-only CLI export from an existing saved configuration and offline inspection of a complete version1 portable artifact. Reuse strict saved configuration parsing and existing preference schemas. V1 includes only product_settings, personalization and research_policy declarations. No automatic import, archive format change, cloud/native operation or runtime activation follows. Existing snapshots/archives retain their original contracts and exclusions. Broader portable model/memory preferences and sync integration remain unfinished.
