from modules.category import Category
from modules.course import Course


class Courses:
    availableCourses: dict

    def __init__(self) -> None:
        self.availableCourses = {}

    def getCategories(self):
        return list(self.availableCourses.keys())

    def getCourses(self, category: Category):
        return self.availableCourses[category]

    def addCourse(self, course: Course):
        if course.category in self.availableCourses:
            self.availableCourses[course.category].append(course)
            return
        self.availableCourses[course.category] = [course]
