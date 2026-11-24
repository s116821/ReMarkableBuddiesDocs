## Placement

Reader and Writer share the existing typed output and destination renderer. Writer first checks whether its plain draft can be typed. If placement resolves to an insertion, Reader and Writer check the exact text for the new page, including its title and any admissible About line. The check runs before creating an insertion request. A reused page keeps its own display procedure and the renderer rechecks the final text under its existing authority.

An unsupported payload leaves the generated answer or draft in its conversation. The application reports output unavailable. A transport error or an uncertain insertion keeps the existing recovery behavior.
