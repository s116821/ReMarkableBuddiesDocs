# Local verification

Buddy source 83bce1431e61efa7de61c1ee1c9cdcda603e59b3, tree
afccab620cce08c1dce9b3e74624966bde4765c6, changes only the ordinary receiving
instruction and its integration test. The focused locked offline Windows test
passed on that exact head. It used an actual Ledger, reopened the Store for
refinement and captured the prompt parts with a local engine. The original
request, source units and selected draft stayed intact. Absent, disabled and
enabled-empty preferences yielded identical prompt bytes. Effective text was
preserved verbatim once in the distinct part, including multiline Unicode.

The result establishes prompt construction and persisted history behavior.
Hosted and independent review are pending. This is not semantic, native,
frozen notebook plan, running reload or preset-routing qualification.
