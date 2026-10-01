from app.database.connection import SessionLocal
from app.repositories.subscription_repository import SubscriptionRepository
from app.repositories.user_repository import UserRepository
from app.services.subscription_service import SubscriptionService

session = SessionLocal()

user_repository = UserRepository(session)
subscription_repository = SubscriptionRepository(session)
subscription_service = SubscriptionService(user_repository, subscription_repository)
user_id = bytes.fromhex(
    "a7c145f2293f4c9b844f2c862ed62d28"
)
user = subscription_service.get_user_subscription(user_id)
print(user)
session.close()