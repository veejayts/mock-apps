MOVIE REVIEW PLATFORM
Build a movie review platform that collects reviews for movies from its users
and later uses the reviews to derive insights which help in providing better recommendations.

The platform should have the following capabilities:

- Add a user:
- Platform by default on-boards a user as a ‘viewer’.
- Captures username, password, and email id of user.
- A user in ‘viewer’ category will be upgraded to ‘critic’ category after he/she published reviews for more than movies. (Reviews of critics will be captured with higher weightage.)
- Add a movie:
- Captures the below details.
- Title
- Year of release
- Language
- Genre
- A movie can be added by a viewer/critic or the admin.
- A movie added by a user is published on the platform only after the submission is approved by the admin. (Good to have).

- Review a movie:

  - User can review a movie only once.
  - Users can only review Movies which have been released so far, they cannot review upcoming movies.
  - Users can give a review-score between 1 to 10. (Higher the score the better the liking for the movie).
  - User cannot Update/Delete their Review
  - List all reviews given by a User
  - List top n movies by total review score for a:
  - particular year of release
  - genre

- Rating for a movie:
- Weighted average of ratings given by users.
- Viewer’s rating will be considered as such, critic’s rating will have higher weightage(2x)

NEW

- List top n movies by total review score based on combination of pivots:

- Pivots: [Year of release, User category, Genre]

- Suggest related movies based on ratings given by the user.

- Ability to update/ delete a review.
