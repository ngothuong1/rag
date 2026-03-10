import os
from langchain_community.vectorstores import FAISS
from embeddings.embedding_model import load_embedding_model

# Đường dẫn tới FAISS index
FAISS_INDEX_PATH = "vectordb/faiss_index"

def load_vectordb():
    """
    Load FAISS vectorstore từ disk
    """
    if not os.path.exists(FAISS_INDEX_PATH):
        raise ValueError(
            f"FAISS index not found at {FAISS_INDEX_PATH}. "
            "Please run: python -m ingestion.build_faiss"
        )
    print("Loading embedding model...")
    embeddings = load_embedding_model()

    print("Loading FAISS index...")
    vectordb = FAISS.load_local(
        FAISS_INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )
    print("FAISS index loaded successfully")
    return vectordb

def load_retriever(k: int = 5, fetch_k: int = 12, saerch_type: str = "mmr", lambda_mult: float = 0.5):
    """
    Tạo retriever từ FAISS vectorstore
    """
    vectordb = load_vectordb()
    retriever = vectordb.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k, "fetch_k": fetch_k, "lambda_mult": lambda_mult}
    )
    return retriever

def retrieve_documents(query: str, k: int = 5):
    """
    Retrieve top-k documents liên quan tới query
    """
    retriever = load_retriever(k)
    docs = retriever.invoke(query)
    return docs

if __name__ == "__main__":
    print("Initializing FAISS retriever...")
    query = input("\nEnter your question: ")
    docs = retrieve_documents(query, k=5)
    print("\nTop retrieved documents:\n")
    for i, doc in enumerate(docs, 1):
        print(f"Document {i}:")
        print(doc.page_content)
        print("-" * 60)