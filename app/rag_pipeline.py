from retriever.faiss_retriever import retrieve_documents
from prompts.rag_prompt import build_rag_prompt
from llm.llm_loader import load_llm

class RAGPipeline:
    def __init__(self):
        # load LLM
        print("Loading LLM...")
        self.llm = load_llm()
        print("RAG pipeline ready\n")

    def build_context(self, docs):
        """
        Combine retrieved documents into context
        """
        context = "\n\n".join(
            [doc.page_content for doc in docs[:3]]
        )
        return context

    def run(self, question: str):
        print("\nRetrieving documents...")
        # 1 retrieve documents
        docs = retrieve_documents(question)
        if not docs:
            return "Không tìm thấy thông tin trong tài liệu."

        # 2 build context
        context = self.build_context(docs)

        # debug (optional)
        print("\nRETRIEVED CONTEXT\n")
        print(context[:1000])
        print("\n")

        # 3 build prompt
        prompt = build_rag_prompt(context, question)

        # 4 run LLM
        print("Generating answer...\n")
        answer = self.llm.invoke(prompt)
        return answer