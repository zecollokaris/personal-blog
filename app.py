<<<<<<< HEAD



#Setting Database location
app.config['SQALCHEMY_DATABASE_URI'] = 'sqlite:////Home/Desktop/personal-blog-project/blog.db'
db = SQLAlchemy(app)

=======
#Importing flask and render_template
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
#Importing Flask-SQLAlchemy for database setup.

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Setting Database location
SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://karis:Kar!s123@localhost/blog'
db = SQLAlchemy(app)
>>>>>>> temp2



if __name__ == '__main__':
    app.run(debug=True)