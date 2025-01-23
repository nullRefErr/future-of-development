from smolagents import LiteLLMModel, tool, ToolCallingAgent
import requests

model = LiteLLMModel(
    model_id="ollama/qwen2.5-coder:14b",
    api_base="http://localhost:11434",  # replace with remote open-ai compatible server if necessary
)
model.verbose = True

@tool
def fetch_webpage(url: str) -> str:
    """
    Fetches content from a webpage.

    Args:
        url: The complete URL of the webpage to fetch (e.g., https://example.com)
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"Error fetching page: {str(e)}"

agent = ToolCallingAgent(tools=[fetch_webpage], model=model)

print(agent.run("fetch the content from https://dev.to"))
