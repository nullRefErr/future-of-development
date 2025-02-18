from fastapi import APIRouter

from controller.chatbot import chatbot_prompt
from models.user_input import ChatbotPrompt

router = APIRouter()


@router.post("/ai/chatbot", tags=["chatbot"])
async def chatbot(data: ChatbotPrompt):
    return chatbot_prompt(data)
