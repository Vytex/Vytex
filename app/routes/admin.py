from random import randint
import datetime

from flask import request, redirect, url_for

from app import app
from app.controller.admin_controller import admin_controller


@app.route('/admin', methods=['POST', 'GET', 'DELETE'])
def admin():
    return admin_controller.index()


@app.route('/admin-api', methods=['POST', 'GET'])
def admin_api():
    if request.method == "GET":
        return admin_controller.get_venues()
    elif request.method == "POST" and request.form.get('venue-url'):
        # get data form client in the form of json ()
        # old if post contains the venue_url 
        venue = request.form['venue-name']
        description = request.form['description']
        venue_url = request.form['venue-url']
        venue_city = request.form['venue-city']
        venue_icon = request.form['venue-icon']
        mon_open = request.form['mon-s']
        mon_close = request.form['mon-e']
        tue_open = request.form['tues-s']
        tue_close = request.form['tues-e']
        wed_open = request.form['wed-s']
        wed_close = request.form['wed-e']
        thu_open = request.form['thur-s']
        thu_close = request.form['thur-e']
        fri_open = request.form['fri-s']
        fri_close = request.form['fri-e']
        sat_open = request.form['sat-s']
        sat_close = request.form['sat-e']
        sun_open = request.form['sun-s']
        sun_close = request.form['sun-e']
        line_capacity = request.form['cap']

        return admin_controller.create_venue(venue=venue, description=description, venue_url=venue_url, venue_city=venue_city, venue_icon=venue_icon,
         mon_open=mon_open, mon_close=mon_close, tue_open=tue_open, tue_close=tue_close, wed_open=wed_open, wed_close=wed_close, thu_open=thu_open, 
         thu_close=thu_close, fri_open=fri_open, fri_close=fri_close, sat_open=sat_open, sat_close=sat_close, sun_open=sun_open, sun_close=sun_close,
         line_capacity = line_capacity)

    elif request.method == "POST" and request.form.get('capacity'):
        venue_id = request.form['venue-id']
        capacity = request.form['capacity']

        return admin_controller.create_list(venue_id=venue_id, capacity=capacity)

    return admin_controller.index()

@app.route('/admin-api/delete', methods=['POST'])
def admin_api_delete():
    if request.method == "POST" and request.form.get('date'):
        id = request.form['venue-id']
        date = request.form['date']
        return admin_controller.deleteLine(id, date)
    else:
        id = request.form['venue-id']
        return admin_controller.delete_venue(id=id)

    return admin_controller.index()
