from random import randint
from flask import request, redirect, url_for

from app import app
from app.controller.home_controller import home_controller
from app.controller.userLines_controller import user_lines_controller
from app.controller.lineList_controller import line_list_controller

@app.route('/user_lines', methods = ['POST', 'GET'])
def user_lines():
    #1 save a spot
    #2 redirect to user_lines/index.html with parameters
    if request.method == 'POST':
        venue_id = request.form["vID"]
        venue_close = request.form["vc"]
        line_time = request.form.get("line_timesS")
        return lineList_controller.line_up(line_time, venue_id, venue_close)
    return user_lines_controller.first()


    