from langchain_core.tools import tool

from app.services.service_factory import create_subscription_service
from app.services.subscription_service import SubscriptionService

session, subscription_service = create_subscription_service()

@tool
def get_my_subscription(user_id: str) -> dict:
    """Get susbcription information for the user"""
    user_id_bytes = bytes.fromhex(user_id)
    subscription = subscription_service.get_user_subscription(user_id_bytes)
    if subscription is None:
        return {
            "status": "not_found",
            "message": "Subscription not found."
        }
    return {
        "subscription_id": str(subscription.subscription_id),
        "subscription_name": subscription.subscription_name,
        "subscription_type": subscription.subscription_type,
        "status": subscription.status,
        "plan_id": subscription.plan_id
    }

@tool
def create_subscription(
    user_id: str,
    plan_id: int,
    subscription_name: str,
    subscription_type: str
) -> dict:
    """Create a new subscription for a user."""
    user_id_bytes = bytes.fromhex(user_id)
    subscription = subscription_service.create_subscription(
        user_id=user_id_bytes,
        plan_id=plan_id,
        subscription_name=subscription_name,
        subscription_type=subscription_type
    )

    return {
        "subscription_id": str(subscription.subscription_id),
        "subscription_name": subscription.subscription_name,
        "subscription_type": subscription.subscription_type,
        "status": subscription.status,
        "plan_id": subscription.plan_id
    }

@tool
def cancel_subscription(subscription_id: str) -> dict:
    """Cancel an existing subscription."""

    pass

@tool
def pause_subscription(subscription_id: str) -> dict:
    """Pause an active subscription."""

    pass

@tool
def resume_subscription(subscription_id: str) -> dict:
    """Resume a paused subscription."""

    pass

