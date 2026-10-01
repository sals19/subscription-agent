from pydantic import BaseModel

class AgentChatRequest(BaseModel):
    user_id: str
    message: str

class AgentChatResponse(BaseModel):
    response: str