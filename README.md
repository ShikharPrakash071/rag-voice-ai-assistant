# 🚀🎤 Voice-Enabled AI Document Assistant (RAG + Domain Mini GPT)

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-Apache--2.0-blue)
![Stars](https://img.shields.io/github/stars/ShikharPrakash071/rag-voice-ai-assistant?style=social)
![Forks](https://img.shields.io/github/forks/ShikharPrakash071/rag-voice-ai-assistant?style=social)
![Issues](https://img.shields.io/github/issues/ShikharPrakash071/rag-voice-ai-assistant)
![Last Commit](https://img.shields.io/github/last-commit/ShikharPrakash071/rag-voice-ai-assistant)
![Repo Size](https://img.shields.io/github/repo-size/ShikharPrakash071/rag-voice-ai-assistant)

<p align="center">
  <b>🚀 Production-ready AI system | 🎤 Voice + 📄 Documents | 🧠 RAG + Mini GPT</b>
</p>

> 🎤 Talk to your documents
> 📄 Turn PDFs into intelligent knowledge systems
> 🧠 Ask anything — via voice or text
> ⚡ Powered by RAG + Domain-Specific Mini GPT

---

## 🧩 Problem Statement

In today’s world, we deal with **huge amounts of unstructured data** like:

📄 PDFs • 📑 Reports • 📚 Research Papers • ⚖️ Legal Docs

But:

* ❌ Searching is slow (Ctrl+F ≠ understanding)
* ❌ No contextual answers
* ❌ Chatbots don’t understand your documents
* ❌ General AI ≠ domain expertise

👉 We need a system that can **understand, retrieve, and respond intelligently**.

---

## 💡 Solution

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

## ✨ Core Features

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

### ⚡ 4. Domain-Specific Mini GPT (⭐ Highlight)

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

## 🏗️ System Architecture

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

## 🔁 End-to-End Flow

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

## 🛠️ Tech Stack

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

## 📈 Scalability Plan

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

## ⚙️ Setup

```bash id="e6l2tx"
git clone https://github.com/ShikharPrakash071/rag-voice-ai-assistant.git
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

## 🎯 Use Cases

### 📚 Education & Learning
- Query textbooks, notes, and PDFs instantly  
- Ask conceptual questions instead of searching manually  
- Voice-based learning assistant  

---

### 🏢 Business & Enterprise
- Analyze reports, SOPs, and internal documents  
- Build company knowledge assistants  
- Reduce time spent on document search  

---

### ⚖️ Legal & Compliance
- Extract insights from contracts and policies  
- Ask clause-based questions  
- Faster document review workflows  

---

### 🧾 Research & Knowledge Work
- Navigate research papers efficiently  
- Summarize and cross-reference documents  
- Build personal research assistants  

---

### 🧠 Domain-Specific AI Assistants
- Create focused AI systems (finance, medical, tech, etc.)  
- Ask domain-restricted questions without uploading files  
- Higher accuracy than general chatbots  

---

### 🎤 Accessibility & Voice Interfaces
- Hands-free document interaction  
- Useful for visually impaired users  
- Natural voice-based querying system  

---

### 🚀 Developer & Product Use Cases
- Integrate as backend for AI SaaS products  
- Build document-based chat applications  
- Extend into full-scale AI platforms  

---

## 🆚 Why Not Just ChatGPT?

While general LLMs like ChatGPT are powerful, they have limitations in **document understanding and domain-specific accuracy**.

This system solves those gaps 👇

---

### 🧠 Context-Aware Answers
- ChatGPT → Generic responses  
- This Project → Answers grounded in your **actual documents (RAG)**  

---

### 📄 Document Intelligence
- ChatGPT → Cannot reliably use your PDFs  
- This Project → Converts PDFs into a **searchable knowledge base**  

---

### 🎯 Domain-Specific Accuracy
- ChatGPT → Broad but inconsistent  
- This Project → **Mini GPT with focused domain knowledge**  

---

### 🎤 Voice Interaction
- ChatGPT → Limited workflows  
- This Project → **Full pipeline (STT → AI → TTS)**  

---

### ⚡ Performance & Control
- ChatGPT → Black-box  
- This Project → **Full system control**  

---

### 🔐 Data Ownership
- ChatGPT → External  
- This Project → **Your data stays local**  

---

### 🚀 Extensibility
- ChatGPT → Fixed  
- This Project → **Build your own AI product**  

---

## 🎯 Final Takeaway

👉 Not just a chatbot  
👉 A **complete AI system for documents + domain intelligence**

---

## 🧠 Architecture Decisions (Explained)

This project is built with **production thinking**, not just as a demo.

---

### ⚙️ FastAPI
- Async, fast, scalable  
- Ideal for AI APIs  

---

### 🧠 RAG over Fine-Tuning
- Dynamic knowledge  
- No retraining  
- Cost-efficient  

---

### 🔍 FAISS
- Fast local vector search  
- No external dependency  
- MVP-friendly  

---

### 🗄️ PostgreSQL
- Structured data (users, metadata, logs)  
- Clean separation from embeddings  

---

### 🧠 HuggingFace Embeddings
- CPU-friendly  
- Open-source  
- Fully local pipeline  

---

### ⚡ Groq LLM
- Ultra-fast inference  
- Low latency responses  

---

### 🎤 Voice Pipeline
- STT → RAG → TTS  
- Real-world usability  

---

### 🐳 Docker
- Consistent environments  
- Production-ready deployment  

---

## ⚖️ Trade-offs & Design

- FAISS (local) → Pinecone (scale)  
- Local storage → S3  
- No Redis yet → simplicity first  

👉 Philosophy: **Simple → Functional → Scalable**

---

## 🚀 System Philosophy

- ❌ Avoid unnecessary complexity  
- ✅ Build working systems first  
- ✅ Scale when needed  

---

## 🧠 System Design Explanation

User (Voice / Text)
 ↓
FastAPI Backend (Dockerized)
 ↓
| PostgreSQL (Users / Metadata) |
| FAISS (PDF + Domain Embeddings) |
| Local Storage (PDFs + Audio Files) |
 ↓

Groq LLM (Inference)
 ↓
Response (Text + Audio)


👉 Flow:
- User interacts via text/voice  
- Backend processes request  
- Relevant context retrieved from FAISS  
- LLM generates response  
- Output returned as text/audio  

👉 This design ensures:
- ⚡ Fast retrieval  
- 🧠 Context-aware answers  
- 📈 Easy scalability

---

## 🧪 Testing

```bash id="i5k1kz"
curl -X POST http://localhost:8000/voice-query \
--data-binary @input.wav \
--output output.mp3
```

---

## 📌 Roadmap

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

## 🤝 Contributing

PRs, ideas, improvements are welcome 🚀
Let’s build something powerful together

---

## 📜 License

Apache-2.0 License

---

🔥 Built with ambition, engineered for production — ready to scale.
