from langchain_community.embeddings import HuggingFaceEmbeddings
from functools import lru_cache
import os

EMBEDDING_MODEL_PATH = os.path.join(
    "models",
    "embeddings",
    "all-MiniLM-L6-v2"
)

@lru_cache(maxsize=1)
def load_embedding_model():
    """
    Load embedding model (cached để tránh load nhiều lần)
    """
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_PATH,
        model_kwargs={
            "device": "cpu"   
        },
        encode_kwargs={
            "normalize_embeddings": True
        }
    )
    return embeddings