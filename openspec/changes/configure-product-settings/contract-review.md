# Shared contract amendment: accepted implementation contract

The single Main proposal b10caaaf-fbff-4092-8d69-dd2216732c01 is reconciled into
contract.md and contract-public.md. No alternate producer schema is introduced.
All shape/default/null/independent-Clear/entry-gate questions in the original draft
are now explicit. Source baseline is Buddy e1e79226b31fddb7339ca3c59038c88f048fc3a9,
as reviewed by Main; source links/pin are attribution, not a local native checkout.

Root accepted the exact amendment before behavior code (receipt below). The
precode vector integrity check was not behavior execution. The deterministic
path/stale-base→conflict and reconstructed-target→invalid-input cases match
Main's reviewed existing conditional writer. Successful apply alone is
true/restart-required; status stays unverified.

Intentional compatibility change: valid export request preflight now precedes
nonsecret config/policy checks, which precede MEM_API_KEY. Error ordering changes;
credential selection precedence and literal values do not. No OS activation or
full destination/Reader-to-Writer qualification is claimed.

Accepted vector corpus:19literal storage cases,60raw protocol frames,19public
requests,17public results and14lifecycle catalog expectations (129definitions).
The Manager now executes the96 raw/public definitions; the19 whole-file fixtures
require producer execution, and the14 catalog entries remain expectations.
Base/path/target arithmetic was independently checked. Final source receipts
and producer replay are attributed separately in acceptance evidence. See vector-integrity.json.


## Coordinated acceptance and execution correction

Root accepted exact c3d095c in REM-42 a827a170 after independent native/source
review; implementation admission is complete. No additional planning approval
is pending. Main owns Rust; SCRAPPY-DOO owns the shared consumer and paired Docs;
Root owns independent review, publication, hosted qualification and delivery.

The first consumer run exposed one literal fixture defect: public wrong-reference
used Begin, which supplies no captured reference. Its valid replacement response
reference could not be refused. That one case now uses a valid Save/verified
pairing with a captured b-reference and mismatched c-reference; all other128
entries remain identical. The129-entry corpus is now SHA256
`9f0f2b6e1f2e9c49323390f8038f93fc5a0cd6765dde9f2400e0215e08914152`.
This tests existing reference binding and changes no protocol. See canonical
REM-42 correction904f30ff and progress9f980b87. The catalog/storage definitions
are still distinct from executed consumer tests and producer captures.
