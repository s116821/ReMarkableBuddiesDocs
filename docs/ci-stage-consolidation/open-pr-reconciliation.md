# Current pull request CI reconciliation

The [original 37-PR snapshot](https://github.com/s116821/ReMarkableBuddiesDocs/blob/d5da9cbae67339d3e041692fb647de4e06be3edc/docs/ci-stage-consolidation/open-pr-reconciliation.md) remains immutable evidence. The current delivery consists of 35 retained feature branches plus two explicitly retired CI drafts. This table is a source/CI propagation inventory, not acceptance of every feature.

## Original retained branches

| Repository PR | Current delivered head | Validation status |
| --- | --- | --- |
| [ReMarkableBuddies#58](https://github.com/s116821/ReMarkableBuddies/pull/58) | `7dc17fb6e914404627b23602715b064e34054525` | Run38835530597 passed all four stages |
| [ReMarkableBuddies#52](https://github.com/s116821/ReMarkableBuddies/pull/52) | `e6bddd41ee28abc38bdbf7c734ba4496081c202d` | Current workflow/build wiring verified; unrelated source conflicts remain |
| [ReMarkableBuddies#51](https://github.com/s116821/ReMarkableBuddies/pull/51) | `77f22745535d99eccfe4518aa087989bc4916940` | Current workflow/build wiring verified; unrelated source conflicts remain |
| [ReMarkableBuddies#50](https://github.com/s116821/ReMarkableBuddies/pull/50) | `106f1bf725931c1e85feb03dad2afaa462d78706` | Current workflow/build wiring verified; unrelated source conflicts remain |
| [ReMarkableBuddies#49](https://github.com/s116821/ReMarkableBuddies/pull/49) | `caf4ee5ad90951992defba5417c237d159f1c277` | Current workflow/build wiring verified; unrelated source conflicts remain |
| [ReMarkableBuddies#48](https://github.com/s116821/ReMarkableBuddies/pull/48) | `c4aab985e70d1b95993078a43b4d08c2df0b9362` | Current workflow/build wiring verified; unrelated source conflicts remain |
| [ReMarkableBuddies#45](https://github.com/s116821/ReMarkableBuddies/pull/45) | `cfe083cffc92475fd64f428e2c9a8bb6e24e70f6` | Current workflow/build wiring verified; unrelated source conflicts remain |
| [ReMarkableBuddies#44](https://github.com/s116821/ReMarkableBuddies/pull/44) | `42580d094fffd662c3257bff582cddf2b6abbe7f` | Current workflow/build wiring verified; unrelated source conflicts remain |
| [ReMarkableBuddies#43](https://github.com/s116821/ReMarkableBuddies/pull/43) | `30b23e2cae7a533544aafaaf61ca6fa4985e3066` | Current workflow/build wiring verified; unrelated source conflicts remain |
| [ReMarkableBuddies#42](https://github.com/s116821/ReMarkableBuddies/pull/42) | `6e65076f5dbf63f713fc57f7f35466e292ccc6d8` | Current workflow/build wiring verified; unrelated source conflicts remain |
| [ReMarkableBuddies#41](https://github.com/s116821/ReMarkableBuddies/pull/41) | `5184d4ddec4747f36c55b851153a83bf9703a427` | Current workflow/build wiring verified; unrelated source conflicts remain |
| [ReMarkableBuddies#40](https://github.com/s116821/ReMarkableBuddies/pull/40) | `010aa6b892f464ee04911acbf81b8f38e2f299a6` | Current workflow/build wiring verified; unrelated source conflicts remain |
| [ReMarkableBuddies#39](https://github.com/s116821/ReMarkableBuddies/pull/39) | `214db0071ef45d9153afb34b77a7588b664b7213` | Current workflow/build wiring verified; unrelated source conflicts remain |
| [ReMarkableBuddies#38](https://github.com/s116821/ReMarkableBuddies/pull/38) | `d68d5a0a6b5618904bb069390148e38595e0cdba` | Current workflow/build wiring verified; unrelated source conflicts remain |
| [ReMarkableBuddies#37](https://github.com/s116821/ReMarkableBuddies/pull/37) | `f1bc51293443d7a8519e61556ea8b664253b8a7c` | Current workflow/build wiring verified; unrelated source conflicts remain |
| [ReMarkableBuddies#36](https://github.com/s116821/ReMarkableBuddies/pull/36) | `51387223135610f8ecf9a5c3ca6d2d8619cce6ed` | Current workflow/build wiring verified; unrelated source conflicts remain |
| [ReMarkableBuddies#35](https://github.com/s116821/ReMarkableBuddies/pull/35) | `cb31f471acc928546d04c82c79161ff1b30e3b45` | Current workflow/build wiring verified; unrelated source conflicts remain |
| [ReMarkableBuddies#34](https://github.com/s116821/ReMarkableBuddies/pull/34) | `91cf92f1c1bbddc2ab4189157048ce2c0a960045` | Current workflow/build wiring verified; unrelated source conflicts remain |
| [ReMarkableBuddies#33](https://github.com/s116821/ReMarkableBuddies/pull/33) | `bc930c1cffc990f83f1a1edb477aa52b4f6879d8` | Current workflow/build wiring verified; unrelated source conflicts remain |
| [ReMarkableBuddies#32](https://github.com/s116821/ReMarkableBuddies/pull/32) | `4e897efdec5b38e2d539c5699cc46013011e13f7` | Current workflow/build wiring verified; unrelated source conflicts remain |
| [ReMarkableBuddies#31](https://github.com/s116821/ReMarkableBuddies/pull/31) | `c8fe23cdf24faf52900d4a6507cda57aebb5fe91` | Current workflow/build wiring verified; unrelated source conflicts remain |
| [ReMarkableBuddies#30](https://github.com/s116821/ReMarkableBuddies/pull/30) | `45110b94fed63cedc7416dee40bcc3dff62fcfb2` | Current workflow/build wiring verified; unrelated source conflicts remain |
| [ReMarkableBuddiesManager#8](https://github.com/s116821/ReMarkableBuddiesManager/pull/8) | `a4b7a430ffacca89cbf4488f2513dc51c02532fd` | [Run 38838772070](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/38838772070) passed all five stages |
| [ReMarkableBuddiesManager#9](https://github.com/s116821/ReMarkableBuddiesManager/pull/9) | `7198b2c38fd0a969f1365989c76843303e9c9e95` | [Run 38838772428](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/38838772428) passed all five stages |
| [ReMarkableBuddiesManager#10](https://github.com/s116821/ReMarkableBuddiesManager/pull/10) | `8959ec69e76d269b5e04b9c3517037268ec6db45` | [Run 38838733061](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/38838733061) passed all five stages |
| [ReMarkableBuddiesManager#11](https://github.com/s116821/ReMarkableBuddiesManager/pull/11) | `ff7ab4ba17dbf9934245ffdd29d4c15ff8953c13` | [Run 38838734635](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/38838734635) passed all five stages |
| [ReMarkableBuddiesManager#12](https://github.com/s116821/ReMarkableBuddiesManager/pull/12) | `20f6b331abf4467f22c0d5ca06d0c512e0d04bd3` | [Run 38838737333](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/38838737333) passed all five stages |
| [ReMarkableBuddiesManager#13](https://github.com/s116821/ReMarkableBuddiesManager/pull/13) | `815f8eca0736c73267a6e919a0f2040d18dbbf73` | [Run 38838742354](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/38838742354) passed all five stages |
| [ReMarkableBuddiesManager#14](https://github.com/s116821/ReMarkableBuddiesManager/pull/14) | `6e36aa8a24492f30db5fa104f74ad5c5336bcde4` | [Run 38838744137](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/38838744137) passed all five stages |
| [ReMarkableBuddiesManager#15](https://github.com/s116821/ReMarkableBuddiesManager/pull/15) | `c5bf0bce36501f914e77b1047e5d46fc1ff75bb7` | [Run 38838746649](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/38838746649) passed all five stages |
| [ReMarkableBuddiesManager#16](https://github.com/s116821/ReMarkableBuddiesManager/pull/16) | `e8a4c3b73c16f0f65db57480d6a534a462a51814` | [Run 38838750056](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/38838750056) passed all five stages |
| [ReMarkableBuddiesManager#17](https://github.com/s116821/ReMarkableBuddiesManager/pull/17) | `9513fc3d43545561b9e524753fd163f374b6a9f8` | [Run 38838753442](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/38838753442) passed all five stages |
| [ReMarkableBuddiesManager#18](https://github.com/s116821/ReMarkableBuddiesManager/pull/18) | `ac3b0990498684da93c47cf07d0ddf1e7d9f9aea` | [Run 38838759348](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/38838759348) passed all five stages |
| [ReMarkableBuddiesManager#21](https://github.com/s116821/ReMarkableBuddiesManager/pull/21) | `8ea501221979f32d45f14b29b4b810c2147dfbad` | [Run 38838761529](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/38838761529) passed all five stages |
| [ReMarkableBuddiesManager#22](https://github.com/s116821/ReMarkableBuddiesManager/pull/22) | `a1bd93e6673ef101a7937c5c0f2f8c762f137198` | [Run 38838765268](https://github.com/s116821/ReMarkableBuddiesManager/actions/runs/38838765268) passed all five stages |

Older Buddy branches retain their original source, tests, lockfiles and SDK pins. Their own obsolete version declaration was removed while the remaining parsed manifest stayed equal; current build stamping and Cross environment passthrough were preserved. PR38 retains its original bounded ABI-read hook on the current metadata helper. These are forward CI commits, not a wholesale integration of current main; Rust/source conflicts remain visible and require each feature's later preservation review. No old native or feature qualification is inferred from CI propagation.

All retained Manager branches integrate current main6b2b4d5 and preserve their own common and applicable platform controls. Native Windows cases remain in Windows Integration only where present; common suites run once in Checks. Full-tree independent review confirms unrelated entries are unchanged. Existing consumer compatibility and final run evidence are recorded in [review](review.md).

## Superseded drafts and later PRs

- [Buddy29](https://github.com/s116821/ReMarkableBuddies/pull/29), original864bc5bfbd6a70fac8589d0db5b59ca847388952, CLOSED without merge; branch preserved. [Retirement accounting](https://github.com/s116821/ReMarkableBuddies/pull/29#issuecomment-6206323563).
- [Manager2](https://github.com/s116821/ReMarkableBuddiesManager/pull/2), originalf745642e24ba01daa18359e1bc1638cbdadbe42c, CLOSED without merge; branch preserved. [Retirement accounting](https://github.com/s116821/ReMarkableBuddiesManager/pull/2#issuecomment-6206323981). Its useful generated-dependency ignore fixes shipped through Manager24. Current human docs-layout guidance is in central AGENTS. Historical session-only XOVI notes do not grant new native permission.
- Original failed equal-date GitVersion controls remain failed evidence; the replacement's PSR equal-date/late-tag/retry controls qualify the replacement only.
- [Manager24](https://github.com/s116821/ReMarkableBuddiesManager/pull/24) is merged6b2b4d5 after exact source review and five passing PR stages. Its actual main38837977618 passed five stages and publishedv0.4.4; no settings changes.
- [Manager25](https://github.com/s116821/ReMarkableBuddiesManager/pull/25) preserves the first stacked quiet-refresh candidate; it already carries compact CI and remains unmerged. [Manager26](https://github.com/s116821/ReMarkableBuddiesManager/pull/26) delivered the independently scoped fix as main `c7d015ad975ac56164b874b3bbfc2d9bd63bfc08`, after all five PR stages and scoped review, with identical compact workflow bytes. Its actual-main release follow-through remains separate. Neither introduces old administrative jobs.

Root coordinates normal non-forced branch updates and merges. Feature authors retain their unfinished source gates. Do not archive or merge a feature merely because its CI wiring is reconciled.
