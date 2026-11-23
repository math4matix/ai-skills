#!/usr/bin/env python3
"""Extract text from a CV (.pdf, .docx, .txt) the way an ATS parser sees it.

Usage: uv run --with pypdf python scripts/extract_text.py CV.pdf
Prints page count and text; a near-empty result means a scanned/image PDF (ATS-fatal).
"""
import re, sys, zipfile

path = sys.argv[1]
if path.lower().endswith(".pdf"):
    from pypdf import PdfReader
    r = PdfReader(path)
    print(f"[pages: {len(r.pages)}] [producer: {(r.metadata or {}).get('/Producer')}]")
    # layout mode keeps lines intact; default mode emits one token per line on some PDFs
    text = "\n".join(p.extract_text(extraction_mode="layout") for p in r.pages)
elif path.lower().endswith(".docx"):
    xml = zipfile.ZipFile(path).read("word/document.xml").decode("utf8")
    text = re.sub(r"</w:p>", "\n", xml)
    text = re.sub(r"<[^>]+>", "", text)
else:
    text = open(path, encoding="utf8").read()
text = re.sub(r"[ \t]+", " ", text)
print(text.strip())
if len(text.strip()) < 200:
    print("\n[WARNING: almost no text layer; likely scanned/image CV, ATS cannot read it]")
