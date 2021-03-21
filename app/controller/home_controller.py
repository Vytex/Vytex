from flask import render_template, jsonify, redirect, url_for, Blueprint, request, flash, session, logging
from flask_login import login_user, login_required, current_user, logout_user

from app import db

# as the models file contains all the models, import what you need
# from app.models import Shoe
from app.models import Venue

class HomeController(object):
    def index(self):
        if current_user != None and current_user.is_authenticated:
            print(current_user)
            image_file= url_for('static', filename='assets/' + current_user.image_file)
            return render_template("home/index.html", image_file=image_file)
        else:
            image_file= url_for('static', filename='assets/profileButtonPlaceholder.jpg')
            return render_template("home/index.html", image_file=image_file)

    def get_venues(self, venueName):
        # TODO change so it retrieves a search result instead of all availible venues
        venues = Venue.get(venueName)
        output = []
        # formatting the data for the client 
        for venue in venues:
            output.append(
                {
                    # TODO add relevant Venue info base on table columns
                    "venue" : venue.venue,
                    "desc" : venue.description,
                    "mon" : venue.mon,
                    "tue" : venue.tue,
                    "wed" : venue.wed,
                    "thu" : venue.thu,
                    "fri" : venue.fri,
                    "sat" : venue.sat,
                    "sun" : venue.sun
                    # "id": user.id,
                    # "brand": shoe.brand,
                    # "model": shoe.model,
                    # "size": shoe.size
                }
            )
        print("-------------------------------about to change pages-----------------------------------")
        # return jsonify(output)

        return redirect(url_for(".lineList", output=output), code=302)
    
    def save_venue(self, venue):
        # shoe = Shoe(size=12, brand='reebook', model='n%d' % (randint(0, 100)))
        # saving shoe
        venue_id = venue.save()
        # success or fail page
        # return render_template("shoe/index.html", shoe_id = shoe_id)
        data = {
            "success": True
        }

        print("data", data)
        return jsonify(data)

    def create_venue(self, venue, description, mon, tue, wed, thu, fri, sat, sun):
        # create a shoe
        print(venue, description, mon, tue, wed, thu, fri, sat, sun)
        venue = Venue(venue=venue, description=description, mon=mon, tue=tue, wed=wed, thu=thu, fri=fri, sat=sat, sun=sun)
        print('--------------------------------------------------->')
        print('before save')
        venue_id = venue.save()
        print('--------------------------------------------------->')
        print('after save')
        # give this object back to the client
        data = {
            "id": venue_id
        }
        return jsonify(data)
    # venueID = db.Column(db.Integer, primary_key=True)
    # venue = db.Column(db.NVARCHAR(30))
    # description = db.Column(db.NVARCHAR(500))
    # mon = db.Column(db.TIME(4))
    # tue = db.Column(db.TIME(4))
    # wed = db.Column(db.TIME(4))
    # thu = db.Column(db.TIME(4))
    # fri = db.Column(db.TIME(4))
    # sat = db.Column(db.TIME(4))
    # sun = db.Column(db.TIME(4))

home_controller = HomeController()