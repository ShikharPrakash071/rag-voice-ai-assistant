from fastapi import APIRouter
from app.services.retriever import get_retriever
from app.services.groq_llm import get_llm
from app.services.rag_pipeline import build_rag

router = APIRouter()

@router.post("/query")
def query(question: str):
    # Lazy loading inside function
    retriever = get_retriever()
    llm = get_llm()

    rag_chain = build_rag(llm, retriever)  # 👈 IMPORTANT (ye missing tha)

    response = rag_chain(question)

    return {"answer": response.content}