from flask_login import login_user, login_required, current_user, logout_user
from random import randint

from flask import Blueprint, request, redirect, url_for, render_template, flash, session, logging
authorization = Blueprint('auth', __name__)


from app import app
from app.controller.lineList_controller import lineList_controller
from app.controller.home_controller import home_controller
from app.models import Venue

@app.route('/lineList', methods=['POST', 'GET'])
def lineListHome():
    if request.method == 'POST' and request.form.get('searchin'):
        venue = request.form['searchin']
        return redirect(url_for("lineList", venue = venue))
    elif request.method == 'POST' and request.form.get('lineTimesS'):
        previous_HTML = request.referrer
        arg1 = previous_HTML.rsplit('/', 1)[-1]
        just_the_argument = arg1.rsplit('?', 1)[0]

        lineTime = request.form['lineTimesS']
        venueID = request.form['vID']
        venueClose = request.form['vc']
        return lineList_controller.line_up(lineTime = lineTime, venueID = venueID, venueClose = venueClose, name=just_the_argument)    
    

    return home_controller.index()

@app.route('/lineList/<venue>', methods=['POST', 'GET'])
def lineList(venue):
    if request.method == 'POST':
        venue = request.form['searchin']
        return render_template("lineList", venue = venue)
    elif (venue != None):
        return lineList_controller.get_venues(venueName = venue)

    return lineList_controller.index()


@authorization.route('/profile', methods=['GET'])
@login_required
def profile():
    image_file = url_for('static', filename='assets/' + current_user.image_file)
    return render_template('Profile/profile.html', username=current_user.username, image_file=image_file)

@app.route('/lineList/line_up', methods = ['POST'])
@login_required
def line_up():
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
    return redirect(url_for("linedUp", name = just_the_argument, venueID = venueID ,lineTime = lineTime, venue_close = venueClose ))

@app.route('/lineList/line_up/<name>', methods = ['POST', 'GET'])
def linedUp(name):
    if request.args.get('lineTime') != None:
        return lineList_controller.line_up(request.args.get('lineTime'), request.args.get('venueID'), request.args.get('venue_close'), name)
    return lineList_controller.get_venues(name, error_msg='No availible times to line up in')

