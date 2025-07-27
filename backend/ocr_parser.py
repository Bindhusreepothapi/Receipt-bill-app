# --- backend/ocr_parser.py ---
import pytesseract
from PIL import Image
import re


def parse_receipt(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))

    # Simple regex-based parsing
    merchant = text.split('\n')[0]
    total_match = re.search(r'Total[:\s]*\$?(\d+[.,]?\d*)', text, re.IGNORECASE)
    date_match = re.search(r'(\d{2}/\d{2}/\d{4})', text)

    total = float(total_match.group(1).replace(',', '')) if total_match else 0.0
    date = date_match.group(1) if date_match else "Unknown"
    items = "; ".join(line for line in text.split('\n') if any(c.isalpha() for c in line) and re.search(r'\d', line))

    return {
        "merchant": merchant.strip(),
        "total": total,
        "date": date,
        "items": items
    }