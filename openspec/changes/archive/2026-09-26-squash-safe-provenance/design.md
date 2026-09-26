# Design

## Decision

Store exact unique imported blob bytes in `docs/migration/imported-blobs.zip`, keyed by their Git SHA-1 blob IDs, without duplicate path trees. ZIP uses standard deflate, fixed timestamps and sorted entries. The existing manifest maps source repository/commit/path to destination/blob; schema version 2 adds archive location and SHA-256. Do not store a Git bundle of unrelated history, create permanent refs/tags, or rely on an unmerged import commit surviving garbage collection.

Use Python standard-library ZIP/hash handling to check archive integrity, exact member inventory, unique entries, and every Git blob hash (`blob LENGTH\0BYTES`). Support retrieving a known manifest blob to an explicitly new output file, preserving existing files. Verification must not compare against mutable live artifact paths. The archive is immutable historical evidence, not another normative OpenSpec tree.

## Risks and validation

Validate against original source blobs before committing the archive. Tests reject tampered archive, missing/extra/duplicate members, wrong bytes and changed manifest hashes; verify with no live imported files to prove future edits/deletions do not destroy evidence. Create a synthetic squash result and clone only its main branch shallowly; prove the import commit cannot resolve and normal Docs checks pass. CI also uses a shallow checkout. Refresh public instructions/comments to require squash universally and retain linked merge order.
