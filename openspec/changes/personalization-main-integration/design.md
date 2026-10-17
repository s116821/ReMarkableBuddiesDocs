# Design

Use the existing `feat/rem-53-personalization-config` and
`docs/rem-53-personalization-config` branches. Record current main as a merge
parent, preserving the previous stacked commits, and keep the resulting diff
limited to personalization and its shared storage prerequisite. Other branches
and their unfinished work remain untouched. Retain main's CI, lockfiles, SDK
dependency and application source outside this scope.

Add an existing-store-only constructor alongside normal `Store::open`. It takes
the same stable OS lease once, validates the existing identity, auxiliary owner
markers and generation structure before maintenance writes, and refuses missing,
unsupported or busy stores without creating a replacement. Keep the lease until
the command's write and exact readback finish. Release it on every refusal as well
as normal Store destruction. Reuse normal recovery and `Store::replace_config`;
do not add another writer or depend on subject-memory configuration.

Personalization maps structured Store refusals to its existing version1 status
values. Normal startup remains able to initialize a new owned store. The new
maintenance constructor never initializes one. Existing same-user hostile-write
and power-loss limits remain; this is not a new native or hardware guarantee.

Integrate only personalization CLI dispatch before dotenv and normal startup.
Do not advertise the unmerged memory/history maintenance flags. Preserve their
historical specification in the old archive, and explicitly reconcile the current
platform-runtime contract with the smaller actual-main delivery.

Verification uses real temporary filesystem stores and the actual host CLI,
including incomplete ownership/generation, a competing lease, unchanged rejected
configuration and exact multiline Unicode. Preserve the already accepted format,
snapshot and revision tests. Run focused changed-path tests, formatter and strict
lint; normal hosted CI supplies supported target build/integration checks.
