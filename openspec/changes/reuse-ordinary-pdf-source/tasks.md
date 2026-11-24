## Implementation

- [ ] Reuse a bounded, verified original PDF source across separate ordinary Reader requests. Keep source admission and one exact lookup per question.
- [ ] Replace or discard a mismatched entry and retain the cold path for otherwise eligible documents larger than the cache limit.

## Verification

- [ ] In the existing pipeline, send two different questions to one running Reader. Verify one PDF extraction, two fresh retrievals and citations to the different passages.
- [ ] Verify a fresh extraction after changing the same document's bytes and after starting a new service. An otherwise supported PDF above the retention limit must answer both questions by cold extraction.
- [ ] Exercise file or page-order changes on a warm request. Keep the existing Writer-priority and inserted-note cases passing.
- [ ] Include a second question about the same original PDF in the signed Buddy service check already tracked under `answer-from-ordinary-installed-pdf`.
