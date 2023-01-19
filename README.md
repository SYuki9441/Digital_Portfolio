# Digital Portfolio - flaskapp
## User name - C22012187
Digital portfolios with flask, only signed-up users can post comments.

## How to run code
```bash
$ python run.py
```

## To leave comment, register first
Users need to register and sign in to leave a comment.

### Try as a test user
```bash
Email: TestUser@demo.com
Password: password
```


## Functions in use
- Template inheritance  
New layout.html is created, {% block content %} {% endblock %} implementation content of each screen is plugged in

- Apply Bootstrap  
For new post, post screen, edit/delete screen, etc.

- Apply Flask WTF  
Easily create forms with validation etc. when used

- DB connection processing in SQLAlchemy
- Flask-Bcrypt  
Used to hash passwords, causing the original data values to be converted to random fixed-length values in order to store passwords securely.

- Flask-Login - user session management  
Easily remember logins, logouts and sessions using decorators.

- Pagination functionality using Flask-SQLAlchemy

- Downloading files using the API – CV file


## References

> Coding Market. 2021. *How to create the Responsive Resume UI Design using HTML and CSS -- Resume Design -- CV Design*. Available at: https://www.youtube.com/watch?v=c9Yn20h2Jxw [Accessed: 16 January 2023].

> Danilevich, O. 2020. *[Searched　for "coding"]*. Available at: https://www.pexels.com/ja-jp/photo/4974912/ [Accessed: 18 January 2023].

> Edwards, S. 2015. *Blank Profile Picture*. Available at: https://pixabay.com/vectors/blank-profile-picture-mystery-man-973460/ [Accessed: 18 January 2023].

> Kubów, A. 2021. *Build a Responsive Online Portfolio from scratch!*. Available at: https://www.youtube.com/watch?v=-D6oTPA4vXc&t=4017s [Accessed: 15 January 2023].

> Programming Tutorial. 5-1-2022. *How to create a responsive navigation bar [Introduction to HTML/CSS]*. Available at: https://www.youtube.com/watch?v=feu9m1E4T9E [Accessed: 15 January 2023].

> Schafer, C. 2018. *Python Flask Tutorial: Full-Featured Web App Part 3 - Forms and User Input*. Available at: https://www.youtube.com/watch?v=UIJKdCIEXUQ&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=3 [Accessed: 13 January 2023]

> Schafer, C. 2018. *Python Flask Tutorial: Full-Featured Web App Part 4 - Database with Flask-SQLAlchemy*. Available at: https://www.youtube.com/watch?v=cYWiDiIUxQc&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=4 [Accessed: 13 January 2023]

> Schafer, C. 2018. *Python Flask Tutorial: Full-Featured Web App Part 6 - User Authentication*. Available at: https://www.youtube.com/watch?v=CSHx6eCkmv0&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=6 [Accessed: 13 January 2023]

> Schafer, C. 2018. *Python Flask Tutorial: Full-Featured Web App Part 7 - User Account and Profile Picture*. Available at: https://www.youtube.com/watch?v=803Ei2Sq-Zs&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=7 [Accessed: 14 January 2023]

> Schafer, C. 2018. *Python Flask Tutorial: Full-Featured Web App Part 8 - Create, Update, and Delete Posts*. Available at: https://www.youtube.com/watch?v=u0oDDZrDz9U&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=8 [Accessed: 14 January 2023]

> Schager, C. 2018. *Python Flask Tutorial: Full-Featured Web App Part 9 - Pagination*. Available at: https://www.youtube.com/watch?v=PSWf2TjTGNY&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=9 [Accessed: 14 January 2023]



<!-- 
Surname, INITIAL(S). Year. Title of image. [Online]. [Date accessed]. Available from: URL -->