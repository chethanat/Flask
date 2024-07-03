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

