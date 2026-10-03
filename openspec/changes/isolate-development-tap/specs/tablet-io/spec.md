## ADDED Requirements

### Requirement: Explicit development tap without capture
The development hardware helper SHALL support tap-only using the existing tap
sequence and SHALL return after successful release without the common screenshot
wait, framebuffer capture or fixed PNG write. Success SHALL NOT imply UI completion.

#### Scenario: Input-only command
- **WHEN** tap-only receives valid coordinates and both event writes succeed
- **THEN** the existing touch start,100ms wait and release occur without capture.

#### Scenario: Existing capture commands
- **WHEN** existing tap or press succeeds
- **THEN** the common capture behavior is preserved.

#### Scenario: Error before successful release
- **WHEN** parsing or a touch write fails
- **THEN** the command does not claim success or perform the common capture tail.
