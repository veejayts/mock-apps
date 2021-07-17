
from modules.user_type import UserType
from modules.date import Date
from random import randint


class User:
    def __init__(self, username: str, email: str, password: str):
        self.uid = str(randint(100, 100000))
        self.user_status = UserType.viewer
        self.username = username
        self.email = email
        self.password = password
        self.reviews_given = {}

    def add_rating(self, rating: float, movie_id: str, year: int):
        if rating < 1 or rating > 10:
            self.println('Invalid rating: must be between 1 and 10')
            return False

        if movie_id in self.reviews_given:
            print('Cannot change review of a movie which has already been reviewed')
            return False

        if year > 2021:
            print('Cannot review movies which have not been released yet')
            return False

        if len(self.reviews_given) > 3:
            if self.user_status != UserType.critic:
                self.upgrade_status()

        self.reviews_given[movie_id] = rating

        return True

    def add_movie(self, title: str, year_of_release: Date, language: str, genre: str):
        pass

    def upgrade_status(self):
        self.user_status = UserType.critic
