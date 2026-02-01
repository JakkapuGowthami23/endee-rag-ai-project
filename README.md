# Endee RAG AI Project

## Project Overview

This project implements a **Retrieval Augmented Generation (RAG)** based Question Answering system.  
It allows users to ask questions over a collection of documents and retrieves **accurate answers** using **semantic search** powered by **Endee** as the vector database.  

**Problem Statement:**  
Many organizations have large amounts of unstructured data (documents, manuals, FAQs). Searching manually is slow and error-prone.  
This project provides a fast, automated way to answer questions using the knowledge stored in documents.

---

## System Design / Technical Approach

The system works in the following stages:

1. **Data Ingestion**
   - Documents are stored in the `data/` folder.
   - `ingest.py` reads documents and converts them into vector embeddings.

2. **Vector Storage**
   - Endee is used as the **vector database** to store embeddings.
   - This allows **semantic search** over the documents.

3. **Query Handling**
   - `query.py` receives a user query.
   - Converts the query into a vector and searches Endee for the top-K relevant documents.
   - The retrieved documents are passed to a **Language Model (LLM)** to generate accurate answers.

4. **RAG (Retrieval Augmented Generation)**
   - Combines the retrieved kno
