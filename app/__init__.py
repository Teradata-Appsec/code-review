from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_login
from flask_bootstrap import Bootstrap
import os

file_path = os.path.abspath(os.getcwd()) + "/todo.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + file_path
app.secret_key = "xooPaezohthou5"

db = SQLAlchemy(app)

Bootstrap(app)

login_manager = flask_login.LoginManager()
login_manager.init_app(app)


from app import routes
