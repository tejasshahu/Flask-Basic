from flask_demo.crudapp.app import app, db, g

db.create_all()
app.run(host="127.0.0.1", port=1234, debug=True)

