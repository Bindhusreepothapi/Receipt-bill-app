from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from backend.ocr_parser import parse_receipt

app = FastAPI()

# Allow frontend (like Streamlit) to access this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Receipt OCR Backend is Running ✅"}

@app.post("/upload/")
async def upload_receipt(file: UploadFile = File(...)):
    contents = await file.read()
    result = parse_receipt(contents, file.filename)
    return {"parsed_data": result}
