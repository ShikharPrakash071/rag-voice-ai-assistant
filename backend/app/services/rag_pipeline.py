from langchain_core.prompts import PromptTemplate

def build_rag(llm, retriever):

    prompt = PromptTemplate.from_template("""
You are an AI assistant that answers questions based on the provided context.

Instructions:
- Use the context as the main source of truth
- Answer clearly and directly
- If the answer is partially available, still try to answer
- Avoid saying "not enough context" unless truly necessary

Context:
{context}

Question:
{question}

Answer:
""")

    def rag_chain(question: str):
        # Retrieve relevant chunks
        docs = retriever.invoke(question)

        # Combine all chunks into context
        context = "\n\n".join([doc.page_content for doc in docs])

        # Format final prompt
        final_prompt = prompt.format(
            context=context,
            question=question
        )

        # Get response from LLM
        response = llm.invoke(final_prompt)

        return response

    return rag_chain