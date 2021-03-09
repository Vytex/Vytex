from random import randint

from flask import request, redirect, url_for

from app import app
from app.controller.lineList_controller import lineList_controller
from app.controller.home_controller import home_controller
from app.models import Venue

@app.route('/lineList', methods=['POST', 'GET'])
def lineListHome():
    if request.method == 'POST':
        venue = request.form['searchin']
        return redirect(url_for("lineList", venue = venue))

    return home_controller.index()

@app.route('/lineList/<venue>', methods=['POST', 'GET'])
def lineList(venue):
    if request.method == 'POST':
        venue = request.form['searchin']
        return render_template("lineList", venue = venue)
    elif (venue != None):
        return lineList_controller.get_venues(venueName = venue)

    return lineList_controller.index()

# @app.route('/lineList-api', methods=['POST', 'GET'])
# def lineList_api():
#     if request.method == "POST":
#         data = request.json
#         return redirect(url_for("lineList", results = data['venue']), code=302)
#     else:

#         # TODO replace with error controller function if they try to do sonmething other than get for example
#         return lineList_controller.index()