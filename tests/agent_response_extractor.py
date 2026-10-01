def extract_agent_response(result):

    message = result["messages"][-1]

    if isinstance(message.content, str):
        return message.content

    return "".join(
        item["text"]
        for item in message.content
        if item.get("type") == "text"
    )