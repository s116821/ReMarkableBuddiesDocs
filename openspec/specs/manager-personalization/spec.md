# Shared Manager personalization editor

## Purpose
Inspect and edit the actual supported personalization configuration over bounded authenticated wired hosts, preserving exact text and distinguishing disk readback from running activation.

## Requirements

### Requirement: Shared actual personalization configuration editing
The Manager SHALL inspect, edit, save, disable and clear the actual supported versioned personalization setting in both browser and Electron through the same bounded fixed-command wired host integration. It SHALL preserve exact valid multiline Unicode text, honor the backend field limits and keep prompts out of routine logs and command arguments. Unsupported or unavailable commands SHALL NOT appear saved or silently fall back to another writer.

#### Scenario: Verified shared edit
- **WHEN** the supported command accepts an exact valid edit and returns consistent current identity, schema, digest and disk readback
- **THEN** both distributions display that verified saved setting without changing its text or unrelated configuration/history.

#### Scenario: Invalid or unsupported edit
- **WHEN** the actual schema/command/text or configured wired host is unavailable, invalid or unsupported
- **THEN** editing refuses with truthful state rather than persisting a fabricated configuration or revealing prompt diagnostics.

### Requirement: Current identity and guarded configuration custody
The Manager SHALL bind mutation to the inspected connection/boot and backend whole-config digest, preserve the backend's lease/CAS and refuse arbitrary paths/commands or unauthorized callers. It SHALL suppress stale UI results, handle contention without automatic retry and distinguish cancelled/unknown commit outcomes from proved nonmutation.

#### Scenario: Configuration or tablet changes
- **WHEN** the config digest, wired identity, boot or request generation changes during an edit
- **THEN** stale success is refused and a fresh supported inspection is required before another guarded mutation.

#### Scenario: Timeout after possible commit
- **WHEN** mutation transport is cancelled or times out after the backend may have committed
- **THEN** the Manager reports outcome unknown and uses fresh verified inspection rather than claiming no write or repeating the write automatically.

### Requirement: Saved setting and running activation are distinct
The Manager SHALL distinguish verified configuration saved on disk from actual running activation. A restart-required receipt SHALL stay visibly unactivated, with no implicit service restart or claim about an in-flight or next request. Disable and clear SHALL follow the real command semantics without deleting history or learned records.

#### Scenario: Saved but restart required
- **WHEN** the actual command verifies disk readback and reports restart-required
- **THEN** the UI confirms only the saved setting and displays that running activation remains pending.

#### Scenario: Disable or clear
- **WHEN** the user explicitly disables or clears through a current guarded supported command
- **THEN** the UI displays the actual verified field/readback semantics and preserves unrelated data and truthful activation state.
