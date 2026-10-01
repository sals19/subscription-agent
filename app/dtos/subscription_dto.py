from pydantic import BaseModel
from typing import Optional


class SubscriptionDto(BaseModel):
    subscription_id: str
    subscription_name: Optional[str]
    subscription_type: Optional[str]
    plan_id: int
    status: str
    start_date: str
    end_date: Optional[str]