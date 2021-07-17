from hashlib import new
from modules.movie import Movie
from modules.date import Date
from modules.user_type import UserType
from modules.admin import Admin
from modules.user import User


class App:
    def __init__(self):
        self.movies = {}
        self.users = {}
        self.unapproved_movies = []
        self.current_user = None

        # t = Movie('code', 2019, 'en', 'action')
        # self.movies[t.movie_id] = t
        # t = Movie('code 2', 2019, 'en', 'romance')
        # self.movies[t.movie_id] = t

        self.run()

    def println(self, val):
        print()
        print(val)

    def login(self, username: str, email: str, password: str):
        if username not in self.users:
            self.println('User does not exist')
            return False

        if password == self.users[username].password:
            self.println('User logged in')
            self.current_user = self.users[username]
            return True

    def register(self, username: str, email: str, password: str, admin=False):
        if username in self.users:
            self.println('User already exists!')
            return False

        if admin:
            self.users[username] = Admin(username, email, password)
        else:
            self.users[username] = User(username, email, password)

        return True

    def run(self):
        try:
            choice = 0
            while choice != 10:
                self.current_user = None
                if choice == 10:
                    break

                self.println('1. Log in\n2. Register\n3. Register admin')
                choice = int(input('Enter your choice: '))

                username = input('Enter your username: ')
                password = input('Enter your password: ')

                if choice == 1:
                    is_valid = self.login(username, None, password)
                    if not is_valid:
                        continue

                elif choice == 2:
                    email = input('Enter your email: ')
                    is_valid = self.register(username, email, password)
                    continue

                elif choice == 3:
                    email = input('Enter your email: ')
                    is_valid = self.register(username, email, password, True)
                    continue

                if self.current_user != None:
                    if self.current_user.user_status == UserType.admin:
                        ch = 0

                        while ch != 10:
                            if ch == 10:
                                self.current_user = None
                                break

                            self.println('1. Approve movies\n10. Exit')
                            ch = int(input('Enter your choice: '))

                            if ch == 1:
                                if len(self.unapproved_movies) == 0:
                                    self.println('No unapproved movies')
                                    continue

                                for i, rting in enumerate(self.unapproved_movies):
                                    self.println(
                                        str(i + 1) + ' ' + rting.title + ' ' + str(rting.year_of_release.year) + ' ' + rting.genre)

                                movie_num = int(
                                    input('Enter the movie number to approve: '))

                                if movie_num < 1 or movie_num > len(self.unapproved_movies):
                                    self.println('Invalid choice')
                                    continue

                                self.movies[self.unapproved_movies[movie_num -
                                                                   1].movie_id] = self.unapproved_movies[movie_num - 1]

                                self.unapproved_movies.pop(movie_num - 1)

                            else:
                                continue

                    else:
                        ch = 0

                        while ch != 10:
                            if ch == 10:
                                self.current_user = None
                                break

                            self.println(
                                '1. View movies\n2. Add movie\n3. Reviews by me')
                            ch = int(input('Enter your choice: '))

                            if ch == 1:
                                num = int(
                                    input('Enter the number of movies you want to list: '))

                                if num < 0:
                                    self.println('Invalid number')
                                    continue

                                sort_choice = int(input(
                                    'Sort by\n\t1. Genre\n\t2. Year\nEnter your choice: '))

                                disp = {}
                                disp_list = []

                                if sort_choice == 1:
                                    sort_by = input('Enter the genre: ')
                                    for mv_id, mv in self.movies.items():
                                        if mv.genre == sort_by:
                                            disp_list.append(mv)

                                elif sort_choice == 2:
                                    sort_by = int(input('Enter the year: '))
                                    for mv_id, mv in self.movies.items():
                                        if mv.year_of_release.year == sort_by:
                                            disp_list.append(mv)

                                else:
                                    self.println('Invalid choice')
                                    continue

                                disp_list.sort(key=lambda x: x.rating.rating)

                                if len(disp_list) == 0:
                                    self.println('No movies matched')
                                    continue

                                for i, mv in enumerate(disp_list):
                                    if i > num:
                                        break
                                    print(str(i + 1) + '. ' + disp_list[i].movie_id + ' ' +
                                          disp_list[i].title + ' ' + disp_list[i].genre + ' ' + str(disp_list[i].rating.rating))

                                self.println('1. Enter rating\n2. Go back')
                                rating_choice = int(
                                    input('Enter your choice: '))

                                if rating_choice == 1:
                                    movie_num = int(
                                        input('Enter the movie number: '))

                                    if movie_num < 0 or movie_num > len(disp_list):
                                        self.println('Invalid choice')
                                        continue

                                    if disp_list[movie_num - 1].year_of_release.year > 2021:
                                        self.println(
                                            'Cannot review future movies')
                                        continue

                                    rating = int(
                                        input('Enter the rating for the movie: '))

                                    success = self.current_user.add_rating(
                                        rating, disp_list[movie_num - 1].movie_id, disp_list[movie_num - 1].year_of_release.year)

                                    if success:
                                        if self.current_user.user_status == UserType.critic:
                                            self.movies[disp_list[movie_num - 1].movie_id
                                                        ].update_rating(rating * 2)
                                        else:
                                            self.movies[disp_list[movie_num -
                                                                  1].movie_id].update_rating(rating)

                                else:
                                    continue

                            elif ch == 2:
                                self.println('Enter the details')
                                title = input('Title: ')
                                year_of_release = int(
                                    input('year_of_release: '))
                                language = input('language: ')
                                genre = input('genre: ')
                                new_movie = Movie(
                                    title, year_of_release, language, genre)

                                self.unapproved_movies.append(new_movie)

                            elif ch == 3:
                                for mv_id, rating in self.current_user.reviews_given.items():
                                    self.println(
                                        self.movies[mv_id].title + ': ' + str(rating))
        except Exception:
            pass


App()
