# Endee RAG AI Project

## Project Overview
This project implements a Retrieval Augmented Generation (RAG) based Question Answering system using Endee as the vector database. The system retrieves relevant document content using semantic search and generates accurate answers using an LLM.

## Problem Statement
Traditional keyword-based search systems fail to understand semantic meaning. This project solves that problem by using vector embeddings and similarity search to retrieve relevant context before generating responses.

## System Design / Technical Approach
1. Documents are stored in a text file
2. Each document is converted into vector embeddings
3. Embeddings are stored in Endee vector database
4. User queries are converted into embeddings
5. Endee retrieves semantically similar documents
6. An LLM generates the final answer using retrieved context

## How Endee is Used
Endee is used as the vector database to:
- Store document embeddings
- Perform semantic similarity search
- Retrieve relevant context for RAG-based answering

## Tech Stack
- Python
- Endee (Vector Database)
- SentenceTransformers
- OpenAI API

## Setup Instructions
```bash
pip install -r requirements.txt

