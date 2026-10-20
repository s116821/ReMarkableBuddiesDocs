## Why

Updating a Buddy PR description currently starts the complete application
pipeline on unchanged source. Two runs at69faff5 demonstrate this. Removing
edited events entirely would regress the already observed invalid-title then
corrected-title recovery case, while skipped normal application contexts could
replace a prior failing result. Metadata admission needs a bounded correction.

## What Changes

Keep the existing ordered pipeline and maintained title Action. Source events
and actual title changes retain normal check names and full validation. A
body-only edit validates the title but omits application work under explicitly
different metadata-only omitted-job names; it must not create or update the
normal application contexts. Prove actual hosted context behavior before
delivery. No release, artifact, dependency, settings or version policy changes.

Buddy implementation and central contract are this candidate's initial scope.
Manager and SDK require their existing owners' coordinated file leases and
SDK-owned specification reconciliation before implementation there.
