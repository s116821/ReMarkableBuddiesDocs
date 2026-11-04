# Design

## Layout

Use `docs/examples/` for examples, `cicd/release/` and `cicd/deploy/` for the
corresponding inputs, and `scripts/` for helper programs. GitHub discovery files
remain in `.github/`; conventional root manifests and build entry points remain
where their tools expect them. Explicit Cargo example declarations preserve
example names after relocation. Documentation exclusions must not hide executable
examples or fixtures from CI or semantic change classification.

## Upstream tooling

Use the distributed `svenstaro/upload-release-action` at the already selected
immutable upstream revision. Its repository includes the distributed entrypoint;
the project no longer selects its dependency closure, rebuilds it, transfers it
between jobs or runs loopback tests of its implementation. Keep explicit draft,
exact release ID and no-overwrite options, followed by application-owned checks
of release identity and uploaded bytes. Historical dependency/audit failures stay
historical; direct use does not assert that those audits now pass.

Keep maintained semantic selection, path filtering, title checks and GitHub
artifact Actions. Plain workflow commands replace wrappers that only invoke
build/package/extraction commands. Small reusable application-specific functions
may remain scripts when they are substantive and need meaningful tests; moving
a testable packaging implementation wholesale into YAML is not a simplification.

## Preserved guarantees

Preserve Git-tag version authority, checks/build/integration/release ordering,
the exact tested source and bytes, complete artifact inventory, ABI and embedded
identity checks, same-ID partial-release recovery and the 1.0 admission gate.
Documentation-only changes do not build or release applications. Public fork and
manual contributor paths remain supported. No repository-setting mutation is
part of this change.

## Delivery and in-flight work

Use independent cleanup branches, leaving dirty product work and frozen native
inputs intact. Review and validate the cleanup, sync this specification and
archive the completed lifecycle in the same Docs PR. Merge component cleanup
with its coordinated Docs delivery, then merge current main into owned open PR
branches (or have their owner do so), preserving stack bases and feature edits.
Resolve semantic path changes rather than copying old workflow files back.

Audit every remaining PR against current main and its actual dependency base:
identify unique unmerged behavior, equivalent landed changes, required evidence,
blockers, owner and next action. An old Draft is neither evidence of incompleteness
nor permission to discard work. The audit is tracked in the project issue, not a
second mutable status file in the source tree.
