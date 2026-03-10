from langchain_community.vectorstores import FAISS
import os
from embeddings.embedding_model import load_embedding_model
from ingestion.pdf_loader import load_pdfs
from ingestion.text_splitter import split_documents

FAISS_PATH = "vectordb/faiss_index"

def build_vector_db():

    print("Loading PDFs...")
    documents = load_pdfs()

    print("Splitting documents...")
    chunks = split_documents(documents)

    print("Loading embedding model...")
    embedding = load_embedding_model()
    print("Creating FAISS index...")

    vectordb = FAISS.from_documents(
        chunks,
        embedding
    )

    os.makedirs(FAISS_PATH, exist_ok=True)
    vectordb.save_local(FAISS_PATH)
    print("FAISS index saved!")

if __name__ == "__main__":
    build_vector_db()