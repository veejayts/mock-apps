from modules.user_type import UserType
from modules.rating import Rating
from modules.user import User


class Admin(User):
    def __init__(self, username, email, password):
        super().__init__(username, email, password)
        self.user_status = UserType.admin

    def approve_rating(self, rating: Rating):
        pass
