from urllib import response
from flask import Flask, redirect, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os


dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "\\app\database.db"
print(dbdir)

app=Flask(__name__, template_folder='templates')

# DB connection
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(50), nullable = False)
    Email = db.Column(db.String(50), nullable = False)
    dogname = db.Column(db.String(50), nullable = False)
    dogtype = db.Column(db.String(50))
    dogissue = db.Column(db.String(200))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/new_contact',methods=['POST'])
def new_contact():
    if request.method == 'POST':
        new_post = Posts(fullname = request.form['FullName'], Email = request.form['Email'], dogname = request.form['DogName'], dogtype = request.form['DogType'], dogissue = request.form['DogIssue'])
        db.session.add(new_post)
        db.session.commit()
        return render_template('received.html')


def pag_not_found(error):
    #return render_template('404.html'), 404
    return redirect(url_for('index'))


if __name__=='__main__':
    db.create_all()
    app.register_error_handler(404, pag_not_found)
    app.run(debug=True, port=5000)  #debug sirve para qe se actualice solo, port por defecto es 5000, puedo modificarlo

