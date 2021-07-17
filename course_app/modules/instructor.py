class Instructor:
    instructorId: str
    courses: list
    rating: float
    ratings: list
    uname: str
    password: str

    def __init__(self, uname: str, password: str):
        self.uname = uname
        self.password = password
        self.courses = []
        self.ratings = []
        self.rating = 0

    def addRating(self, rating: float):
        self.ratings.append(rating)
        self.rating = sum(self.ratings) / len(self.ratings)

    def getUploadedCourses(self):
        return self.courses

    def addCourse(self, course):
        self.courses.append(course)

    def updatePrice(self, course, price: float):
        course.updatePrice(price)

    def getDiscussion(self, course):
        return course.getDiscussion()

    def answerQuestion(self, course, question: str, answer: str):
        course.addAnswer(question, answer)
