from agents.agent_service import runAgent
from models.user_input import ChatbotPrompt


def chatbot_prompt(data: ChatbotPrompt):
    return runAgent(data)
