from pydantic import BaseModel, Field


class ChatbotPrompt(BaseModel):
    input: str = Field(min_length=1)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "input": "I want this number to be blocked"
                }
            ]
        }
    }
