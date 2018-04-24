#Importing flask and render_template
from flask import Flask, render_template, request, redirect, url_for
<<<<<<< HEAD


from datetime import datetime

#Route for index
@app.route('/')
def index():
    post = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
=======
from datetime import datetime
from . import main
from ..models import Blogpost 
#Importing Flask-SQLAlchemy for database setup.
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required
from .. import db

#Route for index...views
@main.route('/')
def index():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
>>>>>>> temp2

    return render_template('index.html', post=posts)

#Route for about
<<<<<<< HEAD
@app.route('/about')
=======
@main.route('/about')
>>>>>>> temp2
def about():
    return render_template('about.html')

#Route for post
<<<<<<< HEAD
@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()

    return render_template('post.html',post=post)

#Route for contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

#Route for add
@app.route('/add')
=======
@main.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)

#Route for add
@main.route('/add')
>>>>>>> temp2
def add():
    return render_template('add.html')

#Route for Adding Post
<<<<<<< HEAD
@app.route('/addpost', methods=['POST'])
=======
@main.route('/addpost', methods=['POST'])
>>>>>>> temp2
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Blogpost(title=title, subtitle=subtitle, author=author,content=content, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()

<<<<<<< HEAD
    return redirect(url_for('index'))
=======

    return redirect(url_for('main.index'))
>>>>>>> temp2
