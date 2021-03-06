from flask import Flask, render_template, request

app = Flask(__name__)

# root to index
@app.route('/')
def index():
    return render_template("Index.html")

@app.route('/info')
def info():
    return render_template("UserAccount.html")

@app.route('/login')
def login():
    return render_template("UserLogin.html")


if  __name__ == "__main__":
    app.run(debug=True)