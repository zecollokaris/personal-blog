#Importing flask and render_template
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from . import db

#Creating table that holds information
class Blogpost(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
