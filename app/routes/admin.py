from random import randint
import datetime

from flask import request, redirect, url_for

from app import app
from app.controller.admin_controller import admin_controller


@app.route('/admin', methods=['POST', 'GET', 'DELETE'])
def admin():
    # if request.method == "DELETE":
    #     print('------------------------------id is---------------------------------------')
    #     print(id)
    #     id = request.form['deleteVenue']
    #     return admin_controller.delete_Venue(id=id)
    return admin_controller.index()


@app.route('/admin-api', methods=['POST', 'GET'])
def admin_api():
    if request.method == "GET":
        return admin_controller.get_venues()
    elif request.method == "POST":
        print('GOT INTO THE POST')
        # get data from client in the form of json ()
        venue = request.form['venueName']
        description = request.form['description']
        venueURL = request.form['venueURL']
        venueCity = request.form['venueCity']
        venueIcon = request.form['venueIcon']
        monOpen = request.form['monS']
        monClose = request.form['monE']
        tueOpen = request.form['tuesS']
        tueClose = request.form['tuesE']
        wedOpen = request.form['wedS']
        wedClose = request.form['wedE']
        thuOpen = request.form['thurS']
        thuClose = request.form['thurE']
        friOpen = request.form['friS']
        friClose = request.form['friE']
        satOpen = request.form['satS']
        satClose = request.form['satE']
        sunOpen = request.form['sunS']
        sunClose = request.form['sunE']
        return admin_controller.create_venue(venue=venue, description=description, venueURL=venueURL, venueCity=venueCity, venueIcon=venueIcon, monOpen=monOpen, monClose=monClose, tueOpen=tueOpen, tueClose=tueClose, wedOpen=wedOpen, wedClose=wedClose, thuOpen=thuOpen, thuClose=thuClose, friOpen=friOpen, friClose=friClose, satOpen=satOpen, satClose=satClose, sunOpen=sunOpen, sunClose=sunClose)
    
    return admin_controller.index()

@app.route('/admin-api/delete', methods=['POST'])
def admin_api_delete():
    if request.method == "POST":
        print('------------------------------id is---------------------------------------')
        id = request.form['venueID']
        print(id)
        return admin_controller.delete_Venue(id=id)

    return admin_controller.index()
