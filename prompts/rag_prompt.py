def build_rag_prompt(context: str, question: str) -> str:
    prompt = f"""
Bạn là trợ lý AI trả lời câu hỏi dựa trên tài liệu PDF trong thư mục data của hệ thống.
### TÀI LIỆU PDF
    {context}
### CÂU HỎI
    {question}
### HƯỚNG DẪN
- Chỉ sử dụng thông tin trong phần TÀI LIỆU PDF ở trên
- Không sử dụng kiến thức bên ngoài
- Trả lời ngắn gọn, đúng trọng tâm
- Nếu tài liệu không chứa câu trả lời, hãy trả lời:
  "Không tìm thấy thông tin trong tài liệu"
### CÂU TRẢ LỜI
"""
    return prompt