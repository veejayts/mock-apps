# javaCourse = Course('Java', 10, javaCategory, javaInstructor)
# pythonCourse = Course('Python', 20, pythonCategory, pythonInstructor)

# # test add course
# print('Adding courses')

# javaInstructor.addCourse(javaCourse)
# pythonInstructor.addCourse(pythonCourse)

# print()

# # in courses
# print('Categories')
# for course in courses.getCategories():
#     print(course.category)

# print()
# print('Courses in java')
# for course in courses.getCourses(javaCategory):
#     print(course.getCourseInfo())

# print()
# print('Courses in python')
# for course in courses.getCourses(pythonCategory):
#     print(course.getCourseInfo())

# print()
# print('Courses uploaded by python instructor')
# for course in pythonInstructor.getUploadedCourses():
#     print(course.getCourseInfo())

# #  test update price
# print('Updating price of python course')
# pythonInstructor.updatePrice(pythonCourse, 0)

# for course in pythonInstructor.getUploadedCourses():
#     print(course.getCourseInfo())

# print()
# print('Discussion present in the python course')
# print(pythonInstructor.getQuestions(pythonCourse))

# print()
# print('User adds a question')
# user.addQuestion(pythonCourse, 'Question about python')

# print(user.getDiscussion(pythonCourse))

# print()
# print('User w no Purchase')
# print(user.viewPurchasedCourses())
# print('User after Purchase')
# user.buyCourse(pythonCourse)
# print(user.viewPurchasedCourses())

# print()
# print('User1 rating the instructor: 3')
# print('User1 rating the instructor: 5')
# user.rateInstructor(pythonInstructor, 3)
# user2.rateInstructor(pythonInstructor, 5)

# print()
# print('Get rating from instructor obj')
# print(pythonInstructor.rating)

# print()
# print('Instructor answering question')
# print()
# print('Before')
# print(pythonInstructor.getQuestions(pythonCourse))
# pythonInstructor.answerQuestion(
#     pythonCourse, user, 1, 'This is the answer to the question')
# print('After')
# print(pythonInstructor.getQuestions(pythonCourse))
