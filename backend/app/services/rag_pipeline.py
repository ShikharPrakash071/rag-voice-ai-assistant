rag_pipeline.py

from langchain_core.prompts import PromptTemplate

def build_rag(llm, retriever):

    prompt = PromptTemplate.from_template("""
Answer the question based on the context below.

Context:
{context}

Question:
{question}

Answer:
""")

    def rag_chain(question: str):
        docs = retriever.invoke(question)
        context = "\n\n".join([doc.page_content for doc in docs])

        final_prompt = prompt.format(
            context=context,
            question=question
        )

        response = llm.invoke(final_prompt)
        return response

    return rag_chain