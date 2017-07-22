import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__,static_url_path="", static_folder="static") # , static_url_path='/static'
#app.static_folder = 'static'
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)

from app import views, models
