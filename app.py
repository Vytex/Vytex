from flask import Flask, render_template, request

app = Flask(__name__)

# root to index
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/lineList')
def lineList():
    results = [
        ["Test Venue", "8PM - LATE", ["9:15-9:45", "9:30-10:00", "10:15-10:45", "11:15-11:45"]]
    ]
    
    return render_template("lineList.html", results=results)

if  __name__ == "__main__":
    app.run(debug=True)