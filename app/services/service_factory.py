from app.database.connection import SessionLocal

from app.repositories.subscription_repository import SubscriptionRepository
from app.repositories.user_repository import UserRepository

from app.services.subscription_service import SubscriptionService


def create_subscription_service():

    session = SessionLocal()

    user_repository = UserRepository(session)

    subscription_repository = SubscriptionRepository(session)

    subscription_service = SubscriptionService(
        user_repository,
        subscription_repository
    )

    return session, subscription_service