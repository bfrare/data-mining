# read_pdf
import os
from PyPDF2 import PdfReader

pdf_path = r"C:\Users\Asus\Downloads\Is_human_oversight_to_AI_systems_still_possible.pdf"

if os.path.exists(pdf_path):
    reader = PdfReader(pdf_path)
    pages_text = [p.extract_text() for p in reader.pages if p.extract_text()]
    full_pdf_text = "\n".join(pages_text)
    print("✅ :", len(reader.pages))
    print(full_pdf_text[:])
else:
    print(f"⚠️ : {pdf_path}")