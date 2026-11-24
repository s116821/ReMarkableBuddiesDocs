## Why

Buddy can start from built-in defaults and accumulate user data before it has a saved configuration file. Manager's existing preference editor needs a saved revision, and the clean setup path requires empty roots.

## What Changes

Add explicit check and create operations for the first saved defaults on an existing local Buddy installation. Reuse the clean setup publisher and the existing wired first-configuration flow. Keep the personalization editor's saved-revision interface.
