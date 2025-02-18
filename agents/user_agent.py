from smolagents import LiteLLMModel, tool, CodeAgent

from services.user_service import getPhoneNumberInfo, getIdInfo, getStatus, getTrustScore, blockNumber

model = LiteLLMModel(
    model_id="ollama/llama3.1:8b",
    api_base="http://localhost:11434",
)
model.verbose = True


@tool
def get_user_info_by_phone(phone: str) -> dict[str, str, str]:
    """
    Get the current user from database by phone number.

    Args:
        phone: Given phone number to get the user info from database.

    Returns:
        name: Name of the user with the given phone number.
        email: Email of the user with the given phone number.
        phone: Phone number of the user.
    """
    user = getPhoneNumberInfo(phone)
    return user


@tool
def get_user_info_by_id(id: str) -> dict[str, str, str]:
    """
    Get the current user from database by id.

    Args:
        id: Given user id to get the user info from database.

    Returns:
        name: Name of the user with the given phone number.
        email: Email of the user with the given phone number.
        phone: Phone number of the user.
    """

    user = getIdInfo(id)
    return user


@tool
def get_premium_status(id: str) -> dict[str]:
    """
    Get the current user's premium status from database by id.

    Args:
        id: Given id to get the user info from database.

    Returns:
        status: User's premium status PREMIUM or IDLE or NONE
    """
    result = getStatus(id)
    return result


@tool
def get_trust_score_by_id(id: str) -> dict[int]:
    """
    Get the current user's trust score from database by id.

    Args:
        id: Given id to get the user info from database.

    Returns:
        trust_score: Integer value to describe User's performance
    """
    result = getTrustScore(id)
    return result


@tool
def block_number_by_id(id: str, phoneNumber: str) -> str:
    """
    Blocks numbers to call or message to the user.

    Args:
        id: this is the user id who wants to block given phone number.
        phoneNumber: Given phone number to block by id.

    Returns:
        A string message to describe the result of the action.
    """
    result = blockNumber(id, phoneNumber)
    return result["message"]


def getUserAgent():
    agent = CodeAgent(
        max_steps=1,
        tools=[
            get_premium_status,
            get_trust_score_by_id,
            get_user_info_by_id,
            get_user_info_by_phone,
            block_number_by_id
        ],
        model=model,
        additional_authorized_imports=[
            'datetime',
            'math',
            'time',
            'random',
            're',
            'statistics',
            'unicodedata',
            'collections',
            'stat',
            'queue',
            'itertools'
        ]
    )
    return agent
