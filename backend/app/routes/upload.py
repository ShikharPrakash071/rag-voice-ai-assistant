from fastapi import APIRouter, UploadFile, File
import os

from app.utils.pdf_loader import load_pdf
from app.utils.chunking import split_docs

router = APIRouter()

UPLOAD_DIR = "data/pdfs"

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save PDF
    with open(file_path, "wb") as f:
        f.write(await file.read())

    print("PDF saved successfully")

    # Load PDF
    print("Loading PDF...")
    documents = load_pdf(file_path)
    print(f"Pages loaded: {len(documents)}")

    # Chunking
    print("Splitting into chunks...")
    chunks = split_docs(documents)
    print(f"Chunks created: {len(chunks)}")

    return {
        "message": "PDF uploaded & processed successfully",
        "pages": len(documents),
        "chunks": len(chunks)
    }