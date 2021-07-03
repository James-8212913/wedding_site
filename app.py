from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title = 'Home')

@app.route("/about")
def about():
    return render_template('about.html', title = 'On The Day')

@app.route("/other_stuff")
def other_stuff():
    return render_template('other_stuff.html', title = "Other Stuff")

if __name__ == '__name__':
    app.run(debug=True)
