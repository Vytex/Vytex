from flask import render_template, jsonify
from flask import render_template, jsonify
from datetime import time, datetime

from app import db

# as the models file contains all the models, import what you need
# from app.models import Shoe
from app.models import Venue

def timeify(timeString):
    x = timeString.partition(':')

    return time(int(x[0]), int(x[2]))

class LineListController(object):
    def index(self):
        return render_template("lineList/index.html")

    def get_venues(self, venueName):
        venues = Venue.get(venueName)
        output = []
        currentDay = datetime.today().weekday()

        for venue in venues:
            
            data = {
                "venueID" : venue.venueID,
                "venue" : venue.venue,
                "venueURL": venue.venueURL,
                "venueCity": venue.venueCity,
                "venueIconAddress": venue.venueIcon,
                "desc" : venue.description,
            }
            if currentDay == 0:
                data["Open"] = venue.monOpen.strftime("%H:%M")
                data["Close"] = venue.monClose.strftime("%H:%M")

            if currentDay == 1:
                data["Open"] = venue.tueOpen.strftime("%H:%M")
                data["Close"] = venue.tueClose.strftime("%H:%M")

            if currentDay == 2:
                data["Open"] = venue.wedOpen.strftime("%H:%M")
                data["Close"] = venue.wedClose.strftime("%H:%M")

            if currentDay == 3:
                data["Open"] = venue.thuOpen.strftime("%H:%M")
                data["Close"] = venue.thuClose.strftime("%H:%M")

            if currentDay == 4:
                data["Open"] = venue.friOpen.strftime("%H:%M")
                data["Close"] = venue.friClose.strftime("%H:%M")

            if currentDay == 5:
                data["Open"] = venue.satOpen.strftime("%H:%M")
                data["Close"] = venue.satClose.strftime("%H:%M")

            if currentDay == 6:
                data["Open"] = venue.sunOpen.strftime("%H:%M")
                data["Close"] = venue.sunClose.strftime("%H:%M")

            output.append(data)

        return render_template("lineList/index.html", results=output)

lineList_controller = LineListController()