from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        import pdb
        pdb.set_trace()
        result = request.form
        return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)