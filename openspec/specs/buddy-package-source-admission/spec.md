# Buddy package source admission

## Purpose

Bind the existing package producer to actual reviewed source and consumed SDK
identity without treating dependency metadata as a qualified package or install.

## Requirements

### Requirement: Requested SDK tag identity uses independent release source
The producer SHALL pair an explicit SDK tag with an explicit independent SDK
release-source checkout. That source SHALL be a clean full standalone canonical
Git repository with the real requested tag object and peeled commit, matching
Cargo's resolved SDK commit and exact tracked manifest bytes. Admission SHALL
match the local object and peel to two stable bounded canonical remote
observations, refusing effective URL rewrites. The verifier SHALL NOT synthesize
tags, fetch into the Cargo checkout, write cache refs/configuration or substitute
an alternative source after refusal.

#### Scenario: Cargo-generated checkout has no tag refs
- **WHEN** the actual clean Cargo SDK checkout has the expected commit/manifest but no tag refs
- **THEN** a separately supplied qualified release checkout may establish requested tag identity
- **AND** Cargo checkout and completion-marker checks remain independent.

#### Scenario: Missing or invalid independent proof
- **WHEN** the tag/source option pair is incomplete or the source is dirty, shallow, redirected, replaced, missing the real tag, or disagrees on origin, commit or manifest
- **THEN** admission refuses rather than altering the cache or accepting guessed tag identity.

#### Scenario: Tag object or canonical observation changes
- **WHEN** the annotation, peel, source identity or canonical remote observation changes during proof
- **THEN** admission refuses even if an annotation replacement still peels to the same commit.

### Requirement: Source proof remains bound to the existing package operation
The producer SHALL bind the actual SDK tag object into normalized dependency
identity and retain the independent source proof privately. Existing pre/post
build, cross-target and final-output checks SHALL refuse changing proof. Public
signed metadata and installation eligibility SHALL NOT be widened by this proof.
Neither SDK source proof nor Cargo metadata alone SHALL claim compiler/runtime,
artifact/signature, reproducibility or device-lifecycle qualification.

#### Scenario: Requested proof cannot be established
- **WHEN** a requested tag proof is missing or refuses
- **THEN** the operation refuses without silently downgrading to commit-only identity.

#### Scenario: Explicit commit-only observation
- **WHEN** neither SDK tag nor independent tag source is requested
- **THEN** the existing commit-pinned observation remains explicitly tag=null and retains existing eligibility restrictions.

#### Scenario: Proof changes across operation boundaries
- **WHEN** the independent proof differs before/after build, across the two targets or before final output
- **THEN** the producer refuses completion without changing the public metadata schema or claiming rollback of prior effects.

### Requirement: Build and final output roots are disjoint
The producer SHALL refuse equal or nested resolved build/final output roots
before source/tool admission or output creation. Existing fresh external-root
and exact-input requirements SHALL remain in force.

#### Scenario: Equal or nested output roots
- **WHEN** build equals final output, build contains final output, or final output contains build
- **THEN** the producer refuses before source/tool calls or creating either output.

#### Scenario: Fresh sibling roots
- **WHEN** build and final output are fresh disjoint external siblings
- **THEN** ordinary exact-source and tool admission proceeds without waiving other checks.
