from random import randint

from flask import request, redirect, url_for

from app import app
from app.controller.lineList_controller import line_list_controller
from app.controller.home_controller import home_controller
from app.models import Venue

@app.route('/lineList', methods=['POST', 'GET'])
def line_list_home():
    if request.method == 'POST' and request.form.get('searchin'):
        venue = request.form['searchin']
        return redirect(url_for("line_list", venue = venue))
    elif request.method == 'POST' and request.form.get('line-time-s'):
        line_time = request.form['line-times-s']
        venue_id = request.form['v-id']
        venue_close = request.form['vc']
        return line_list_controller.line_up(line_time = line_time, venue_id = venue_id, venue_close = venue_close)    
    

    return home_controller.index()

@app.route('/lineList/<venue>', methods=['POST', 'GET'])
def line_list(venue):
    if request.method == 'POST':
        venue = request.form['searchin']
        return render_template("line_list", venue = venue)
    elif (venue != None):
        return line_list_controller.get_venues(venue_name = venue)

    return line_list_controller.index()

@app.route('/lineList/lineUp', methods = ['POST'])
def line_up():
    venue_id = request.form["v-id"]
    venue_close = request.form["vc"]
    line_time = request.form.get("line-times-s")
    return line_list_controller.line_up(line_time, venue_id, venue_close)