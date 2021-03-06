from flask import render_template, jsonify, redirect, url_for

from app import db

# as the models file contains all the models, import what you need
# from app.models import Shoe
from app.models import Venue

class AdminController(object):
    def index(self):
        return render_template("admin/index.html")

    def get_venues(self):
        # TODO change so it retrieves a search result instead of all availible venues
        venues = Venue.get_all()
        output = []
        # formatting the data for the client 
        for venue in venues:
            output.append(
                {
                    # TODO add relevant Venue info base on table columns
                    "venue_id" : venue.venueID,
                    "venue" : venue.venue,
                    "desc" : venue.description,
                    "mon" : venue.mon.strftime("%H:%M"),
                    "tue" : venue.tue.strftime("%H:%M"),
                    "wed" : venue.wed.strftime("%H:%M"),
                    "thu" : venue.thu.strftime("%H:%M"),
                    "fri" : venue.fri.strftime("%H:%M"),
                    "sat" : venue.sat.strftime("%H:%M"),
                    "sun" : venue.sun.strftime("%H:%M"),
                    "venueID" : venue.venueID
                }
            )
        print("-------------------------------about to change pages-----------------------------------")
        # return jsonify(output)

        return jsonify(output)
    
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

    def delete_Venue(self, id):
        Venue.delete(id)

        data = {
            "success": True
        }
        return jsonify(data)

admin_controller = AdminController()