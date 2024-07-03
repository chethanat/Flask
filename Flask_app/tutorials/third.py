# render_template: it will grab htm file and add it here
from flask import render_template, Flask

# as best practice always add html file within the templates folder
#NOTE: the html file should be always in templates folder else you will get error template not found

app = Flask(__name__)


@app.route("/html")
def html_func():
    return render_template('index.html')

# you can send data from backend to html file frontend and can access in html using jinja
@app.route('/<name>')
def send_data_to_html(name):
    return render_template('index.html', content=name, list=["a", "b"])

# you can also use python code within htm file see html file to print hello 10 times
if __name__ == "__main__":
    app.run(debug=True)


