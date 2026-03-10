from embeddings.embedding_model import load_embedding_model
embedding = load_embedding_model()
vector = embedding.embed_query("Tôi muốn mua hàng tại công ty")
print(len(vector))