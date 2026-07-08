import os
import shutil

from app.rag.loader import PDFLoader
from app.rag.splitter import TextSplitter
from app.rag.vector_store import VectorStore


class UploadService:

    def __init__(self):

        self.loader = PDFLoader()

        self.splitter = TextSplitter()

        self.vector_db = VectorStore()

        self.upload_dir = "uploads"

        os.makedirs(self.upload_dir, exist_ok=True)

    def upload_pdf(self, file):

        filepath = os.path.join(
            self.upload_dir,
            file.filename
        )

        with open(filepath, "wb") as buffer:

            shutil.copyfileobj(file.file, buffer)

        documents = self.loader.load_pdf(filepath)

        chunks = self.splitter.split_documents(documents)

        self.vector_db.add_documents(chunks)

        return {
            "message": "Document uploaded successfully."
        }