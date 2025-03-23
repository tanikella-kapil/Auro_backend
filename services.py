from sentence_transformers import SentenceTransformer
import numpy as np

# ✅ Use a free local embedding model from Hugging Face
model = SentenceTransformer('all-MiniLM-L6-v2')  

def generate_embedding(text: str):
    """Generates embeddings for a given text using a local model."""
    return np.array(model.encode(text)).tobytes()  

def retrieve_answer(question: str, docs):
    """Retrieves an answer by finding the most relevant document."""
    doc_texts = [doc.content for doc in docs]
    
    # Simulated response (since OpenAI is removed)
    return f"Answer based on relevant documents: {doc_texts[:1]}"
