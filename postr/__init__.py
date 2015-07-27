from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config.DevConfig')
db = SQLAlchemy(app)

from postr import views, models