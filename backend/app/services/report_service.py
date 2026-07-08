import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


class ReportService:

    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def generate_report(
        self,
        patient_name,
        age,
        gender,
        findings,
    ):

        prompt = f"""
You are an experienced radiologist.

Generate a professional preliminary radiology report.

Patient Information

Name: {patient_name}

Age: {age}

Gender: {gender}

Clinical Findings:

{findings}

Return the report using exactly this format.

Title

Clinical Information

Findings

Impression

Recommendation

Write in professional medical language.

Do not invent patient history beyond the supplied findings.
"""

        response = self.model.generate_content(prompt)

        return response.text