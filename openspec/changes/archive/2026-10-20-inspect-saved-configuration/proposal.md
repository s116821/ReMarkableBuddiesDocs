# Inspect saved configuration

## Why
Manager can inspect saved storage mode and use the dedicated personalization editor, but has no bounded general view of the saved versioned configuration. A saved file must not be mistaken for effective runtime/provider state or serialized wholesale into a renderer.

## Scope
Add one read-only producer command and a strictly reduced snapshot, then consume it in the shared browser/Electron UI through existing fixed wired host adapters. Main owns producer and central contract; SCRAPPY owns consumer; Root independently reviews the concrete contract before dependent implementation. This is one linked delivery, not a completed planning prerequisite.

No settings mutation, credentials management, effective environment resolution, provider validation, Store admission, mode activation, service control or device qualification is included. Unsupported roadmap settings remain explicit gaps. Existing personalization and saved-mode interfaces remain their owners.

## Source basis
Current REM42 requirements and October20 owner discussion; immutable Buddy b34e6d5cb772b13a833c2830e6770a8b98cf5330 src/config.rs, src/config/personalization.rs, src/main.rs, src/storage/files.rs and src/memory/mod.rs; current central canonical contracts. See design for external management-plane references. Proposed wire and acceptance below are design decisions, not implemented claims.
