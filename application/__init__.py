from flask import Flask

app = Flask(__name__)

from application import views  # Circular Imports https://flask.palletsprojects.com/en/1.1.x/patterns/packages/