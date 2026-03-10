from langchain_community.llms import LlamaCpp

def load_llm():
    llm = LlamaCpp(
        model_path="models/llm/vinallama-7b-chat_q5_0.gguf",
        temperature=0.1,
        max_tokens=1024,
        n_ctx=4096,
        n_batch=512,
        verbose=True
    )
    return llm