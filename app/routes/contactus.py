from random import randint
import datetime

from flask import Blueprint, request, redirect, url_for, render_template, flash, session, logging
from flask_login import login_user, login_required, current_user, logout_user

authorization = Blueprint('auth', __name__)

from app import app
from app.controller.contactus_controller import contactus_controller

#TODO either alter or remove bellow

@app.route('/contact', methods=['POST', 'GET'])
def contactus():
    if request.method == 'POST':
        venue = request.form['searchin']
        return redirect(url_for("Home", venue = venue))

    return contactus_controller.index()


@authorization.route('/profile', methods=['GET'])
@login_required
def profile():
    image_file = url_for('static', filename='assets/' + current_user.image_file)
    return render_template('Profile/profile.html', username=current_user.username, image_file=image_file)
#@app.route('/contactus-api', methods=['POST', 'GET'])
#def contactus_api():
    #if request.method == "POST":
        #print('---------------------------------->\n\n\nin POST BB\n\n\n---------------------------------->')
        #data = request.json
        #print('---------------------------------->\n\n\nGot DATA\n\n\n---------------------------------->')
        #return redirect(url_for("lineList", results = data['venue']), code=302)
    #else:
        #print('---------------------------------->\n\n\nin else in routes\n\n\n---------------------------------->')

        # TODO replace with error controller function if they try to do sonmething other than get for example
        #return contactus_controller.index()


# BEFORE I CHANGED TO REPRESENT THE FINAL APP

# @app.route('/home-api', methods=['POST', 'GET'])
# def home_api(venueName=None):
#     if request.method == "GET":
#         print('---------------------------------->\n\n\nin GET\n\n\n---------------------------------->')
#         data = request.json
#         return home_controller.get_venues(data['venue'])
#     elif request.method == "POST":
#         # get data from client in the form of json ()
#         data = request.json
#         time = datetime.time(9, 0)
#         return home_controller.create_venue(venue=data['venue'], description='This is a test venue', mon=time, tue=time, wed=time, thu=time, fri=time, sat=time, sun=time)
#     else:
#         print('---------------------------------->\n\n\nin else in routes\n\n\n---------------------------------->')

#         # TODO replace with error controller function if they try to do sonmething other than get for example
#         return home_controller.index()


