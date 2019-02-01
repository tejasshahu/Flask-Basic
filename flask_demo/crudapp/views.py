
# import flask_sijax
# flask_sijax.Sijax(app)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_demo.crudapp import app, db

# path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')

# app.config['SIJAX_STATIC_PATH'] = path
# app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'
#
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Students.sqlite3'
# app.config['SECRET_KEY'] = "random string"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# app = Flask(__name__)
# app.config.from_object('config')

# db = SQLAlchemy(app)

# from flask_demo.crudapp import db
# from flask_demo.crudapp import app
from flask import Flask
# app = Flask(__name__)
from flask import request, flash, url_for, redirect, render_template
from flask_demo.crudapp.app.models.database_models.Students import Students


@app.route('/')
def show_all():
    return render_template('show_all.html', Students=db.session.query(Students.name).all())


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields', 'error')
        else:
            student = Students(request.form['name'], request.form['city'], request.form['addr'], request.form['pin'])

            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')

# @app.route('/delete', methods=['POST'])
# def delete_student(id):
#     if request.method.post:
#         return render_template('show_all.html', Students=Students.query.all())
#     return render_template('show_all.html', Students=Students.query.all())


@app.route('/edit', methods=['POST'])
def edit_student(id):
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields', 'error')
        else:
            student = Students(request.form['name'], request.form['city'], request.form['addr'],
                               request.form['pin'])

            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')


# @flask_sijax.route(app, '/delete')
# def delete_student(id):
#     def say_hi(obj_response):
#         obj_response.alert('Are you sure want to delete?')
#         if(yes):
#             return render_template('show_all.html', Students=Students.query.all())
#             # delete student
#         else:
#             return render_template('show_all.html', Students=Students.query.all())
#             # dont delete redirect to show_all page
#         if g.sijax.is_sijax_request:
#             # Sijax request detected - let Sijax handle it
#             g.sijax.register_callback('say_hi', say_hi)
#             return g.sijax.process_request()
#         return render_template('show_all.html', Students=Students.query.all())
#         # return render_template('sijaxexample.html')


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    db.create_all()
    app.run(debug=True)

