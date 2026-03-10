from langchain_community.document_loaders import PyPDFLoader
import os

DATA_PATH = "data"

def load_pdfs():

    documents = []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".pdf"):
            file_path = os.path.join(DATA_PATH, file)
            loader = PyPDFLoader(file_path)
            docs = loader.load()
            documents.extend(docs)

    return documents

if __name__ == "__main__":

    docs = load_pdfs()

    print("Total documents:", len(docs))
    print(docs[0].page_content[:500])
    print(docs[0].metadata)