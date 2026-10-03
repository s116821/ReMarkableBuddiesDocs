## Decision

Add one command label to the existing tap/press branch and return after touch_stop
when that label is tap-only. Keep the100ms tap and existing device/range assumptions.
No framebuffer read, additional two-second wait or fixed PNG write follows this
command. Input I/O has no internal absolute deadline; failed writes or termination
before release still lack a release guarantee. Exit0 is no document/UI acknowledgement.

The actual6eba saved source screenshot remained My Files. Why the reported tap had
no visible effect remains unknown. Current evdev uses libc input_event and writes
its raw bytes; libc has explicit32-bit time64 compatibility fields. No ABI patch
is selected without actual target layout/cfg evidence.

Main subsequently reported its actual ARM fixture agrees on16-byte C input_event
and Rust InputEvent, type/code/value offsets8/10/12, and serialized new(3,53,164)
bytes. This is Main-attributed owned ABI evidence, not target input/UI proof or a
binding to the old installed helper. No serializer change is justified here.

## Verification and simulator impact

Run the exact extracted example branch and screenshot tail in a host-owned mock
harness. Verify tap-only emits start/wait/release without capture, existing tap and
press keep capture, invalid coordinates act before input, and failed release cannot
claim success/capture. This is development CLI sequencing; production simulator
behavior is unchanged. Owned tests cannot prove firmware acceptance or UI effects.

No sync/archive until coordinated implementation review and remaining gates finish.
