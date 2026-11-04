# Host startup and history integration

Buddy source `a8a183556d13e63ad60d7cb48802fc7a361de1bd` is based on
`4eeaabef92245173ff136e9773c0416de2653466`. The Docs base is
`68ac03324a63cd25af69565e099874eefcfc25e7`.

The source reuses the combined host delta from
[Buddy 34](https://github.com/s116821/ReMarkableBuddies/pull/34) and
[Buddy 35](https://github.com/s116821/ReMarkableBuddies/pull/35).
The paired contract follows [Docs 16](https://github.com/s116821/ReMarkableBuddiesDocs/pull/16)
and [Docs 18](https://github.com/s116821/ReMarkableBuddiesDocs/pull/18).
Their original revisions and historical checks remain attached to those drafts.
The extraction carries the child delta and composes the CLI with current main.
The current ordinary Reader mode and data guard remains held across its consumers.

Windows locked offline integration passed 53 tests across Reader startup/history,
storage configuration, storage inspection CLI, memory maintenance CLI and
provider-boundary controls. The initial parallel build hit Windows virtual
memory limits. The passing run used one Cargo job on the same committed source.
Another 24 library controls passed across Reader runtime, exact original
recovery, ordinary mode, memory preflight and the schema parser. The test build
reported six existing Windows Writer fixture warnings.
Ajv 8.20.0 replayed all 52 structural cases against the actual CLI's schema v2
document. The emitted 9,224 bytes matched the embedded document with SHA-256
`1a5731df59b3a6e08b14e9520467be31a4f62b9b58e665fecdc061d124daf9d8`.

The local evidence covers host behavior. Fresh acquisition, usable
tokenizer-backed context, native effects, Writer, cross-device recovery and
the broader conversation lifecycle remain in durable-conversation-context.
The adapter in Buddy PR48 and its adapted counterpart in PR40 retain separate
custody. Future integration must preserve the ordinary failure and lifetime
contracts documented here.
