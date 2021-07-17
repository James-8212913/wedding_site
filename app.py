from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about/")
def about():
    return render_template('about.html')

@app.route("/other_stuff/")
def other_stuff():
    return render_template('other_stuff.html')

if __name__ == '__name__':
    app.run(debug=True)
