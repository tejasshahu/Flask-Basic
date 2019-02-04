from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
import flask_sijax

app = Flask(__name__)
app.config.from_object('config')
flask_sijax.Sijax(app)

db = SQLAlchemy(app)

from flask_demo.crudapp.app import views

