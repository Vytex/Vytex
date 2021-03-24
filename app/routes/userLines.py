from random import randint

from flask import Blueprint, request, redirect, url_for, render_template, flash, session, logging

from flask_login import login_user, login_required, current_user, logout_user

authorization = Blueprint('auth', __name__)



from app import app
from app.controller.home_controller import home_controller
from app.controller.userLines_controller import userLines_controller
from app.controller.lineList_controller import lineList_controller

@app.route('/userLines', methods = ['POST', 'GET'])
def userLines():
    if request.method == 'POST':
        venueID = request.form["vID"]
        venueClose = request.form["vc"]
        lineTime = request.form.get("lineTimesS")
        return lineList_controller.lineUp(lineTime, venueID, venueClose)
    return userLines_controller.First()


@authorization.route('/profile', methods=['GET'])
@login_required
def profile():
    image_file = url_for('static', filename='assets/' + current_user.image_file)
    return render_template('Profile/profile.html', username=current_user.username, image_file=image_file)
    
