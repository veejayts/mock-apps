
class Instructor:
    instructorId: str
    courses: list
    rating: float
    ratings: list
    name: str

    def __init__(self, name: str, globalCourseListing: Courses):
        self.name = name
        self.globalCourseListing = globalCourseListing
        self.courses = []
        self.ratings = []

    def getUploadedCourses(self):
        return self.courses

    def addCourse(self, course: Course):
        self.courses.append(course)
        self.globalCourseListing.addCourse(course)

    def updatePrice(self, course: Course, price: float):
        course.updatePrice(price)

    def getQuestions(self, course: Course):
        course.getQuestions()

    def answerQuestion(self, course: Course, discussion: DiscussionThread, qNumber: int, answer: str):
        course.answerQuestion(course, discussion, qNumber, answer)
