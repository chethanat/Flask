from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/<name>')
def say_hello(name):
    '''
    /chethu will return Hello chethu
    '''
    return f'Hello {name}'


if __name__ in "__main__":
    app.run(debug=True)