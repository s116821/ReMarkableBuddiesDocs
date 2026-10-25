# Explicit single-byte TrueType PDF text

## Why

The existing adapter rejects simple TrueType fonts with explicit ToUnicode maps,
even when they supply bounded unambiguous single-byte codes. Its Unicode path is
currently restricted to Type0 Identity-H with two-byte source codes. REM-4's PDF
support can cover this additional declared text layer through the existing parser.

## Scope

Admit a closed TrueType/WinAnsiEncoding profile with explicit one-byte ToUnicode,
bounded width metadata and the existing descriptor validator. Bind cached maps to
their source width, reuse current expansion/target/output controls and advance the
fixed extractor revision for fresh PDFs. Preserve old Type1/Type0 behavior and
whole-document refusal. No font/program interpreter, encoding guess/fallback,
dependency, SDK/runtime/model/network/native or configuration change is selected.
This is text-layer support, not font validity, rendered glyph fidelity or OCR.
