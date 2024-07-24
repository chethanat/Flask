# FLASK
WSGI has been adopted as standard for python web appication development
WSGI acts as universal interface between web server and web applications
Werkzeug is WSGI toolit which implements requests response objects
Flask is web application framework written in python Flask is based on Werkzeug WSGI toolkit and Jinja2 template engine

## By default application will run on 127.0.0.1 on port 5000


## to run Flask appication if you are not running as main
For windows
set FLASK_APP=python_file_name
Flask run

For Linux
export FLASK_APP=python_file_name
flask run

## to take the changes modified by the user use debug=True
app.run(debug=True)

Do not use run() in production server

