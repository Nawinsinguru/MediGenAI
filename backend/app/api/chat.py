from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user
from app.models.user import User
from app.rag.chat_service import HospitalChatService
from app.schemas.chat_schema import ChatRequest, ChatResponse

router = APIRouter(
    prefix="/chat",
    tags=["Hospital Chat"]
)


@router.post("", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    current_user: User = Depends(get_current_user)
):
    chat_service = HospitalChatService()   # Create only when API is called

    answer = chat_service.ask(request.question)

    return ChatResponse(
        answer=answer
    )