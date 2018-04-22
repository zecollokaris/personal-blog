#Importing flask and render_template
from flask import Flask, render_template

#Importing Flask-SQLAlchemy for database setup.
from flask_sqlalchemy import SQAlchemy

app = Flask(__name__)

#Setting Database location
app.config['SQALCHEMY_DATABASE_URI'] = 'sqlite:////Home/Desktop/personal-blog-project/blog.db'

db = SQAlchemy(app)

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

if __name__ == '__main__':
    app.run(debug=True)