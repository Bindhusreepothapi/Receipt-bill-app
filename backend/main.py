
# --- backend/main.py ---
from fastapi import FastAPI, UploadFile, File, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import os
from backend import ocr_parser, utils
from backend import db,models
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
models.Base.metadata.create_all(bind=db.engine)

@app.get("/")
def root():
    return {"message": "Hello from FastAPI on Render!"}

@app.get("/", response_class=HTMLResponse)
async def root():
    return "<h2>✅ Receipt OCR API is Running</h2><p>Go to <a href='/docs'>/docs</a> to explore.</p>"


UPLOAD_DIR = "uploaded_receipts"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
def upload_receipt(file: UploadFile = File(...), db_session: Session = Depends(db.get_db)):
    filepath = os.path.join(UPLOAD_DIR, file.filename)
    utils.save_upload_file(file, filepath)

    parsed_data = ocr_parser.parse_receipt(filepath)
    receipt = models.Receipt(**parsed_data)
    db_session.add(receipt)
    db_session.commit()
    db_session.refresh(receipt)

    return {"message": "Receipt processed and stored.", "data": parsed_data}

@app.get("/receipts/")
def get_all_receipts(db_session: Session = Depends(db.get_db)):
    return db_session.query(models.Receipt).all()

@app.get("/search/")
def search_receipts(keyword: str, db_session: Session = Depends(db.get_db)):
    return db_session.query(models.Receipt).filter(models.Receipt.merchant.ilike(f"%{keyword}%")).all()
