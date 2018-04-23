from . import db

#Importing Flask-SQLAlchemy for database setup.
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

class Blogpost(db.Model):
    __tablename__ = 'blog'
    #Creating table that holds information
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)