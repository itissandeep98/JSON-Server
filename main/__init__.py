from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key = '5ZN5zi!45QUsGG'
from main import routes