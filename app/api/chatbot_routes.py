from fastapi import APIRouter, HTTPException
from app.models.conversation import Conversation, Message
from app.services.chatbot_service import chatbot_service
import uuid

router = APIRouter()

@router.post("/chat", response_model=Message)
async def chat(conversation: Conversation):
    if not conversation.id:
        conversation.id = str(uuid.uuid4())
    
    if not conversation.messages:
        raise HTTPException(status_code=400, detail="Conversation must contain at least one message")
    
    user_message = conversation.messages[-1]
    if user_message.role != "user":
        raise HTTPException(status_code=400, detail="Last message must be from the user")

    response_content = await chatbot_service.get_response(conversation)
    response_message = Message(content=response_content, role="assistant")
    
    return response_message