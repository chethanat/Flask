# redirect will be used to redirect to particular url which given in url_for
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


@app.route('/<name>')
def say_hello(name):
    '''
    /chethu will return Hello chethu
    '''
    return f'Hello {name}'


# here inside url we can use another route or name of function Ex: '/' or 'hello_world'
@app.route("/admin")
def admin():
    return redirect(url_for('hello_world'))



if __name__ == "__main__":
    app.run(debug=True)

