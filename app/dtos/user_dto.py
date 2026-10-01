from pydantic import BaseModel


class UserDto(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    email: str