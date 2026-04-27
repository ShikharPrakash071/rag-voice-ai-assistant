# 📄 RAG Voice Assistant (PDF Q&A System)

This project is a Retrieval-Augmented Generation (RAG) based backend system that allows users to upload PDF documents, process them into structured knowledge, and prepare them for intelligent question answering using modern LLM pipelines.

The system is designed to be **fully GPU-free**, cost-efficient, and production-scalable, using local vector storage and open-source embeddings.

---

## 🚀 Current Features (MVP - Phase 1 Complete)

- 📂 Upload PDF documents via FastAPI
- 📄 Parse PDFs into structured text (page-wise extraction)
- ✂️ Intelligent text chunking using recursive splitting
- 🧠 Generate embeddings using HuggingFace models
- 🔍 Store embeddings in FAISS vector database
- 💾 Persist vector database locally for reuse

---

## 🏗️ Tech Stack (Updated & Accurate)

### 🔹 Backend
- **FastAPI** – High-performance async API framework

### 🔹 RAG Pipeline
- **LangChain (modular ecosystem)**  
  - `langchain-core`
  - `langchain-community`
  - `langchain-text-splitters`
  - `langchain-huggingface`

### 🔹 Embeddings
- **HuggingFace Sentence Transformers**
  - Model: `all-MiniLM-L6-v2`
  - Fully CPU-compatible (no GPU required)

### 🔹 Vector Database
- **FAISS (Facebook AI Similarity Search)**
  - Local, fast, efficient similarity search
  - No external DB dependency

### 🔹 PDF Processing
- **PyPDF (via LangChain loaders)**

---

## 🧠 System Architecture (Current)


User Upload → FastAPI → PDF Loader → Chunking → Embeddings → FAISS → Stored Locally

---

## 🔄 Data Flow Explained

1. User uploads a PDF via API
2. PDF is saved to local storage (`data/pdfs/`)
3. PDF is parsed into page-level documents
4. Documents are split into smaller chunks
5. Each chunk is converted into vector embeddings
6. Embeddings are stored in FAISS
7. Vector database is saved locally for later retrieval

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/rag-voice-assistant.git
cd rag-voice-assistant/backend

### 2. Create virtual environment
Bash
python -m venv venv
source venv/Scripts/activate  # Windows (Git Bash)

### 3. Install dependencies
Bash
pip install -r requirements.txt

### 4. Run the server
Bash
uvicorn app.main:app --reload

### 5. Open API docs

http://127.0.0.1:8000/docs

Example Output
After uploading a PDF:
JSON
{
  "message": "PDF uploaded & processed successfully",
  "pages": 78,
  "chunks": 86
}

⚠️ Important Notes

* Only valid PDFs are supported (not renamed .txt files)

* System is CPU-based and may take time for large documents

* FAISS is local (not yet production distributed)

🎯 Upcoming Features (Next Phases)

🔥 Phase 2 (Next Step)

Question answering API

FAISS retrieval pipeline

Groq LLM integration

🎤 Phase 3

Voice input (Whisper)

Audio output (TTS)

🌐 Phase 4

React frontend (UI)

Chat interface

File management system

💡 Design Philosophy

No GPU dependency

No paid APIs

Modular architecture (production-ready)

Scalable from local → cloud

🤝 Contribution

This project is built as a practical, industry-level RAG system. Contributions, improvements, and suggestions are welcome.

📌 Status

✅ Phase 1 Complete: Data Ingestion + Vectorization

🚧 Phase 2 In Progress: Query + LLM Integration


