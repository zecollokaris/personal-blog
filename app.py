#Importing flask and render_template
from flask import Flask, render_template

app = Flask(__name__)

#Route for index
@app.route('/')
def index():
    return render_template('index.html')

#Route for about
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)