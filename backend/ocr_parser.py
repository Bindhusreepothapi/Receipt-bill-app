from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes
import io
import re 
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def parse_receipt(file_bytes, filename):
    try:
        if filename.lower().endswith(".pdf"):
            images = convert_from_bytes(file_bytes)
            text = ""
            for img in images:
                text += pytesseract.image_to_string(img)
        else:
            image = Image.open(io.BytesIO(file_bytes))
            text = pytesseract.image_to_string(image)

        # REGEX logic to extract real fields
        vendor_match = re.search(r"(?i)vendor[:\-]?\s*(.+)", text)
        amount_match = re.search(r"(?i)(total|amount)[:\-]?\s*[\$₹]?\s*([\d,]+\.\d{2})", text)
        date_match = re.search(r"\d{4}[-/]\d{2}[-/]\d{2}", text)

        vendor = vendor_match.group(1) if vendor_match else "Not Found"
        amount = amount_match.group(2) if amount_match else "Not Found"
        date = date_match.group(0) if date_match else "Not Found"

        return {
            "vendor": vendor.strip(),
            "total_amount": amount.strip(),
            "date": date.strip(),
            "raw_text": text
        }

    except Exception as e:
        return {"error": str(e)}
