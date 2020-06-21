from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
cors=Flask(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = '5ZN5zi!45QUsGG'
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

from main import routes