# Ordinary SDK gesture consumer integration

Buddy `608b00b80c72d4e5fefa80f961e970cd0b938fc9` starts at delivered
`4eeaabef92245173ff136e9773c0416de2653466`. Docs starts at delivered
`68ac03324a63cd25af69565e099874eefcfc25e7`.
The exact six-file extraction comes from [Buddy 40](https://github.com/s116821/ReMarkableBuddies/pull/40)
`0e4431ff` and [Docs 29](https://github.com/s116821/ReMarkableBuddiesDocs/pull/29)
`4f5210a`. Five consumer files match that source. The sixth, the hardware
example, checks the portrait argument before constructing Touch in both
single-direction branches, matching the round-trip branch.

The current SDK pin stays `80b29ebec3a46b6976e5288d2e8d65fbeccca816`. Its
gesture implementation differs from the historical planner only by three
provenance and license comment lines. The production Reader retains
cancellation, input and completion guards. The guarded navigation path
refuses unsupported layouts instead of emitting the old fallback swipe.

Windows locked offline tests with one Cargo job passed 60 controls. These
included three fake emitter tests, nine composite navigation/request-guard
tests, five document metadata tests, and 43 offline simulator cases. The
test build reported six existing Windows Writer fixture warnings.

The existing Linux diagnostic fixture constructs Touch with no device and
uses an in-memory batch sink. Its unused emitter panics if reached. Linux
execution of that fixture and compilation of the Linux diagnostic body
belong to exact hosted checks. The Windows hardware example check passed with
all features and covers the non-Linux stub. The example was never executed.

The adapter under Buddy 48 and its adapted copy in Buddy 40 retain their
separate custody. The ordinary mode and data fences and startup failure
contract are unchanged. Current native completion, crash release, active-page
authority, other profiles and the broader Reader lifecycle remain separately
owned.
