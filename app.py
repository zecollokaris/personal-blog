#Importing flask and render_template
from flask import Flask, render_template, request, redirect, url_for
'''
#Importing Flask-SQLAlchemy for database setup.
from flask_sqlalchemy import SQLAlchemy'''

app = Flask(__name__)
'''
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
    content = db.Column(db.Text)'''


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

#Route for Adding Post
@app.route('/addpost', method=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Blogpost(title=title, subtitle=subtitle, author=author,content=content)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)