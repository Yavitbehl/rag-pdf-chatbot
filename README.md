# RAG Chatbot

## Setup

1. Install packages:

pip install -r requirements.txt

2. Add PDFs inside pdfs folder

3. Create vector database:

python ingest.py

4. Install Ollama and run:

ollama pull llama3

5. Start chatbot:

streamlit run app.py

Features:
- PDF ingestion
- Chunking
- Open source embeddings
- Vector database
- RAG answering
- Source citations
