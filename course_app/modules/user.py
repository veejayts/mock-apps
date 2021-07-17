from modules.question import Question
from modules.instructor import Instructor
from modules.course import Course
from random import randint


class User:
    uid: str
    purchasedCourses: dict
    questionsPosted: list
    ratingsGiven: list
    uname: str
    password: str

    def __init__(self, uname, password) -> None:
        self.uid = str(randint(100, 10000))
        self.uname = uname
        self.password = password
        self.purchasedCourses = {}
        self.questionsPosted = []
        self.ratingsGiven = []

    def buyCourse(self, course: Course):
        if course.category not in self.purchasedCourses:
            self.purchasedCourses[course.category] = [course]
            return
        if course in self.purchasedCourses[course.category]:
            print('Already bought')
            return
        self.purchasedCourses[course.category].append(course)

    def viewPurchasedCourseCategories(self):
        return list(self.purchasedCourses.keys())

    def viewPurchasedCourses(self, category):
        return self.purchasedCourses[category]

    def addQuestion(self, course: Course, question: str):
        discussion = course.addQuestion(question)
        self.questionsPosted.append(discussion)

    def getDiscussion(self, course: Course):
        return course.getDiscussion()

    def rateInstructor(self, instructor: Instructor, rating: float):
        instructor.addRating(rating)

    def rateCourse(self, course: Course, rating: float):
        course.addRating(rating)
