from random import randint
from flask import request, redirect, url_for

from app import app
from app.controller.home_controller import home_controller
from app.controller.lineList_controller import lineList_controller

@app.route('/userLines', methods = ['POST', 'GET'])
def userLines():
    if request.method == 'POST':
         # used to get search value from previous pages html so it can 
        # run the same search on the error page if routed there
        previous_HTML = request.referrer
        arg1 = previous_HTML.rsplit('/', 1)[-1]
        just_the_argument = arg1.rsplit('?', 1)[0]
        #the rest of the form values
        venueID = request.form["vID"]
        venueClose = request.form["vc"]
        lineTime = request.form.get("lineTimesS")
        # returns as redirect to get search param in html for error handling
        return redirect(url_for("user_lined_up", name = just_the_argument, venueID = venueID ,lineTime = lineTime, venue_close = venueClose ))
    return lineList_controller.First()



@app.route('/userLines/<name>', methods = ['POST', 'GET'])
def user_lined_up(name):
    return lineList_controller.lineUp(request.args.get('lineTime'), request.args.get('venueID'), request.args.get('venue_close'), name)