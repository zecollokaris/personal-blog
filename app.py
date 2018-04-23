


#Setting Database location
app.config['SQALCHEMY_DATABASE_URI'] = 'sqlite:////Home/Desktop/personal-blog-project/blog.db'
db = SQLAlchemy(app)




if __name__ == '__main__':
    app.run(debug=True)