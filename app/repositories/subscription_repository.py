
import uuid

from app.models.Subscriptions import Subscriptions
from app.models.Users import Users


class SubscriptionRepository:

    def __init__(self, session):
        self.session = session

    def get_by_user_id(self, user_id):
        if type(user_id) == 'str':
            user_id = bytes.fromhex(user_id)
        return (
            self.session.query(Subscriptions)
            .filter(Subscriptions.user_id == user_id)
            .first()
        )

    def create_subscription(self, user_id: str,
    plan_id: int,
    subscription_name: str,
    subscription_type: str):
        newSubscription = Subscriptions()
        newSubscription.subscription_id = uuid.uuid4().bytes
        newSubscription.user_id = user_id
        newSubscription.plan_id = plan_id
        newSubscription.subscription_name = subscription_name
        newSubscription.subscription_type = subscription_type
        self.session.add(newSubscription)
        self.session.commit()
        self.session.refresh(newSubscription)
        return newSubscription
