from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'My super secret key!'

# Database - sqlite
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskapp.db'

# Database - mysql
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://USERNAME:PASSWORD@csmysql.cs.cf.ac.uk:3306/USERNAME_DATABASE_NAME'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c22012187:Wood283141()DBM@csmysql.cs.cf.ac.uk:3306/c22012187_flaskapp'


db = SQLAlchemy(app)

# Setting bcrypt
bcrypt = Bcrypt(app)

# Addition of login process
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'primary'
# Using decorators to easily remember logins, logouts and sessions.

from flaskapp import routes