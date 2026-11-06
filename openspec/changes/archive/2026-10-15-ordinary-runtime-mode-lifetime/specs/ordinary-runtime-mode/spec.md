## ADDED Requirements

### Requirement: Ordinary Reader mode lifetime
The ordinary Reader SHALL hold a distinct Store-owned mode lifetime guard from
final ordinary admission through its actual Ledger, memory, worker and loop
consumption. Admission SHALL validate the exact current mode token and accept
only absent mode or LocalOnly under the established configuration policy. Mode
transitions through the Store API SHALL refuse while an ordinary guard exists.
Dropping the guard SHALL release only its mode exclusion. The guard SHALL grant
no publishing, selected-domain, provider or native permission.

#### Scenario: Ordinary consumers retain local mode
- **WHEN** an ordinary Reader admits absent mode or LocalOnly with synchronization disabled and another handle attempts a mode transition
- **THEN** the transition refuses until every ordinary guard is dropped, while existing local data remains usable and unchanged.

#### Scenario: Nonlocal or stale admission refuses
- **WHEN** ordinary admission observes isolated/shared mode, contradictory LocalOnly configuration, a stale token or malformed mode state
- **THEN** it refuses before ordinary model/device effects without changing modes or falling back to another state.

### Requirement: Preserve existing mode boundaries
Ordinary mode fencing SHALL reuse the existing Store and mode exclusion rather
than broaden publisher leases, duplicate operation ownership or introduce a
second sync engine. Absent-mode legacy publisher compatibility SHALL remain
explicit; LocalOnly SHALL continue to refuse that publisher. Selected receiving
and historical recovery SHALL retain their independent authority boundaries.

#### Scenario: Existing publication and recovery policies remain distinct
- **WHEN** ordinary lifetime fencing is added to the existing application
- **THEN** absent-mode legacy operation remains compatible, explicit modes cannot invoke that legacy publisher, and no ordinary guard authorizes selected receiving or alters token-free historical recovery.
