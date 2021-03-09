from flask import render_template, jsonify, redirect, url_for
from datetime import time, datetime

from app import db

# as the models file contains all the models, import what you need
# from app.models import Shoe
from app.models import Venue

def timeify(timeString):
    x = timeString.partition(':')

    return time(int(x[0]), int(x[2]))

class AdminController(object):
    def index(self):
        return render_template("admin/index.html")

    def get_venues(self):
        # TODO change so it retrieves a search result instead of all availible venues
        venues = Venue.get_all()
        output = []
        currentDay = datetime.today().weekday()
        # formatting the data for the client 
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
                data["monOpen"] = venue.monOpen.strftime("%H:%M")
                data["monClose"] = venue.monClose.strftime("%H:%M")

            if currentDay == 1:
                data["tueOpen"] = venue.tueOpen.strftime("%H:%M")
                data["tueClose"] = venue.tueClose.strftime("%H:%M")

            if currentDay == 2:
                data["wedOpen"] = venue.wedOpen.strftime("%H:%M")
                data["wedClose"] = venue.wedClose.strftime("%H:%M")

            if currentDay == 3:
                data["thuOpen"] = venue.thuOpen.strftime("%H:%M")
                data["thuClose"] = venue.thuClose.strftime("%H:%M")

            if currentDay == 4:
                data["friOpen"] = venue.friOpen.strftime("%H:%M")
                data["friClose"] = venue.friClose.strftime("%H:%M")

            if currentDay == 5:
                data["satOpen"] = venue.satOpen.strftime("%H:%M")
                data["satClose"] = venue.satClose.strftime("%H:%M")

            if currentDay == 6:
                data["sunOpen"] = venue.sunOpen.strftime("%H:%M")
                data["sunClose"] = venue.sunClose.strftime("%H:%M")

            output.append(data)

        return jsonify(output)
    
    # def save_venue(self, venue):
    #         # TODO IMPLEMENT
    #     venue_id = venue.save()
    #     data = {
    #         "success": True
    #     }

    #     print("data", data)
    #     return jsonify(data)

    def create_venue(self, venue, description, venueURL, venueCity, venueIcon, monOpen, monClose, tueOpen, tueClose, wedOpen, wedClose, thuOpen, thuClose, friOpen, friClose, satOpen, satClose, sunOpen, sunClose):
        # create a shoe
        print(venue, description, venueURL, venueCity, venueIcon, monOpen, monClose, tueOpen, tueClose, wedOpen, wedClose, thuOpen, thuClose, friOpen, friClose, satOpen, satClose, sunOpen, sunClose)
        
        # below is prefix for icon path
        # ../../static/assets/venueIcons/
        venueIconAddress = "../../static/assets/venueIcons/" + venueIcon
        venue = Venue(venue=venue, description=description, venueURL=venueURL, venueCity=venueCity, venueIcon=venueIconAddress, monOpen=timeify(monOpen), monClose=timeify(monClose), tueOpen=timeify(tueOpen), tueClose=timeify(tueClose), wedOpen=timeify(wedOpen), wedClose=timeify(wedClose), thuOpen=timeify(thuOpen), thuClose=timeify(thuClose), friOpen=timeify(friOpen), friClose=timeify(friClose), satOpen=timeify(satOpen), satClose=timeify(satClose), sunOpen=timeify(sunOpen), sunClose=timeify(sunClose))
        venue_id = venue.save()
        # give this object back to the client
        data = {
            "venueID": venue_id
        }
        return jsonify(data)

    def delete_Venue(self, id):
        Venue.delete(id)

        data = {
            "success": True
        }
        return jsonify(data)

admin_controller = AdminController()