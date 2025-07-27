# 🧾 Receipt OCR App

# 🧾 Receipt OCR Application

This is a full-stack Python project that uses OCR to extract receipt details, stores them in a SQLite database, and visualizes them on a Streamlit dashboard.

## 🔧 Tech Stack

- **Backend**: FastAPI
- **OCR**: Tesseract via pytesseract
- **Database**: SQLite + SQLAlchemy
- **Frontend**: Streamlit
- **Language**: Python 3

---

## 📌 Features

- Upload receipt images (JPG/PNG)
- Automatically extract text using OCR (pytesseract)
- Display and download the extracted text
- Backend built with FastAPI
- Frontend built with Streamlit
- Lightweight, easy to run locally

---

## 📂 Project Structure
ReceiptBillApp/
├── backend/            # FastAPI backend + OCR logic + DB
│   ├── db.py
│   ├── main.py
│   ├── models.py
│   ├── ocr_parser.py
│   ├── utils.py
│   └── receipts.db
│
├── dashboard/          # Streamlit dashboard
│   └── dashboard_app.py
│
├── uploaded_receipts/  # Uploaded image storage
├── samples/            # Sample receipts
├── frontend/           # Optional streamlit UI (if applicable)
│   └── app.py
│
├── requirements.txt
├── README.md
└── .gitignore

⚙️ Installation
1. Clone the Repository

```bash
git clone https://github.com/your-username/ReceiptBillApp.git
cd ReceiptBillApp

2. Create a Virtual Environment

python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate  # On macOS/Linux

3. Install Dependencies
make sure the filename is correct:requirements.txt
pip install -r requirements.txt  #command for installation
If you don’t have Tesseract installed:

Download from: https://github.com/tesseract-ocr/tesseract

Add its path to your environment variables

Example path: C:\Program        Files\Tesseract-OCR\tesseract.exe

🚀 Running the App Locally
▶️ Start FastAPI Backend
 cd backend
 uvicorn main:app --reload
By default, backend will be running at:
👉 http://127.0.0.1:8000
👉 Swagger UI: http://127.0.0.1:8000/docs

▶️ Start Streamlit Frontend (New Terminal)

cd frontend
streamlit run app.py
This will open the frontend in your browser.

🖼️ Sample Output
Upload receipt →
![App Screenshot](C:\Users\Bindu Sree\Desktop\ReceiptBillApp\screenshot.png)

🧠 How it Works
Uses pytesseract to extract text from the uploaded image

FastAPI handles image upload and returns extracted text

Streamlit sends the image to backend and displays results

📦 Dependencies
fastapi
uvicorn
streamlit
opencv-python
pytesseract
pillow
python-multipart

Install via:
pip install -r requirements.txt
🔧 Tesseract Installation (Required)
Make sure Tesseract OCR is installed on your system.

📥 Windows:
Download from: https://github.com/tesseract-ocr/tesseract

Install and add the path to tesseract.exe in your system environment variables
e.g., C:\Program Files\Tesseract-OCR\tesseract.exe

📁 Sample Receipts
Use the sample_receipts/ folder to test different receipt images.

💡 Future Improvements
Export results to PDF
Multi-language OCR support
Save history of scans

🙌 Credits
OCR: Tesseract OCR
UI: Streamlit
API: FastAPI

📜 License
This project is licensed under the MIT License.


