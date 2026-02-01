from endee import Endee
from sentence_transformers import SentenceTransformer

# Initialize Endee vector database
db = Endee("rag_db")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read documents
with open("data/docs.txt", "r") as file:
    documents = file.read().split("\n\n")

# Store documents in Endee
for idx, doc in enumerate(documents):
    embedding = model.encode(doc).tolist()
    db.insert(
        id=str(idx),
        vector=embedding,
        metadata={"text": doc}
    )

print("Documents stored successfully in Endee")
