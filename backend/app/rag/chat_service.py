import os

import google.generativeai as genai
from dotenv import load_dotenv

from app.rag.vector_store import VectorStore

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


class HospitalChatService:

    def __init__(self):
        self.vector_db = VectorStore()
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def ask(self, question: str):

        docs = self.vector_db.similarity_search(question)

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
You are an intelligent hospital assistant.

Answer ONLY using the provided hospital documents.

If the answer is not found in the context, reply:

"I couldn't find that information in the hospital documents."

Hospital Documents:

{context}

Question:
{question}

Answer:
"""

        response = self.model.generate_content(prompt)

        return response.text