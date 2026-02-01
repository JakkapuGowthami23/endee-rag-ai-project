from endee import Endee
from sentence_transformers import SentenceTransformer
import openai

# Initialize Endee database
db = Endee("rag_db")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Take user question
question = input("Ask a question: ")

# Convert question to embedding
query_embedding = model.encode(question).tolist()

# Search relevant documents from Endee
results = db.search(query_embedding, top_k=2)

# Build context from retrieved docs
context = " ".join([r["metadata"]["text"] for r in results])

prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{question}
"""

# Generate answer using LLM
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

print("\nAnswer:")
print(response["choices"][0]["message"]["content"])
