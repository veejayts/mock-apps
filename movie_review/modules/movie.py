from random import randint
from modules.date import Date
from modules.rating import Rating


class Movie:
    def __init__(self, title: str, year_of_release: int, language: str, genre: str):
        self.movie_id = str(randint(100, 100000))
        self.title = title
        self.year_of_release = Date(year_of_release)
        self.language = language
        self.genre = genre
        self.rating = Rating(self.movie_id)

    def update_rating(self, rating: float):
        self.rating.update_rating(rating)
