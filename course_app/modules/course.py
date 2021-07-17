from modules.question import Question
from modules.discussion_thread import DiscussionThread
from modules.instructor import Instructor
from modules.category import Category


class Course:
    name: str
    price: float
    rating: float
    ratings: list
    category: Category
    instructor: Instructor
    discussions: dict

    def __init__(self, name: str, price: float, category: Category, instructor: Instructor):
        self.name = name
        self.price = price
        self.category = category
        self.instructor = instructor
        self.rating = 0
        self.ratings = []
        self.discussions = {}

    def updatePrice(self, price: float):
        self.price = price

    def addRating(self, rating: float):
        self.ratings.append(rating)
        self.rating = sum(self.ratings) / len(self.ratings)

    def getDiscussion(self):
        return self.discussions

    def addQuestion(self, question: Question):
        if question in self.discussions:
            print('Question already asked')
            return
        self.discussions[question] = 'Unanswered'

    def addAnswer(self, question: str, answer: str):
        if question not in self.discussions:
            print('Question not present')
            return
        self.discussions[question] = answer

    def getCourseInfo(self):
        return {
            'name': self.name,
            'price': self.price,
            'rating': self.rating,
            'category': self.category,
            'instructor': self.instructor,
            'discussions': self.discussions,
        }
