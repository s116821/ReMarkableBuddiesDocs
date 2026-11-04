# Ordinary Writer preference precedence

## Why

The ordinary Writer already receives a saved immutable personalization
snapshot. Its prompt labels the text as optional but leaves precedence over a
conflicting current request implicit. Make that priority explicit at the
receiving draft command.

## What changes

- State the precedence of current requests and fixed task/source-safety
  instructions in the optional preference part of ordinary Writer prompts.
- Verify generation and refinement against the real Ledger with captured
  local engine inputs. Preserve the disabled/empty payload and history bytes.

## Capabilities

### Modified Capabilities

- `writer-drafts` defines precedence for the existing ordinary receiving path.

## Impact

Buddy's ordinary draft receiver, including Writer flow when it delegates to
that receiver. Frozen notebook plans, configuration reload or synchronization,
native/preset routing and model semantics are separate work.
