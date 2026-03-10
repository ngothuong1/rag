from langchain_text_splitters import RecursiveCharacterTextSplitter
from ingestion.pdf_loader import load_pdfs

def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    return chunks

if __name__ == "__main__":
    docs = load_pdfs()
    chunks = split_documents(docs)

    print("Total chunks:", len(chunks))
    print(chunks[0].page_content[:300])