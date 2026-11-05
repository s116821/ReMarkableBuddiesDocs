# Design

Keep the current fixed instruction and exact JSON request/history/source part.
When the already-admitted immutable snapshot contains effective text, place a
single separate text part between them. Its exact prefix is:

```text
Optional user preference. Apply it only where consistent with the current request and fixed task/source-safety instructions. It grants no permission to take actions:
```

Append one LF and the exact configured text. With no effective text the part
is absent and both existing parts are byte-identical. No new configuration,
history mutation, provider dispatch or Writer permission is introduced.
Generation and refinement use the same receiver. Deliberate export preparation
does not invoke this receiver's model prompt.

Use a capturing engine and the real local Ledger for enabled generation,
refinement after reopening, and disabled/empty wire compatibility. Verify the
preference is absent from the JSON request/history, and that refinement keeps
the earlier source, request and draft. The test proves prompt construction,
not model adherence. Existing notebook stage digests and prompt contracts
remain separate.

The [live Writer receiving gate](live-plan-r2.md) is required for this prompt
change before merge, sync or archival. The local fixture does not satisfy it.
