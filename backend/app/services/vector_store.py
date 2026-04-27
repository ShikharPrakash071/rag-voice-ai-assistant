from langchain_community.vectorstores import FAISS

def create_vector_store(chunks, embeddings):
    return FAISS.from_documents(chunks, embeddings)

def save_vector_store(db, path):
    db.save_local(path)