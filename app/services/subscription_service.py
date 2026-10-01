from app.dtos.user_dto import UserDto
from app.dtos.subscription_dto import SubscriptionDto


class SubscriptionService:

    def __init__(self, user_repository, subscription_repository):
        self.user_repository = user_repository
        self.subscription_repository = subscription_repository

    def get_user(self, user_id):

        user = self.user_repository.get_by_id(user_id)

        if not user:
            raise ValueError("User not Found")

        return UserDto(
            user_id=user.user_id.hex(),
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email
        )

    def get_user_subscription(self, user_id):

        subscription = self.subscription_repository.get_by_user_id(user_id)

        if not subscription:
            raise ValueError("Subscription not Found")

        return SubscriptionDto(
            subscription_id=subscription.subscription_id.hex(),
            subscription_name=subscription.subscription_name,
            subscription_type=subscription.subscription_type,
            plan_id=subscription.plan_id,
            status=subscription.status,
            start_date=subscription.start_date.isoformat(),
            end_date=(
                subscription.end_date.isoformat()
                if subscription.end_date
                else None
            )
        )

    def create_subscription(self, user_id: str,
    plan_id: int,
    subscription_name: str,
    subscription_type: str):
        subscription = self.subscription_repository.create_subscription(user_id,
    plan_id,
    subscription_name,
    subscription_type)
        return subscription
