from app.rag_pipeline import RAGPipeline

def main():
    print("RAG application...\n")
    rag = RAGPipeline()
    print("Type 'exit' to quit\n")
    while True:
        question = input("User: ")
        if question.lower() in ["exit", "quit"]:
            print("Exiting...")
            break

        answer = rag.run(question)
        print("\nAssistant:")
        print(answer)
        print("\n" + "-" * 60 + "\n")

if __name__ == "__main__":
    main()