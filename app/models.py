<<<<<<< HEAD
from . import db

#Importing Flask-SQLAlchemy for database setup.
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

class Blogpost(db.Model):
    __tablename__ = 'blog'
    #Creating table that holds information
=======
#Importing flask and render_template
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from . import db
from flask_login import UserMixin

''''@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))'''

#Creating table that holds information
class Blogpost(db.Model):
    __tablename__ = 'posts'
>>>>>>> temp2
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
<<<<<<< HEAD
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)
=======
    content = db.Column(db.String(500))
    date_posted = db.Column(db.DateTime)

#Creating table that holds information
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    username = db.Column(db.String(10))
    password = db.Column(db.String(20))
    password = db.Column(db.String(20))
    
>>>>>>> temp2
