from app.agent.agent import agent
from tests.agent_response_extractor import extract_agent_response

def test_agent():

    user_id = "a7c145f2293f4c9b844f2c862ed62d28"

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                    f"My user ID is {user_id}. "
                    "What is my current subscription?"
                )
                }
            ]
        }
    )

    print("\n========== AGENT RESULT ==========")
    print(result)

    print("\n========== FINAL RESPONSE ==========")
    response = extract_agent_response(result)

    assert result is not None