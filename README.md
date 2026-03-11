# RAG là gì?

RAG (Retrieval-Augmented Generation) là một phương pháp kết hợp khả năng truy xuất thông tin từ các nguồn dữ liệu bên ngoài (Reatrival) với sức mạnh tạo nội dung của mô hình ngôn ngữ lớn (LLM) 

# RAG hoạt động như thế nào?

1. Indexing (bước chuẩn bị)
- Chia nhỏ tài liệu: chia tài liệu thành các đoạn nhỏ (chunks) để dễ dàng xử lý và tìm kiếm
- Tạo vector embeddings: chuyển đổi văn bản thành vector để máy tính hiểu 
- Lưu vào vector database: Chroma, v.v.

2. Quá trình truy vấn (thời điểm người dùng hỏi)
- Chuyển câu hỏi thành vector (embedding)
- Tìm kiếm ngữ nghĩa: hệ thống so sánh vector của câu hỏi với các vector trong cơ sở dữ liệu để tìm ra những nội dung có ý nghĩa tương tự nhất
- Tạp prompt mở rộng: kết hợp prompt giúp LLM trả lời chính xác hơn
- LLM tạo câu trả lời

# Hệ thống RAG Chatbot

- Mô tả: Hệ thống RAG cho phép LLM trả lời câu hỏi dựa trên nội dung của các tài liệu PDF
- Flow: 
PDF -> Chunk text -> embbeding -> FAISS vectorDB
User hỏi -> embedding câu hỏi -> Similarity Search -> Top chunks -> Prompt -> LLM -> Final Answer
- Các thành phần của hệ thống:
1. Data
rag\data\cauhoicuakh.pdf
rag\data\dkykhtt.pdf
2. PDF Loader
rag\ingestion\pdf_loader.py
Chức năng:
- Đọc các file .pdf
- Chuyển nội dung PDF thành text
3. Text Splitter (Chunking)
rag\ingestion\text_splitter.py
Chức năng:
- Chia tài liệu thành các chunk nhỏ hơn
Lý do: 
- LLM có giới hạn context windown
- Tăng độ chính xác hơn khi tìm kiếm
- Vector search hoạt động tốt hoen với đoạn văn ngắn
4. Build FAISS (Build VectorDB)
rag\ingestion\build_faiss.py
Chức năng:
- Xây dựng vectorDB (FAISS index) 
5. Embedding Model
rag\embeddings\embedding_model.py
- Model sử dụng: all-MiniLM-L6-v2, chuyển văn bản thành vector, chuyển câu hỏi của user thành vector
6. VectorDB (FAISS)
rag\retriver\faiss_retriver.py
- FAISS dùng để: lưu trữ vector embedding, tìm kiếm các vector gần nhất, truy xuất các đoạn văn bản liên quan 
7. Prompt
rag\prompts\rag_prompt.py
8. LLM
rag\llm\llm_loader.py
- Model sử dụng: vinallama-7b-chat_q5_0.gguf
Chức năng: hiểu câu hỏi của người dùng, sử dụng context từ retriver sinh câu trả lời cuối cùng
