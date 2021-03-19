from random import randint
import datetime

from flask import request, redirect, url_for

from app import app
from app.controller.login_controller import login_controller

#TODO either alter or remove bellow

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['authorization']
        return redirect(url_for("UserAccount", user = profileUser))

    return login_controller.index()

@app.route('/login-api', methods=['POST', 'GET'])
def login_api():
    if request.method == "POST":
        print('---------------------------------->\n\n\nin POST BB\n\n\n---------------------------------->')
        data = request.json
        print('---------------------------------->\n\n\nGot DATA\n\n\n---------------------------------->')
        return redirect(url_for("lineList", results = data['venue']), code=302)
    else:
        print('---------------------------------->\n\n\nin else in routes\n\n\n---------------------------------->')

        # TODO replace with error controller function if they try to do sonmething other than get for example
        return login_controller.index()


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


