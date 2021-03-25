from random import randint

from flask import Blueprint, request, redirect, url_for, render_template, flash, session, logging

from flask_login import login_user, login_required, current_user, logout_user

authorization = Blueprint('auth', __name__)



from app import app
from app.controller.home_controller import home_controller
from app.controller.lineList_controller import lineList_controller

@app.route('/userLines', methods = ['POST', 'GET'])
@login_required
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
    
@authorization.route('/profile', methods=['GET'])
@login_required
def profile():
    #returns profile icon if user is logged in
    image_file = url_for('static', filename='assets/' + current_user.image_file)
    return render_template('Profile/profile.html', username=current_user.username, image_file=image_file)
    
