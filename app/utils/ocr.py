import pytesseract
from PIL import Image
import pdfplumber

def process_document(file):
    text = ""
    tables = []
    charts = []
    if file.name.lower().endswith(".pdf"):
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
                tables.extend(page.extract_tables())
    else:
        img = Image.open(file)
        text = pytesseract.image_to_string(img)
    return text, tables, charts
