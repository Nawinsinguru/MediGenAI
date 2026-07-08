from app.rag.loader import PDFLoader
from app.rag.splitter import TextSplitter
from app.rag.vector_store import VectorStore

loader = PDFLoader()
splitter = TextSplitter()
vector_db = VectorStore()

documents = loader.load_pdf("sample.pdf")

chunks = splitter.split_documents(documents)

vector_db.add_documents(chunks)

print("=" * 50)
print("Documents added successfully.")
print("=" * 50)

results = vector_db.similarity_search(
    "What are the visiting hours?"
)

print()

for i, doc in enumerate(results, start=1):
    print(f"Result {i}")
    print("-" * 40)
    print(doc.page_content[:400])
    print()