from repository.db import save_message, get_messages


def send_message(from_id: str, to_id: str, message: str):
    save_message(from_id, to_id, message)
    return {"message": "Message sent successfully!"}


def getMessages(from_id: str, to_id: str):
    my_messages = get_messages(from_id, to_id)
    their_messages = get_messages(to_id, from_id)

    sorted_messages = sorted(my_messages + their_messages, key=lambda x: x["created_at"])
    return {"messages": sorted_messages}
