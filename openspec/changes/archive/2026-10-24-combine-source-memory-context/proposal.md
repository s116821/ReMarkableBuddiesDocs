# Combine historical source and optional memory context

## Why

The ordinary source receiver freezes exact request/history/source passages, while
the offline memory Provider separately returns labeled associative facts. There is
no bounded data assembly boundary that derives memory scope from that captured
request and accounts for both layers together. Callers should not reconstruct or
rewrite the source frame to add optional memory.

## Scope

Add a read-only consuming attachment API on FrozenRequestContext. Keep the original
frame unchanged and nest it in a new historical wrapper with optional typed memory
query identity, status, diagnostics and context. Derive query text/document from
the frozen request/source, validate returned ordinary data and bound complete
encoding and caller-counted tokens. Preserve existing source/evidence APIs.

This is neither model integration nor a durable schema change. Existing held
Reader/memory/runtime work, live-model gates, selected admission, configuration,
research, Writer and Manager contracts remain separately unfinished.

## Delivery

One coordinated Rust/Docs delivery, with independent precode and implementation
reviews, exact tests/CI, canonical sync and archive of this increment only. Real
temporary Store/Index/LocalMemory fixtures suffice for this data-only change;
no model/device/provider network or service operation is needed.
