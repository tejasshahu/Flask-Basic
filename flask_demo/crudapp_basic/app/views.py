from flask_demo.crudapp.app import app, db
from flask import request, flash, url_for, redirect, render_template
from flask_demo.crudapp.app.models.database_models.Students import Students


@app.route('/')
def home_page():
    return render_template('home_page.html')


@app.route('/show_all')
def show_all():
    return render_template('show_all.html', students=db.session.query(Students.id,
                                                                      Students.name,
                                                                      Students.city,
                                                                      Students.addr,
                                                                      Students.pin).all())


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr'] or not request.form['pin']:
            flash('Please enter all the fields', 'error')
        else:
            student = Students(request.form['name'], request.form['city'], request.form['addr'], request.form['pin'])
            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('home_page'))
    return render_template('new.html')


@app.route('/delete', methods=['POST'])
def delete_student():
    if request.method == 'POST':
        if request.form['id']:
            db.session.delete(Students.query.filter_by(id=request.form['id']).one())
            db.session.commit()
            return redirect(url_for('show_all'))


@app.route('/edit', methods=['POST'])
def edit_student():
    if request.method == 'POST':
        # if not request.form['name'] or not request.form['city'] or not request.form['addr'] or not request.form['pin']:
        #     flash('Please enter all the fields', 'error')
        if request.form['id']:
            students = db.session.query(Students.id,
                                        Students.name,
                                        Students.city,
                                        Students.addr,
                                        Students.pin
                                        ).filter(Students.id == request.form['id']).all()
            return render_template('edit_page.html', students=students)


@app.route('/update_student', methods=['POST'])
def update_student():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr'] or not request.form['pin']:
            flash('Please enter all the fields', 'error')
        else:
            update_id = request.form['id']
            Students.query.filter(Students.id == update_id).update({
                'name': request.form['name'],
                'city': request.form['city'],
                'addr': request.form['addr'],
                'pin': request.form['pin']
            })
            db.session.commit()
            flash('Record was successfully updated')
            return redirect(url_for('home_page'))

# @flask_sijax.route(app, '/delete')
# def delete():
#     def delete_student(obj_response):
#         obj_response.alert('Are you sure want to delete?')
#         # if(yes):
#         #     return render_template('home_page.html', Students=Students.query.all())
#         #     # delete student
#         # else:
#         #     return render_template('home_page.html', Students=Students.query.all())
#             # dont delete redirect to home_page page
#     if g.sijax.is_sijax_request:
#         # Sijax request detected - let Sijax handle it
#         g.sijax.register_callback('delete_student', delete_student)
#         return g.sijax.process_request()
#     return render_template('show_all.html', students=db.session.query(Students.name,
#                                                                       Students.city,
#                                                                       Students.addr,
#                                                                       Students.pin).all())

