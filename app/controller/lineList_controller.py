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
                    "mon" : venue.mon,
                    "tue" : venue.tue,
                    "wed" : venue.wed,
                    "thu" : venue.thu,
                    "fri" : venue.fri,
                    "sat" : venue.sat,
                    "sun" : venue.sun
                }
            )
        print('------------------------------results--------------------------------------------')
        print(output[0]['venue'])
        return render_template("lineList/index.html", results=output)

lineList_controller = LineListController()