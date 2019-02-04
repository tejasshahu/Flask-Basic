import os
from flask_demo.crudapp.app import app

path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')

app.config['SIJAX_STATIC_PATH'] = path
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Students.sqlite3'
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

