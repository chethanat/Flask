# we can also inherit templates here you can refer index1.html and base.html for reference
# we can also import templates from bootstrap(getbootstrap.com) go to bootstrap website and copy the sripts of css and whateer you want present their
# you need to add css inside head section <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous"> and javascript below at the end of bod section so that you can use bootstrap
#<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
#<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>
# you can add navbar bycopying it from vnavbar section and adding at beginning of body
# you can create any child pages using t his base template
# now you can use the same base.html for other html files example new.html just you need to use extends
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index1.html', content="Testing")

@app.route("/new")
def new_page():
    return render_template('new.html')

if __name__ == "__main__":
    app.run(debug=True)