## ADDED Requirements

### Requirement: Ordinary resident startup waits for quiet before activation

During ordinary installed Reader startup, valid input activity in read-only preparation SHALL defer activation under the original startup deadline and main-thread service health owner. The service SHALL use a fresh guard and repeat the read-only admission after quiet input. It SHALL record a non-sensitive waiting status and retain the existing activation completion status. Lost input integrity, an occupied activation slot or failed admission SHALL stop startup. The publication boundary and subsequent activation SHALL use the existing strict guard and recovery behavior.

#### Scenario: Input during read-only startup

- **WHEN** input is active during ordinary startup before activation publication
- **THEN** Reader waits for quiet and rechecks admission within the same startup deadline, without creating a Reader request or attempting activation under the canceled guard.

#### Scenario: Input after the protected boundary

- **WHEN** input changes after the protected activation boundary or during an ordinary Reader request
- **THEN** the existing cancellation and recovery handling applies, without automatically retrying any protected action.
