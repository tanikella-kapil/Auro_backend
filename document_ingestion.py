from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
import pdfplumber
from database_config import get_db
from models import Document  # Ensure models.py is correct

router = APIRouter()

# Function to extract text from PDF
def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

# API to upload a document
@router.post("/upload/")
async def upload_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Extract text if it's a PDF
    if file.filename.endswith(".pdf"):
        content = extract_text_from_pdf(file.file)
    else:
        content = (await file.read()).decode("utf-8")

    # Save to database
    new_doc = Document(filename=file.filename, content=content)
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)

    return {"message": "Document uploaded successfully!", "document_id": new_doc.id}
