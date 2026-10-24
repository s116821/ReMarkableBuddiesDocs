# Corpus-aware lexical passage ranking

## Why

The normalized Index currently counts distinct shared terms. Equal overlap always
prefers earlier material, even when later material concentrates on the question's
distinctive term. Frequency, corpus rarity and passage length cannot affect rank.
REM-4 calls for useful ranked retrieval under bounded context budgets.

## What changes

Use a fixed, fully specified local BM25 scorer in the existing Index query path.
Retain existing input/tokenization/chunking, public API, source identity, fresh
full-index queries, provenance, neighbor ordering and complete-result budgets.
Demonstrate authored relevance contrasts against the old overlap order and retain
ordinary extraction/cache/receiving regressions. Correct the retrieval guide's
stale unfinished wording for already-delivered historical evidence/inheritance.

## Scope and limits

This is lexical ranking over already-normalized text, not embeddings, semantic
search, verification, confidence or a model-quality evaluation. No dependency,
SDK, runtime, source admission, configuration, provider/network request, tablet,
service, model credential, Manager or CI graph changes. Held work stays held.
Implementation, qualification and paired delivery remain unfinished.
