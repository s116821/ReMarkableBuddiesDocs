## ADDED Requirements

### Requirement: Installed Reader retains its recognized subject with the original overview

When ordinary installed Reader accepts a source subject, it SHALL retain it on the same resident capture as the normalized center and atomically publish both with the interpreted user turn. It SHALL preserve the role text, original document, page, viewport and image media. When ordinary continuation resolves eligible historical attachments, the subject SHALL appear only on its matching overview association.

#### Scenario: Resume with a stored selected subject

- **WHEN** ordinary continuation reopens a conversation after a Reader interpretation with a retained subject
- **THEN** the existing image association supplies the same subject, origin turn, document, page and center with the verified overview
- **AND** the question and answer remain separate role text

#### Scenario: Resume an earlier capture

- **WHEN** a capture was created with no subject description or explicit subject uncertainty
- **THEN** earlier image and center data remain readable and no subject is synthesized
