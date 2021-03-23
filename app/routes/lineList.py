from random import randint

from flask import request, redirect, url_for

from app import app
from app.controller.line_list_controller import line_list_controller
from app.controller.home_controller import home_controller
from app.models import Venue

@app.route('/line_list', methods=['POST', 'GET'])
def line_list_home():
    if request.method == 'POST' and request.form.get('searchin'):
        venue = request.form['searchin']
        return redirect(url_for("line_list", venue = venue))
    elif request.method == 'POST' and request.form.get('line_timesS'):
        line_time = request.form['line_timesS']
        venue_id = request.form['vID']
        venue_close = request.form['vc']
        return line_list_controller.line_up(line_time = line_time, venue_id = venue_id, venue_close = venue_close)    
    

    return home_controller.index()

@app.route('/line_list/<venue>', methods=['POST', 'GET'])
def line_list(venue):
    if request.method == 'POST':
        venue = request.form['searchin']
        return render_template("line_list", venue = venue)
    elif (venue != None):
        return line_list_controller.get_venues(venueName = venue)

    return line_list_controller.index()

@app.route('/line_list/line_up', methods = ['POST'])
def line_up():
    venue_id = request.form["vID"]
    venue_close = request.form["vc"]
    line_time = request.form.get("line_timesS")
    return line_list_controller.line_up(line_time, venue_id, venue_close)