from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from app.config import OPENAI_API_KEY

from app.tools.subscription_tools import (get_my_subscription, create_subscription, cancel_subscription, resume_subscription, pause_subscription)

tools = [
    get_my_subscription,
    create_subscription,
    cancel_subscription,
    pause_subscription,
    resume_subscription
]

llm = ChatOpenAI(
    model="gpt-5.6",
    temperature=0,
    api_key=OPENAI_API_KEY,
    use_responses_api=True
)

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
    You are a subscription management assistant.
    You help users retrieve information about their subscriptions.
    When the user asks about their subscription, 
    use the get_my_subscription tool.
    Never invent subscription information.
    Never claim an operation succeeded unless the corresponding tool reports success.
    """
)