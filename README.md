# 🚀🎤 Voice-Enabled AI Document Assistant (RAG + Domain Mini GPT)

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-Apache--2.0-blue)
![Stars](https://img.shields.io/github/stars/ShikharPrakash071/rag-voice-assistant?style=social)
![Forks](https://img.shields.io/github/forks/ShikharPrakash071/rag-voice-assistant?style=social)
![Issues](https://img.shields.io/github/issues/ShikharPrakash071/rag-voice-assistant)
![Last Commit](https://img.shields.io/github/last-commit/ShikharPrakash071/rag-voice-assistant)
![Repo Size](https://img.shields.io/github/repo-size/ShikharPrakash071/rag-voice-assistant)

<p align="center">
  <b>🚀 Production-ready AI system | 🎤 Voice + 📄 Documents | 🧠 RAG + Mini GPT</b>
</p>

> 🎤 Talk to your documents
> 📄 Turn PDFs into intelligent knowledge systems
> 🧠 Ask anything — via voice or text
> ⚡ Powered by RAG + Domain-Specific Mini GPT

---

## 🌍🧩 Problem Statement

In today’s world, we deal with **huge amounts of unstructured data** like:

📄 PDFs • 📑 Reports • 📚 Research Papers • ⚖️ Legal Docs

But:

* ❌ Searching is slow (Ctrl+F ≠ understanding)
* ❌ No contextual answers
* ❌ Chatbots don’t understand your documents
* ❌ General AI ≠ domain expertise

👉 We need a system that can **understand, retrieve, and respond intelligently**.

---

## 💡🚀 Solution

Introducing a **next-gen AI system** that combines:

### 🔹 🧠 RAG (Retrieval-Augmented Generation)

→ Accurate answers from your documents

### 🔹 🧠⚡ Domain-Specific Mini GPT

→ Ask questions **without uploading PDFs**

### 🔹 🎤 Voice Interaction Layer

→ Natural, real-time conversations

---

### 🎯 What You Can Do

* 📄 Upload PDFs → 🔍 Instantly searchable
* 🧠 Ask questions → 🎯 Context-aware answers
* 🎤 Speak → 🔊 Get voice replies
* ⚡ Ask domain questions → 📚 No upload needed

👉 Basically:
**ChatGPT for your documents + Focused AI for your domain** 🔥

---

## 🔥✨ Core Features

### 🧠 1. AI Brain (RAG Pipeline)

* 📄 Chunking → 🧠 Embeddings → 🔍 Retrieval → 🤖 LLM → 💬 Answer
* 🎯 Context-aware, grounded responses
* ❌ Reduced hallucination

---

### 📄 2. PDF Ingestion Engine

* 📥 Upload via API
* 📄 Smart parsing (page-wise)
* ✂️ Intelligent chunking
* 🧠 Embedding generation
* 💾 FAISS storage

✔ Convert raw PDFs → intelligent systems

---

### 🔍 3. Smart Query Engine

* 🔎 Semantic search (FAISS)
* 📊 Top-k retrieval
* 🧠 LLM reasoning
* 💬 Accurate responses

---

### 🧠⚡ 4. Domain-Specific Mini GPT (⭐ Highlight)

* 📚 Pre-loaded knowledge base
* 🚫 No upload required
* 🎯 Domain-restricted answers

✔ Acts like **Mini ChatGPT (focused + accurate)**

---

### 🎤 5. Voice AI System

* 🎙️ Speech-to-Text
* 🧠 RAG processing
* 🔊 Text-to-Speech

✔ Full conversational loop

---

### 🔊 6. Audio Engine

* 🎧 gTTS-based synthesis
* 📁 Unique audio file generation
* 🌐 API-based playback

---

### ⚡ 7. Performance Optimizations

* 💤 Lazy loading
* 🧠 LRU caching
* ⚡ Fast startup & response

---

## 🏗️⚙️ System Architecture

```id="w3y7a1"
User (🎤 Voice / ⌨️ Text)
        ↓
🐳 Dockerized FastAPI Backend
        ↓
-------------------------------------------------
| 🗄️ PostgreSQL (Users / Metadata)              |
| 🧠 FAISS (Vectors: PDFs + Domain Knowledge)   |
| 📁 Local Storage (PDFs + Audio)               |
-------------------------------------------------
        ↓
⚡ Groq LLM (Inference Engine)
        ↓
💬 Response (Text + 🔊 Audio)
```

---

## 🔄🔁 End-to-End Flow

### 📄 Upload Flow

1. 📥 Upload PDF
2. 💾 Store locally
3. 📄 Parse text
4. ✂️ Chunk
5. 🧠 Generate embeddings
6. 🔍 Store in FAISS
7. 🗄️ Save metadata

---

### 🎤 Query Flow

1. 🎤 Speak / ⌨️ Type
2. 🔄 Convert to text
3. 👤 Identify user
4. 🔍 Retrieve context (FAISS / Domain DB)
5. 🤖 LLM generates answer
6. 🔊 Convert to audio
7. 💬 Return response

---

## 🧱🛠️ Tech Stack

| Layer        | Tech                 |
| ------------ | -------------------- |
| ⚙️ Backend   | FastAPI              |
| 🗄️ Database | PostgreSQL           |
| 🧠 Vector DB | FAISS                |
| 🤖 LLM       | Groq API             |
| 🧬 Embedding | HuggingFace (MiniLM) |
| 🔊 Audio     | gTTS                 |
| 📁 Storage   | Local                |
| 🐳 Deploy    | Docker               |

---

## 🚀📈 Scalability Plan

| Layer        | Upgrade 🔥 |
| ------------ | ---------- |
| 🧠 Vector DB | Pinecone   |
| ⚡ Cache      | Redis      |
| 📁 Storage   | AWS S3     |
| 🚀 Deploy    | Kubernetes |

---

### 🧠 Why Upgrade?

* ⚡ Pinecone → scalable vector search
* ⚡ Redis → ultra-fast caching
* ☁️ S3 → infinite storage
* 🐳 K8s → production deployment

---

## ⚙️🧑‍💻 Setup

```bash id="e6l2tx"
git clone https://github.com/ShikharPrakash071/rag-voice-assistant.git
cd rag-voice-assistant

pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 🐳 Docker

```bash id="xq7b91"
docker build -t ai-doc-assistant .
docker run -p 8000:8000 ai-doc-assistant
```

---

## 🔌 API

* 📄 `POST /upload`
* 🔍 `POST /query`
* 🎤 `POST /voice-query`
* 🔊 `GET /audio/{file}`

---

## 🎯💼 Use Cases

* 📚 Study assistant
* 🏢 Business intelligence
* ⚖️ Legal analysis
* 🧾 Research exploration
* 🧠 Domain AI systems

---

## 🧪 Testing

```bash id="i5k1kz"
curl -X POST http://localhost:8000/voice-query \
--data-binary @input.wav \
--output output.mp3
```

---

## 📌🗺️ Roadmap

### ✅ Phase 1 — Foundation

* PDF ingestion
* FAISS storage
* RAG pipeline

---

### ✅ Phase 2 — Intelligence

* Query system
* LLM integration
* Mini GPT

---

### ✅ Phase 3 — Voice AI

* STT + TTS
* Real-time interaction

---

### 🚧 Phase 4 — Product

* Auth system
* Multi-user support
* Dashboard

---

### 🚀 Phase 5 — Scale

* Docker optimization
* Cloud deploy
* Pinecone + Redis + S3
* Streaming responses

---

## 🤝💬 Contributing

PRs, ideas, improvements are welcome 🚀
Let’s build something powerful together

---

## 📜 License

Apache-2.0 License

---

🔥 Built with ambition, engineered for production — ready to scale.
