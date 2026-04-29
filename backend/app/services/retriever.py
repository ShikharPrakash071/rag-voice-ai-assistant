from langchain_community.vectorstores import FAISS
from app.services.embeddings import get_embeddings

VECTOR_DIR = "data/vector_store"

def get_retriever():
    embeddings = get_embeddings()
    db = FAISS.load_local(
        VECTOR_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )
    return db.as_retriever(search_kwargs={"k": 2}) # Adjusted 'k': 3 to 2 for better performance and accuracy balance.