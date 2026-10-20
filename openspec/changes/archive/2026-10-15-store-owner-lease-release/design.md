# Existing repair, current-main qualification

Source basis: actual mainb74395a1 Store::_lease and Store::open; actual failed job116489263395/run38754475546 and tests/storage.rs:85 onward; existing accepted cca7ea9d Drop and selection/publication_tests.rs inherited_descriptor_does_not_extend_a_dropped_owners_lease; storage-owner exact public confirmations6195113780/6195208828. Main preserves existing owner semantics and does not take over the owner's SDK package work.

Explicitly unlock the private lease in Store::drop. The last logical Store owner is being destroyed; public consumers cannot clone its private descriptor. A child-inherited descriptor must not extend that logical ownership. Do not retry acquisition or interpret status metadata as lock authority. Unlock does not permit a second writer while an actual live Store owns the lease.

Adapt the existing regression into a private Unix test module using an owned temporary Store: duplicate the real private descriptor, drop Store, reopen while the duplicate remains alive, close the old duplicate, prove the new owner still excludes another opener, then drop the new owner and reopen again. This is deterministic open-file-description evidence, not a claim to reproduce every subprocess schedule or device behavior. Windows cannot qualify Unix descriptor semantics; retain that explicit platform limit.

Publish the test-only revision first to retain a genuine current-main failing result, then apply only the existing Drop. Use existing ordinary storage process tests and required checks; no unrelated source/SDK/provider matrix. Main is the narrow extraction author with source-owner agreement. Other Main topic refs and every protected native file remain preserved.
