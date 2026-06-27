
import streamlit as st
import ollama

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

st.title("PDF RAG Chatbot")

question = st.text_input("Ask a question")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="database",
    embedding_function=embeddings
)

if question:

    docs = db.similarity_search(question, k=3)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Answer the question using only the context.

Context:
{context}

Question:
{question}
"""

    result = ollama.chat(
        model="llama3",
        messages=[
            {"role":"user","content":prompt}
        ]
    )

    st.subheader("Answer")
    st.write(result["message"]["content"])

    st.subheader("Sources")

    for doc in docs:
        st.write(
            doc.metadata.get("source"),
            "page:",
            doc.metadata.get("page")
        )
