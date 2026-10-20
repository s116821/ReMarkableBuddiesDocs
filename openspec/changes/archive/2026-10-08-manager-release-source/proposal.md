# Manager release-source preview (REM-41/42/54)

## Why
Manager main (555421ce) only displays the REM-21 foundation. October 8 REM-41/42
requires persistent source policy and official stable discovery while open.
Actual signed APK, wired transport and package ownership qualification are absent.
Implement the independently useful read-only preview without representing metadata
as a qualified install, reopening REM-46, or waiting for public catalog acceptance.

## What Changes
- Shared Angular/browser/Electron official GitHub stable metadata refresh and polling.
- Separate installed unknown, official candidate, qualified availability unavailable,
  and community unlisted state. Persist policy; preserve an unavailable saved policy.
- Fail-closed eligibility with explicit missing verified package/device constraints.
- REM-54 supported Tailwind integration and shared responsive shell conventions.
- Focused metadata/fault/promotion/persistence and real shared-host rendering checks.

## Capabilities
### New Capabilities
- `manager-release-source`: read-only stable discovery and source preference.

## Impact
Docs base 8008389f; Manager base 555421ce. No release workflow, installer, package
producer, tablet transport, Buddy API or native operation changes. REM-41/42/54
remain unfinished; REM-35 owns 1.0 and REM-55 owns delayed catalog inclusion.
Deliver paired Docs/Manager revisions; do not independently close a planning PR.

Source basis: complete REM-41/42/35/46/54/55 descriptions and timestamped comments,
current repositories, Mem handoff v35 final 0093 closeout and October 8 prior art.
Current chat 99-percent checkpoint policy supersedes older issue reserve text.
