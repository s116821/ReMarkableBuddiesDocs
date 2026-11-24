## Source identity and lifetime

The installed Reader owns one bounded, in-memory entry. Pin the PDF and page-table file identities across native capture using metadata. After Writer arbitration selects Reader, read the current page table and original PDF. Check the capture's verified page and order, re-read both complete files and compare both digests within the original acquisition allowance. Only then consider a cache hit. Match the document ID, PDF format, original content digest, page count and extractor revision. Validate the normalized material against its previously verified complete index key. A changed document or incompatible entry takes the cold extraction path. A failed source admission ends the request.

Keep derived text opaque to the resident service. Start a fresh worker for each request, with its own ID, expiry and existing resource limits. It accepts one exact query and exits. Oversize documents that satisfy normal source limits still work and simply skip retention. Only verified normalized material and its source identity survive the request. Nothing is written to disk or synchronized for this cache. Its lifetime ends with eviction or the service process.

## One question at a time

Reuse applies only to preparing the source. Each verified handwritten question searches the entire admitted source again, under its own deadline and evidence budget. Keep the current document, page order, conversation and file checks at provider and publication boundaries. A queued Writer action and an inserted notebook page keep their existing paths.
