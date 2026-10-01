from app.dtos.user_dto import UserDto

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