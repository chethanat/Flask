# we are exposing on GET and POST
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

# by default any URL respons to GET requests. We can allow other requests as well using methods
# here we are allowing methods GET and POST throgh this rouuter
@app.route('/api', methods=["POST", "GET"])
def login():
    # but to determine you got GET or POST request use request from fastapi. If it is post i will redirect to submit the form if it is get i will
    if request.method == "POST":
        user = request.form['nm']
        return (redirect(url_for("user", usr=user)))
    else:
        return render_template('login.html')


@app.route('/<usr>')
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)