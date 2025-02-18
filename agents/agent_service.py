from agents.user_agent import getUserAgent
from models.user_input import ChatbotPrompt


def runAgent(data: ChatbotPrompt):
    agent = getUserAgent()
    res = agent.run(data.input)

    return res
