#Importing flask and render_template
from flask import Flask, render_template

#Importing Flask-SQLAlchemy for database setup.
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Setting Database location
app.config['SQALCHEMY_DATABASE_URI'] = 'sqlite:////Home/Desktop/personal-blog-project/blog.db'
db = SQAlchemy(app)

#Creating table that holds information
class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)


#Route for index
@app.route('/')
def index():
    return render_template('index.html')

#Route for about
@app.route('/about')
def about():
    return render_template('about.html')

#Route for post
@app.route('/post')
def post():
    return render_template('post.html')

#Route for contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

#Route for add
@app.route('/add')
def add():
    return render_template('add.html')



if __name__ == '__main__':
    app.run(debug=True)