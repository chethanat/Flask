# session will help to access the other pages by using with passing any information here in ogin their is user
# we can use the same user information when accessing the user information and send the data no need to send usr as part of url
from flask import Flask, render_template, request, url_for, redirect, session
from datetime import timedelta

app = Flask(__name__)
# the session data will be encrypted to encrypt and decrypt the session information use below
app.secret_key = "hello"
# here we can define how long the session should be active, then pass the same thing inside session
app.permanent_session_lifetime = timedelta(days=5)

# here we are allowing methods GET and POST throgh this rouuter
@app.route('/api', methods=["POST", "GET"])
def login():
    # but to determine you got GET or POST request use request from fastapi. If it is post i will redirect to submit the form if it is get i will
    if request.method == "POST":
        session.permanent = True # to make session permanent as defined above

        user = request.form['nm']
        session["user"] = user
        return (redirect(url_for("user")))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template('login.html')


@app.route('/user')
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>Hi  {user}</h1>"
    else:
        return redirect(url_for("login"))


# to remove data from the session use pop and pass what data needs to be remove
@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)