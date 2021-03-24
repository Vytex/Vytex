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
        lineTime = request.form['lineTimesS']
        venueID = request.form['vID']
        venueClose = request.form['vc']
        return lineList_controller.lineUp(lineTime = lineTime, venueID = venueID, venueClose = venueClose)    
    

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

@app.route('/lineList/lineUp', methods = ['POST'])
@login_required
def lineUp():
    if current_user != None and current_user.is_authenticated:
        venueID = request.form["vID"]
        venueClose = request.form["vc"]
        lineTime = request.form.get("lineTimesS")
        return lineList_controller.lineUp(lineTime, venueID, venueClose)
    else:
        return render_template("Login/index.html")

