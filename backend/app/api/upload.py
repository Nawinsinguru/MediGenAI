from functools import lru_cache
from fastapi import APIRouter, UploadFile, File, Depends

from app.auth.dependencies import get_current_user
from app.models.user import User
from app.services.upload_service import UploadService

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

@lru_cache(maxsize=1)
def get_upload_service():
    return UploadService()


@router.post("/pdf")
def upload_pdf(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user)
):
    return get_upload_service().upload_pdf(file)