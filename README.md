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
> Account.html  Edwards, S. 2015. *Blank Profile Picture*. Available at: https://pixabay.com/vectors/blank-profile-picture-mystery-man-973460/ [Accessed: 18 January 2023].

> Danilevich, O. 2020. *[Searched　for "coding"]*. Available at: https://www.pexels.com/ja-jp/photo/4974912/ [Accessed: 18 January 2023].

<!-- 
Surname, INITIAL(S). Year. Title of image. [Online]. [Date accessed]. Available from: URL -->