from fastapi import APIRouter, UploadFile, File
import os

from app.utils.pdf_loader import load_pdf
from app.utils.chunking import split_docs
from app.services.embeddings import get_embeddings
from app.services.vector_store import create_vector_store, save_vector_store

router = APIRouter()

UPLOAD_DIR = "data/pdfs"
VECTOR_DIR = "data/vector_store"

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

    # 🔥 Embeddings
    print("Creating embeddings...")
    embeddings = get_embeddings()

    # 🔥 Vector DB (FAISS)
    print("Storing in FAISS...")
    db = create_vector_store(chunks, embeddings)

    # 🔥 Save Vector DB
    save_vector_store(db, VECTOR_DIR)
    print("Vector DB saved successfully")

    return {
        "message": "PDF uploaded & processed successfully",
        "pages": len(documents),
        "chunks": len(chunks)
    }