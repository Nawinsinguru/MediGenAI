from fastapi import APIRouter, UploadFile, File, Depends

from app.auth.dependencies import get_current_user
from app.models.user import User
from app.services.upload_service import UploadService

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

service = UploadService()


@router.post("/pdf")
def upload_pdf(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user)
):

    return service.upload_pdf(file)