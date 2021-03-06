from flask import Flask, render_template, request

app = Flask(__name__)

# root to index
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contact')
def contactus():
    return render_template("contactus.html")

@app.route('/create')
def create():
    return render_template("create.html")


if  __name__ == "__main__":
    app.run(debug=True)