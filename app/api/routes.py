from fastapi import APIRouter
from .chatbot_routes import router as chatbot_router

router = APIRouter()

router.include_router(chatbot_router, prefix="/chatbot", tags=["chatbot"])

@router.get('/ping')
async def ping_pong():
    """A simple ping endpoint."""
    return {"message": "pong!"}