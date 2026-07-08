from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user
from app.models.user import User
from app.schemas.report_schema import (
    ReportRequest,
    ReportResponse,
)
from app.services.report_service import ReportService

router = APIRouter(
    prefix="/reports",
    tags=["Medical Report"]
)

service = ReportService()


@router.post(
    "/generate",
    response_model=ReportResponse
)
def generate_report(
    request: ReportRequest,
    current_user: User = Depends(get_current_user)
):

    report = service.generate_report(
        request.patient_name,
        request.age,
        request.gender,
        request.findings,
    )

    return ReportResponse(
        report=report
    )