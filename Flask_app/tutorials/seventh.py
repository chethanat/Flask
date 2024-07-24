# message flashing: This will let the user know what actions he performed by messages Ex: If user login it will let know user has logged in. If logged out it will let now user logged out
from flask import Flask, render_template, request, url_for, redirect, flash

app = Flask(__name__)

app.secret_key = "hello"

@app.route('/api', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        flash("Logged in successful")
        user = request.form['nm']
        return user
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    # incllude this in login.html with get_flashed_messages function
    flash("User logged out successfully", "info")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)