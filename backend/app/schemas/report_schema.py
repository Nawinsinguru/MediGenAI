from pydantic import BaseModel


class ReportRequest(BaseModel):
    patient_name: str
    age: int
    gender: str
    findings: str


class ReportResponse(BaseModel):
    report: str