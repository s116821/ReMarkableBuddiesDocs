## MODIFIED Requirements

### Requirement: Verified-layout navigation readiness
On the verified RM2 layout, navigation SHALL resolve the requested adjacent native
page from validated current page order before one swipe, then establish fresh
bracketed target identity and positive settled-chrome evidence within a monotonic
deadline under input guards. It SHALL preserve downstream eligibility and strict
source-content guards, never refresh an active baseline or repeat a timed-out
swipe. Unsupported ordinary layouts SHALL refuse before emission.

#### Scenario: Metadata and pixels arrive separately
- **WHEN** metadata points at the target before its pixels arrive, or target pixels arrive before metadata
- **THEN** neither alone completes navigation; fresh correlated owner/order, positive chrome, distinguishable target content and matching observations are required, with late observations rejected.

#### Scenario: Inserted notes or page boundary
- **WHEN** the requested neighbor is an inserted notes page or no neighbor exists
- **THEN** native page order determines the neighbor regardless of PDF redirect index; a known boundary issues no swipe.

#### Scenario: Identical-looking pages or occupied gutter
- **WHEN** source and target cannot be visually distinguished, or legitimate gutter ink prevents the conservative chrome predicate
- **THEN** completion refuses safely at its bound without ignoring content, repeating input or claiming successful navigation; an inked question source to a blank successor remains a distinct positive case.

#### Scenario: Ownership or order changes
- **WHEN** a wrong neighbor/session/visit, page-order/redirect mutation or external input occurs
- **THEN** navigation cancels before further input or classification, with no stale success or unsafe repeated swipe.

## ADDED Requirements

### Requirement: Guarded ordinary portrait gesture consumption
The ordinary Reader SHALL consume the pinned SDK plan for the explicitly
admitted RM2 portrait direction. The Reader SHALL retain the existing
request/input guards and bounded destination observation. It SHALL require
stable portrait configuration and recognized source chrome before emission,
refuse unsupported input and unverified fallback, and attempt one release
after an ordinary emission error.

#### Scenario: Unsupported or drifting configuration
- **WHEN** the source model, portrait configuration or chrome is unsupported, or the configuration changes during destination observation
- **THEN** the Reader SHALL refuse before emission for invalid source inputs, or refuse settlement and replay after one admitted gesture.

#### Scenario: Explicit diagnostic configuration
- **WHEN** the hardware diagnostic requests a Next, Previous or round-trip gesture
- **THEN** it SHALL validate explicit portrait before opening the input device.
