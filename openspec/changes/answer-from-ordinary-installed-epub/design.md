# Design

The application binds the open document and native page order to the saved page table and the original EPUB bearing the same document ID. A redirect identifies an original rendered page and distinguishes a handwritten page inserted into the book. It gives no location within an EPUB spine section. Reader obtains section names and reading order from the original publication.

Use the existing isolated retrieval worker, deadlines, input cancellation and bounded cache. Key the text to the document ID, original-byte digest, extractor revision and normalized units. Recheck the current page, table, file and conversation before publishing an answer. A change to the original bytes invalidates reuse. Inserting a Buddy page between questions can preserve it.

The ordinary Reader setting for EPUBs is local to the device. A PDF-only declaration continues to admit PDFs alone. Existing queued Writer requests take priority before book content is read. Research still follows the saved policy and an explicit no-internet request. The answer uses the usual bounded set of passages, with section provenance for EPUBs.
