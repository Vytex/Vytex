from random import randint
from flask import request, redirect, url_for

from app import app
from app.controller.home_controller import home_controller
from app.controller.userLines_controller import UserLinesController
from app.controller.lineList_controller import lineList_controller

@app.route('/userLines', methods = ['POST', 'GET'])
def userLines():
    #1 save a spot
    #2 redirect to userLines/index.html with parameters
    venueID = request.form["vID"]
    venueClose = request.form["vc"]
    lineTime = request.form.get("lineTimesS")
    return lineList_controller.lineUp(lineTime, venueID, venueClose)


    