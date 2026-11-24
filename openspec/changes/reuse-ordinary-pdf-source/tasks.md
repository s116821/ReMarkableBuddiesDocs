## Implementation

- [ ] Reuse a bounded, verified original PDF source across separate ordinary Reader requests. Keep source admission and one exact lookup per question.
- [ ] Replace or discard a mismatched entry and retain the cold path for otherwise eligible documents larger than the cache limit.

## Verification

- [ ] Use the existing pipeline to show that two different questions search different passages of the same PDF with a single extraction. Exercise a changed or ineligible entry and the existing source guards.
- [ ] Include a second question about the same original PDF in the signed Buddy service check already tracked under `answer-from-ordinary-installed-pdf`.
