from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '5ZN5zi!45QUsGG'
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

from main import routes