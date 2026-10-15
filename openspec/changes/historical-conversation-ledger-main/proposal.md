# Change: Deliver the historical conversation ledger library on main

## Why
The shared Store ships independently of its conversation domain. Accepted historical implementation 18e1a741 contains a coherent persistence library and regressions that can be delivered without activating the larger unfinished Reader, selected-branch or native stack.

## What Changes
Add schema-one conversation, turn, source-image, historical capture, binding-receipt and export-association APIs over the existing Store. Preserve exact text, image bytes, chronology, correction links, atomic publication and explicit context refusal. Add three bounded/read-only Store inspection helpers and consume an exact accepted SDK revision with default features disabled and mock enabled only for tests.

## Impact
Library callers gain durable historical records; the installed Reader remains unchanged. This does not complete REM-37, integrate provider history, enable Writer, implement selected causal views or authorize native actions. Existing active durable-conversation-context and other stacked changes remain unfinished and preserved. Source basis: current public roadmap/contracts, full REM-37 description and all 48 accessible chronological comments reviewed October 15, accepted source 18e1a741, and current SDK author compatibility confirmation. Material requirements are published here; private tools are unnecessary to review or test this scope.
