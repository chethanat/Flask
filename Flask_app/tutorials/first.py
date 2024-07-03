# import Flask class from the Flask project
from flask import Flask

# Create an instance of FLask class and send the name of the current module which required to determine root path
app = Flask(__name__)


# IT tells Flask to associte the following function with root url "/" on web application
@app.route("/")
def hello_world():
    return "Hello World"


if __name__ == "__main__":
    # Start the Flask development server to server application. By default it eun on http://127.0.0.1 on port 5000
    app.run()

