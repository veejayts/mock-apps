class Rating:
    def __init__(self, movie_id: str):
        self.movie_id = movie_id
        self.rating = 0
        self.ratings_list = []

    def update_rating(self, rating: float):
        self.ratings_list.append(rating)
        self.rating = sum(self.ratings_list) / len(self.ratings_list)
