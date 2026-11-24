## Source identity and lifetime

The installed Reader owns one bounded, in-memory entry. Before considering it, Reader performs normal input arbitration, admits the current original page and checks the full contents of the original PDF. Match the document ID, PDF format, original content digest, page count and extractor revision. Validate the normalized material against its previously verified complete index key. A changed document or incompatible entry takes the cold extraction path. A failed source admission ends the request.

Keep derived text opaque to the resident service where the existing worker owns parsing. Keep each worker's resource limits and request lifetime. Oversize documents that satisfy normal source limits still work and simply skip retention. The entry holds no questions, answers, previous search results, credentials or session handles. Its lifetime ends with eviction or the service process.

## One question at a time

Reuse applies only to preparing the source. Each verified handwritten question searches the entire admitted source again, under its own deadline and evidence budget. Keep the current document, page order, conversation and file checks at provider and publication boundaries. A queued Writer action and an inserted notebook page keep their existing paths.
