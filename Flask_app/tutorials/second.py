# redirect will be used to redirect to particular url which given in url_for
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World"


# variable here name is the variable this will help to build URL dynamically
# we can convert variable from one type to another <converter:variable_name> Ex:<int:id>
# we have strings, int, float, path(it is string but also accept slashes), uuid
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


# add_url_rule() is function of application objevt that is also available to buil a URL with function
# This approach mainly used in case we are importing view function from another module
# add_url_rule(<url_rule>, <endpoint>, <view fuunction>)
# here we try to map ch view function

def ch():
    return "Hello Chethan"
app.add_url_rule('/ch','/ch', ch)


if __name__ == "__main__":
    app.run(debug=True)

