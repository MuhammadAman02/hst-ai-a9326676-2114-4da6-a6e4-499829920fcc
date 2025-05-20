import os
import openai
from typing import List
from app.models.conversation import Message, Conversation
from app.core.logging_config import get_logger

logger = get_logger(__name__)

class ChatbotService:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.model = "gpt-3.5-turbo"
        self.system_message = (
            "You are a helpful medical assistant. Provide accurate and helpful "
            "information, but always advise users to consult with a qualified healthcare "
            "professional for personalized medical advice, diagnosis, or treatment."
        )

    async def get_response(self, conversation: Conversation) -> str:
        messages = [{"role": "system", "content": self.system_message}]
        messages.extend([{"role": m.role, "content": m.content} for m in conversation.messages])

        try:
            response = await openai.ChatCompletion.acreate(
                model=self.model,
                messages=messages,
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.7,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logger.error(f"Error getting response from OpenAI: {str(e)}")
            return "I'm sorry, but I'm having trouble generating a response right now. Please try again later."

chatbot_service = ChatbotService()