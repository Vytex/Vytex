from flask import render_template, jsonify, redirect, url_for
from datetime import time, datetime, timedelta

from app import db

from app.models import Venue, Lines

def timeify(timeString):
    # formats string of 4 numbers   ex. from 1230 to 12:30
    x = timeString.partition(':')

    return time(int(x[0]), int(x[2]))

class AdminController(object):
    def index(self):
        # loads admin main page
        return render_template("admin/index.html")

    def get_venues(self):
        # retrieves a list of venues and line lists
        venues = Venue.get_all()
        lines = Lines.get_all()
        output = []
        currentDay = datetime.today().weekday()
        # formatting the data for the client 
        for venue in venues:
            
            data = {
                "venueID" : venue.venueID,
                "venue" : venue.venue,
                "venueURL" : venue.venueURL,
                "venueCity" : venue.venueCity,
                "venueIconAddress" : venue.venueIcon,
                "desc" : venue.description,
                "capacity" : venue.lineCapacity,
            }
            # only retrieve the business hours for today
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

        for line in lines:
            # retrieves all line times and their current capacity (whether the timeslot is used or not)
            data = {
                "venueID" : line.venueID,
                "date" : line.date,
                "00:00 - 00:30" : line.x00000030,
                "00:30 - 01:00" : line.x00300100,
                "01:00 - 01:30" : line.x01000130,
                "01:30 - 02:00" : line.x01300200,
                "02:00 - 02:30" : line.x02000230,
                "02:30 - 03:00" : line.x02300300,
                "03:00 - 03:30" : line.x03000330,
                "03:30 - 04:00" : line.x03300400,
                "04:00 - 04:30" : line.x04000430,
                "04:30 - 05:00" : line.x04300500,
                "05:00 - 05:30" : line.x05000530,
                "05:30 - 06:00" : line.x05300600,
                "06:00 - 06:30" : line.x06000630,
                "06:30 - 07:00" : line.x06300700,
                "07:00 - 07:30" : line.x07000730,
                "07:30 - 08:00" : line.x07300800,
                "08:00 - 08:30" : line.x08000830,
                "08:30 - 09:00" : line.x08300900,
                "09:00 - 09:30" : line.x09000930,
                "09:30 - 10:00" : line.x09301000,
                "10:00 - 10:30" : line.x10001030,
                "10:30 - 11:00" : line.x10301100,
                "11:00 - 11:30" : line.x11001130,
                "11:30 - 12:00" : line.x11301200,
                "12:00 - 12:30" : line.x12001230,
                "12:30 - 13:00" : line.x12301300,
                "13:00 - 13:30" : line.x13001330,
                "13:30 - 14:00" : line.x13301400,
                "14:00 - 14:30" : line.x14001430,
                "14:30 - 15:00" : line.x14301500,
                "15:00 - 15:30" : line.x15001530,
                "15:30 - 16:00" : line.x15301600,
                "16:00 - 16:30" : line.x16001630,
                "16:30 - 17:00" : line.x16301700,
                "17:00 - 17:30" : line.x17001730,
                "17:30 - 18:00" : line.x17301800,
                "18:00 - 18:30" : line.x18001830,
                "18:30 - 19:00" : line.x18301900,
                "19:00 - 19:30" : line.x19001930,
                "19:30 - 20:00" : line.x19302000,
                "20:00 - 20:30" : line.x20002030,
                "20:30 - 21:00" : line.x20302100,
                "21:00 - 21:30" : line.x21002130,
                "21:30 - 22:00" : line.x21302200,
                "22:00 - 22:30" : line.x22002230,
                "22:30 - 23:00" : line.x22302300,
                "23:00 - 23:30" : line.x23002330,
                "23:30 - 00:00" : line.x23300000
            }
            output.append(data)

        return jsonify(output)
    
    def create_list(self, venueID, capacity, theDate=datetime.today().strftime('%m/%d/%Y'), isTomorrow=False):
        # creates an instance of a Line list for a venue for a specific date. the x00000030 values can be translated as: (x)(00:00)(00:30)
        if isTomorrow == True:
            date = (datetime.today() + timedelta(days=1)).strftime('%m/%d/%Y')
        else: 
            date = theDate

        if Venue.getByID(venueID) and Lines.get_line(venueID, date) is None:
            lList = Lines(
                venueID = venueID, 
                date = date, 
                x00000030 = capacity,
                x00300100 = capacity,
                x01000130 = capacity,
                x01300200 = capacity,
                x02000230 = capacity,
                x02300300 = capacity,
                x03000330 = capacity,
                x03300400 = capacity,
                x04000430 = capacity,
                x04300500 = capacity,
                x05000530 = capacity,
                x05300600 = capacity,
                x06000630 = capacity,
                x06300700 = capacity,
                x07000730 = capacity,
                x07300800 = capacity,
                x08000830 = capacity,
                x08300900 = capacity,
                x09000930 = capacity,
                x09301000 = capacity,
                x10001030 = capacity,
                x10301100 = capacity,
                x11001130 = capacity,
                x11301200 = capacity,
                x12001230 = capacity,
                x12301300 = capacity,
                x13001330 = capacity,
                x13301400 = capacity,
                x14001430 = capacity,
                x14301500 = capacity,
                x15001530 = capacity,
                x15301600 = capacity,
                x16001630 = capacity,
                x16301700 = capacity,
                x17001730 = capacity,
                x17301800 = capacity,
                x18001830 = capacity,
                x18301900 = capacity,
                x19001930 = capacity,
                x19302000 = capacity,
                x20002030 = capacity,
                x20302100 = capacity,
                x21002130 = capacity,
                x21302200 = capacity,
                x22002230 = capacity,
                x22302300 = capacity,
                x23002330 = capacity,
                x23300000 = capacity
            )
            venueName = lList.save()
            # returns and displays the following information if successful
            data = {
                "venue list created for venue ID": venueID
            }
        else:
            # returns and displays the following information if NOT successful
            data = {
                "Sorry The following venue ID does not exist or it already has a line created: ": venueID
            }
        return jsonify(data)
    
    def create_venue(self, venue, description, venueURL, venueCity, venueIcon, monOpen, monClose, tueOpen, tueClose, wedOpen, wedClose, thuOpen, thuClose, friOpen, friClose, satOpen, satClose, sunOpen, sunClose, lineCapacity):        
        # Creates a new vanue and a linelist for today and tomorrows date
        venueIconAddress = "../../static/assets/venueIcons/" + venueIcon
        venue = Venue(venue=venue, description=description, venueURL=venueURL, venueCity=venueCity, venueIcon=venueIconAddress, monOpen=timeify(monOpen), monClose=timeify(monClose), tueOpen=timeify(tueOpen), tueClose=timeify(tueClose), wedOpen=timeify(wedOpen), wedClose=timeify(wedClose), thuOpen=timeify(thuOpen), thuClose=timeify(thuClose), friOpen=timeify(friOpen), friClose=timeify(friClose), satOpen=timeify(satOpen), satClose=timeify(satClose), sunOpen=timeify(sunOpen), sunClose=timeify(sunClose), lineCapacity=lineCapacity)
        venue_id = venue.save()
        self.create_list(venue_id, lineCapacity)
        tomorrow = datetime.today() + timedelta(days=1)
        self.create_list(venue_id, lineCapacity, tomorrow.strftime('%m/%d/%Y') )

        # returns and displays the following information if successful
        data = {
            "venueID": venue_id
        }
        return jsonify(data)

    def delete_Venue(self, id):
        Venue.delete(id)
        Lines.delete_by_ID(id)
        data = {
            "success": True
        }
        return jsonify(data)
    
    def delete_line(self, id, date):
        Lines.delete(id, date)
        data = { 
            "success": True
        }
        return jsonify(data)

admin_controller = AdminController()