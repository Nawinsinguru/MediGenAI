from langchain_chroma import Chroma

from app.rag.embeddings import EmbeddingModel


class VectorStore:

    def __init__(self):
        self.embedding = EmbeddingModel().get_embeddings()

        self.db = Chroma(
            persist_directory="vector_db",
            embedding_function=self.embedding,
        )

    def add_documents(self, documents):
        self.db.add_documents(documents)

    def similarity_search(self, query, k=4):
        return self.db.similarity_search(query, k=k)