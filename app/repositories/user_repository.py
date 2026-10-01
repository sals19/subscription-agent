
from app.models.Users import Users


class UserRepository:

    def __init__(self, session):
        self.session = session

    def get_by_id(self, user_id):
        return self.session.get(Users, user_id)

    def get_by_email(self, email):
        return (
            self.session.query(Users)
            .filter(Users.email == email)
            .first()
        )

    def create(self, user):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
    