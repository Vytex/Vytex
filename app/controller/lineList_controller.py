from flask import render_template, jsonify
from flask import render_template, jsonify

from app import db

# as the models file contains all the models, import what you need
# from app.models import Shoe
from app.models import Venue

class LineListController(object):
    def index(self):
        return render_template("lineList/index.html")

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
        return render_template("lineList/index.html", results=output)

lineList_controller = LineListController()