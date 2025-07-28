# 🧾 Receipt OCR Application

This is a full-stack Python project that uses OCR to extract receipt details, stores them in a SQLite database, and visualizes them on a Streamlit dashboard.

## 🔗 Live Demo

- **Frontend (Netlify):** [https://app.netlify.com/projects/friendly-bunny-f0c0f7/overview--frontend](https://app.netlify.com/projects/friendly-bunny-f0c0f7/overview--frontend)
- **Backend (Render):** [ http://127.0.0.1:8000/docs]( http://127.0.0.1:8000/docs)
- **GitHub Repo:** [Receipt Bill App](https://github.com/bindhusreepothapi/Receipt-bill-app)

---

## 🔧 Tech Stack

- **Frontend:** React, HTML, CSS
- **Backend:** FastAPI, Uvicorn, Python
- **OCR Engine:** Pytesseract (Tesseract OCR)
- **Database:** SQLite + SQLAlchemy
- **Dashboard:** Streamlit
- **Deployment:** Netlify (Frontend), Render(Backend)
- **Frontene_old:** streamlit

---

## 🚀 Features

- Upload image of printed receipts
- Extracts text using Tesseract OCR
- Parses date, total, items, vendor etc.
- Stores parsed data in SQLite
- RESTful API using FastAPI
- React frontend for uploading images
- Interactive dashboard with Streamlit
- Deployment on Netlify and Render
---


## 📁 Project Structure

```
ReceiptBillApp/
│
├── backend/                         # FastAPI backend
│   ├── __init__.py
│   ├── db.py                        # Database setup (SQLite + SQLAlchemy)
│   ├── main.py                      # FastAPI app & routes
│   ├── models.py                    # Receipt ORM model
│   ├── ocr_parser.py                # OCR and receipt parsing logic
│   ├── utils.py                     # Utility functions
│
├── dashboard/                       # Streamlit dashboard
│   └── dashboard_app.py             # Streamlit app for data visualization
│
├── frontend/                        # React frontend
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.js                   # Upload form component
│   │   ├── index.js                 # Entry point
│   │   └── styles.css               # Optional: styles if any
│   ├── package.json                 # React project config
│   └── .env                         # (optional) for proxy or backend URL
│
├── receipts.db                      # SQLite database (auto-created)
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
├── project-structure.txt            # Text version of this tree
├── .gitignore
└── LICENSE                          # (Optional) MIT License or similar

```


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

▶️ Frontend Setup

cd frontend
npm install
npm start
This will open the frontend in your browser.

▶️ Streamlit Dashboard

cd ../dashboard
streamlit run dashboard_app.py

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
