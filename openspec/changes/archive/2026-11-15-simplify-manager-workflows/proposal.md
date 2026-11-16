# Simplify Manager workflows

## Why

Manager currently exposes successive implementation slices as a long page of
configuration editors, inventories and archive variants. The maintainer asked
for a full requirements audit and substantial UX cleanup. The requested product
is a companion for managing a tablet, its preferences and Buddy-owned data.
Protocol steps and internal storage generations are not separate user tasks.

## What changes

- Replace the flat dashboard with Tablet, Settings, Data, and Backup & sync
  destinations, plus secondary Troubleshooting.
- Group related controls into contextual workflows; remove obsolete preview
  marketing, duplicate summaries and idle operation controls.
- Keep configuration origins, private inputs, confirmation, cancellation and
  uncertain outcomes correct while using ordinary user-facing language.
- Preserve requested capabilities and browser/Electron parity. Do not claim
  unfinished installation, tablet provisioning or backup functionality works.

## Impact

Manager renderer and UI checks; central Manager UX requirements and guidance.
No new provider, dependency, tablet operation or Buddy administration API.
Open feature branches must adopt the navigation before their later delivery.
