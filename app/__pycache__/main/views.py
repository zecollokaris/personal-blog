#Importing flask and render_template
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

#Importing Flask-SQLAlchemy for database setup.
from flask_sqlalchemy import SQLAlchemy

#Route for index...views
@app.route('/')
def index():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()

    return render_template('index.html', post=posts)

#Route for about
@app.route('/about')
def about():
    return render_template('about.html')

#Route for post
@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)

#Route for add
@app.route('/add')
def add():
    return render_template('add.html')

#Route for Adding Post
@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Blogpost(title=title, subtitle=subtitle, author=author,content=content, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))
