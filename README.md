 # RAG PDF Chatbot

An AI chatbot that answers questions from PDF documents using Retrieval Augmented Generation (RAG).

## Overview

This project implements a RAG pipeline:

PDF Documents
↓
Text Extraction
↓
Chunking
↓
Embeddings
↓
Vector Database
↓
Retriever
↓
LLM Response


## Features

- PDF document processing
- Text chunking with overlap
- Semantic search using embeddings
- Vector database storage
- LLM based answers
- Source/page references


## Tech Stack

- Python
- LangChain
- ChromaDB
- Sentence Transformers
- Ollama
- Streamlit


## Installation

Clone repository:

git clone https://github.com/Yavitbehl/rag-pdf-chatbot.git


Install dependencies:

pip install -r requirements.txt


## Usage

1. Add PDF files inside the pdfs folder

2. Create vector database:

python ingest.py


3. Run chatbot:

streamlit run app.py


## Architecture

User Question
↓
Embedding Model
↓
Vector Search
↓
Relevant PDF Chunks
↓
LLM
↓
Final Answer


## Future Improvements

- OCR support for scanned PDFs
- Better evaluation metrics
- Deployment using Docker
