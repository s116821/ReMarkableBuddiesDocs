# Design

## Context
Manager main v0.2.2 already pins Angular 22.2.0 and Tailwind/PostCSS 4.3.3 with a lockfile, uses the official PostCSS plugin, and loads the same Angular output in both hosts. Keep that upstream integration; no replacement compiler or platform stylesheet.

## Decisions
Use CSS-first `@theme` semantic tokens for surface, ink, muted, border, brand, warning, danger and focus. Literal utility classes handle layout and typography. A small `@layer components` set handles reusable panels, primary/secondary controls, fields and visible status; avoid bare header/section/aside component selectors that leak into future screens. Base rules retain document typography and keyboard focus.

Preserve release behavior and semantics. Disabled install remains disabled; no live device connection appears. Reuse actual release checking/error transitions to validate states. Avoid dynamic utility construction, host CSS branches, custom Tailwind plugins and redundant dependency upgrades. Add an explicit Angular development configuration and check its browser output separately from production/packaged output.

## Verification and risks
Tailwind source scanning and production pruning can leave template class strings without CSS; assert computed styles in actual rendered development and production browser pages and the packaged Electron renderer. Check narrow/wide layout, contrast, keyboard focus, error and disabled states with deterministic release fixtures, no live network calls. Capture representative views for review. Linux package evidence is distinct from Main's required Windows verification and native tablet qualification. Keep Windows and independent final review gates open until observed.

## Sources
- https://tailwindcss.com/docs/installation/framework-guides/angular
- https://angular.dev/guide/tailwind
- Public issue requirement: use Tailwind consistently throughout shared Angular shell/screens; preserve responsive accessibility and document conventions.
