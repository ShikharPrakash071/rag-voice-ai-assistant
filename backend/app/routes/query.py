from fastapi import APIRouter
from app.services.retriever import get_retriever
from app.services.groq_llm import get_llm
from app.services.rag_pipeline import build_rag

router = APIRouter()

# Initialize once
retriever = get_retriever()
llm = get_llm()
rag_chain = build_rag(llm, retriever)

@router.post("/query")
def query(question: str):
    response = rag_chain(question)
    return {"answer": response.content}