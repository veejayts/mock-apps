from modules import category
from modules import instructor
from modules import course
from modules.category import Category
from modules.course import Course
from modules.user import User
from modules.courses import Courses
from modules.instructor import Instructor


class App:
    courses: Courses
    instructors: dict
    users: dict

    def __init__(self) -> None:
        self.courses = Courses()
        self.instructors = {}
        self.users = {}
        self.currentUser = None

        self.login()

    def login(self):
        choice = 1

        while(choice != 0):
            # try:
            print()
            print('0. Exit')
            print('1. Login as user')
            print('2. Login as instructor')
            print('3. Register as user')
            print('4. Register as instructor')
            choice = int(input('Enter your choice: '))

            uname = input('Enter the user name: ')
            password = input('Enter the password: ')

            if choice == 1:
                if len(self.users) == 0 or uname not in self.users or self.users[uname].password != password:
                    print('Invalid user credentials')
                    continue
                self.currentUser = self.users[uname]
                self.runAsUser()

            elif choice == 2:
                if len(self.instructors) == 0 or uname not in self.instructors or self.instructors[uname].password != password:
                    print('Invalid user credentials')
                    continue
                self.currentUser = self.instructors[uname]
                self.runAsInstructor()

            elif choice == 3:
                if uname not in self.users:
                    user = User(uname, password)
                    self.users[user.uname] = user
                    self.currentUser = user
                else:
                    print('User already exists')

            elif choice == 4:
                if uname not in self.instructors:
                    instructor = Instructor(uname, password)
                    self.instructors[instructor.uname] = instructor
                    self.currentUser = instructor
                else:
                    print('User already exists')
            # except:
            #     print('exception occurred')
            #     continue

    def logout(self):
        pass

    def runAsInstructor(self):
        choice = 1

        while(choice != 6):
            print('\n1. Add Course\n2. Update Price\n3. Get Discussion\n4. Answer Question\n5. Show uploaded courses\n6. Logout')
            choice = int(input())

            if choice == 1:
                name = input('Enter the name: ')
                price = float(input('Enter the price: '))
                category = input('Enter the category: ')
                newCourse = Course(name, price, category, self.currentUser)

                self.currentUser.addCourse(newCourse)
                self.courses.addCourse(newCourse)

            elif choice == 2:
                uploadedCourses = self.currentUser.getUploadedCourses()

                if len(uploadedCourses) == 0:
                    print('No courses uploaded')
                    continue

                for idx, course in enumerate(uploadedCourses):
                    print(str(idx + 1) + ' ' + course.name)

                cNumber = int(input('Enter the course number: '))

                if cNumber > len(uploadedCourses):
                    print('Invalid input')
                else:
                    price = float(input('Enter new price: '))
                    self.currentUser.updatePrice(
                        uploadedCourses[cNumber - 1], price)

            elif choice == 3:
                uploadedCourses = self.currentUser.getUploadedCourses()

                if len(uploadedCourses) == 0:
                    print('No courses uploaded')
                    continue

                for idx, course in enumerate(uploadedCourses):
                    print(str(idx + 1) + ' ' + course.name)

                cNumber = int(input('Enter the course number: '))

                if cNumber > len(uploadedCourses):
                    print('Invalid input')
                else:
                    discussion = self.currentUser.getDiscussion(
                        uploadedCourses[cNumber - 1])
                    for qNo, d in enumerate(discussion):
                        print(str(qNo + 1) + '\n' + '\tQ: ' +
                              d + '\n\tA: ' + discussion[d])

            elif choice == 4:
                uploadedCourses = self.currentUser.getUploadedCourses()

                if len(uploadedCourses) == 0:
                    print('No courses uploaded')
                    continue

                for idx, course in enumerate(uploadedCourses):
                    print(str(idx + 1) + ' ' + course.name)

                cNumber = int(input('Enter the course number: '))

                if cNumber > len(uploadedCourses):
                    print('Invalid input')
                else:
                    print()
                    print('The questions present are the following:')

                    discussion = self.currentUser.getDiscussion(
                        uploadedCourses[cNumber - 1])
                    ques = []

                    if len(discussion) == 0:
                        print('No questions present')
                        continue

                    for qNo, d in enumerate(discussion):
                        print(str(qNo + 1) + '\n' + 'Q: ' + d)
                        ques.append(d)

                    print('Enter the question number you want to answer: ')
                    qNumber = int(input())

                    if qNumber > len(discussion):
                        print('Invalid input')
                    else:
                        print('Enter the answer: ')
                        answer = input()
                        self.currentUser.answerQuestion(
                            uploadedCourses[cNumber - 1], ques[qNumber - 1], answer)

            elif choice == 5:
                uploadedCourses = self.currentUser.getUploadedCourses()
                for idx, course in enumerate(uploadedCourses):
                    print(str(idx + 1) + ' ' + course.name)

            elif choice == 6:
                self.logout()
                return

    def runAsUser(self):
        choice = 1

        while(choice != 6):
            print('\n1. Categories and courses\t 2. View purchased courses\t 6. Exit')
            choice = int(input('Enter choice: '))
            if choice == 1:
                print('Categories:')
                categories = self.courses.getCategories()

                if len(categories) == 0:
                    print('No categories available')
                    continue

                for idx, category in enumerate(categories):
                    print(str(idx + 1) + ' ' + category)

                cNumber = int(
                    input('Enter category number to view or 0 to go to main menu: '))

                if cNumber == 0:
                    continue

                print('Courses in Category')
                courses = self.courses.getCourses(categories[cNumber - 1])

                if len(courses) == 0:
                    print('No courses available')
                    continue

                for idx, course in enumerate(courses):
                    print(str(idx + 1) + ' ' + str(course.getCourseInfo()))

                cNumber = int(
                    input('Enter course number to view options or \nEnter 0 to go to main menu: '))

                if cNumber == 0:
                    continue

                c = int(input('\n 1. Buy course: '))

                if c == 1:
                    self.currentUser.buyCourse(courses[cNumber - 1])
                    continue

            if choice == 2:
                print('Courses bought')
                categories = self.currentUser.viewPurchasedCourseCategories()

                if len(categories) == 0:
                    print('No purchased courses')
                    continue

                categoryNumber = self.selectCategory(categories)

                courseList = self.currentUser.viewPurchasedCourses(
                    categories[categoryNumber - 1])

                if len(courseList) == 0:
                    print('No purchased courses')
                    continue

                courseNumber = self.selectCourse(courseList)

                print(
                    '\n1. Rate course\n 2. Rate instructor\n 3. Ask Question\n 4. View Discussion: ')

                ch = int(input())

                if ch == 1:
                    rating = float(input('Enter the rating: '))
                    self.currentUser.rateCourse(
                        courseList[courseNumber - 1], rating)
                elif ch == 2:
                    rating = float(input('Enter the rating: '))
                    self.currentUser.rateInstructor(
                        courseList[courseNumber - 1].instructor, rating)
                elif ch == 3:
                    question = input('Enter the question: ')
                    self.currentUser.addQuestion(
                        courseList[courseNumber - 1], question)
                elif ch == 4:
                    print(self.currentUser.getDiscussion(
                        courseList[courseNumber - 1]))

    def selectCourse(self, courseList: list):
        isValid = False

        while not isValid:
            for idx, course in enumerate(courseList):
                print(str(idx + 1) + '. ' + str(course.getCourseInfo()))

            courseNumber = int(input('Enter the course number: '))

            if courseNumber > len(courseList):
                print('Invalid choice')
                continue
            isValid = True

            return courseNumber

    def selectCategory(self, categoryList: list):
        isValid = False

        while not isValid:
            for idx, category in enumerate(categoryList):
                print(str(idx + 1) + '. ' + category)

            categoryNumber = int(input('Enter the category number: '))

            if categoryNumber > len(categoryList):
                print('Invalid choice')
                continue
            isValid = True

        return categoryNumber


App()
