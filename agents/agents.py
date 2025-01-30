from smolagents import LiteLLMModel, tool, ToolCallingAgent, CodeAgent
import requests

model = LiteLLMModel(
    model_id="ollama/llama3.1:8b",
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


@tool
def getFirstChars(data: str) -> str:
    """
    get first 100 characters from the data

    Args:
        data: The data to get the first 100 characters from
    """
    try:
        return data[:100]
    except Exception as e:
        return f"Parsing 100 chars: {str(e)}"


agent = CodeAgent(
    tools=[fetch_webpage, getFirstChars],
    model=model,
    additional_authorized_imports=['datetime', 'math', 'time', 'random', 're', 'statistics',
                                   'unicodedata', 'collections', 'stat', 'queue', 'itertools']
)

res = agent.run(
    "I want you to run until success and stop. Result will be assigned to a variable. No trash talk. Short and concise answers. You must return the value as 'result'. Fetch the content from https://dev.to then get the first 100 characters then return the result then stop the agent")

print("***********" + res)
