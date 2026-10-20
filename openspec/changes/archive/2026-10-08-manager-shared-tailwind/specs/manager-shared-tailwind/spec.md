## ADDED Requirements

### Requirement: Supported shared Tailwind integration
The Manager SHALL generate Tailwind styles using the supported Angular PostCSS integration with pinned, locked dependencies, one shared theme and reusable styling conventions for browser and Electron. Application versions SHALL remain derived from Git tags/build metadata.

#### Scenario: Development and production builds
- **WHEN** a contributor builds or serves development and builds production with the documented commands
- **THEN** the shared template utilities and semantic theme styles are generated without host-specific CSS or a custom styling compiler

### Requirement: Consistent accessible shared components
The shell and current release-preview components SHALL use shared theme/layout/control/status conventions and preserve readable contrast, responsive layout, keyboard navigation and visible focus/error/disabled states without altering release discovery or enabling installation.

#### Scenario: Narrow viewport and keyboard use
- **WHEN** browser or packaged Electron renders the shared UI at a narrow or wide viewport and a user navigates controls by keyboard
- **THEN** content remains readable without horizontal overflow, focus is visible with display-DPR quantization accounted for, and unavailable controls remain disabled

#### Scenario: Release check or failure
- **WHEN** the existing release controller is checking or encounters a release/preference error
- **THEN** the shared UI visibly distinguishes pending, disabled and error states while retaining existing source preference and installation gates

### Requirement: Public conventions and bounded verification
The Manager SHALL document its upstream integration, tokens, reusable conventions and checks under docs, and record actual development/production browser and native-host packaged Electron evidence independently of tablet qualification.

#### Scenario: Contribution and delivery
- **WHEN** a contributor adds a shared screen or reviews the linked delivery
- **THEN** public docs describe literal utility usage and accessibility checks, and checks intercept the initial release request before UI startup and reject unexpected external requests, and evidence identifies tested host/platforms without claiming unobserved Windows, native tablet or installation support
