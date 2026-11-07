# Conditional portable preference import

## Purpose

Explicit private saved-preference import using the unchanged version1 artifact. See the [wire contract](../../changes/archive/2026-11-06-import-portable-configuration/contract.md). Runtime activation and broader archive/cloud/native integration remain separate.

## Requirements

### Requirement: Explicit conditional present-declaration import
The backend SHALL expose a separate explicit private inspect/prepare/apply/status protocol for the existing version1 portable preference artifact, preserving its closed three-setting schema. It SHALL overlay only present allowed declarations, preserve omitted destination members and unrelated raw values, retain supported null as a declaration rather than deletion, and validate the whole original/artifact/result without materializing defaults. It SHALL bind changed Apply to the exact original Config/path/artifact/target and refuse substitution or rebase. Existing export/offline inspection behavior SHALL remain unchanged.

#### Scenario: Sparse private preferences
- **WHEN** a valid artifact contains only selected preference declarations
- **THEN** Prepare describes only actual allowed changes without text disclosure, and admitted Apply publishes that exact overlay while retaining omitted/excluded destination declarations and original text contents.

#### Scenario: Empty or identical overlay
- **WHEN** the overlay leaves the complete raw destination value unchanged
- **THEN** Prepare returns no-change without rewriting bytes, creating an intent or opening a Store.

#### Scenario: Changed or invalid original inputs
- **WHEN** any whole-input validation, original Config/path/artifact/target correspondence or inclusive byte bound fails
- **THEN** the invocation refuses with a bounded sanitized report rather than dropping fields, accepting a prefix, resetting omitted state or publishing a substituted target.

### Requirement: Scoped existing custody and truthful uncertainty
Changed Apply SHALL use the existing raw conditional publisher and original consuming Store/mode custody for legacy1 or complete owned ordinary notebook4 in absent/LocalOnly mode only. It SHALL refuse selected/feedback families and unsupported notebook state without initialization/adoption/repair, enforce canonical Config/root separation, and preserve other maintenance admissions and owned records/media. Publication/output uncertainty SHALL retain the original unknown without replay/rollback/another frame. Status SHALL observe exact desired full bytes under the original path without artifact/Store/provider access or historical-authority claims. All operations SHALL report runtime activation unverified.

#### Scenario: Ready destination and original intent
- **WHEN** supported existing custody and every original change condition still match
- **THEN** only the exact saved Config target may change through the existing publisher, with actual ownership retained through write_all success or error and no flush requirement.

#### Scenario: Busy or unsupported destination
- **WHEN** ownership, family, notebook readiness/history/mode or canonical separation is busy, unavailable, corrupt or unsupported
- **THEN** existing refusal categories apply without data/config repair, fallback or credential/provider/native action.

#### Scenario: Uncertain publication or incomplete output
- **WHEN** publication or output may have occurred without a complete verified result
- **THEN** no automatic retry or rollback occurs, and later original-intent Status supplies only current-byte observation without settling historical uncertainty or granting running/native authority.
