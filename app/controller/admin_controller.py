from flask import render_template, jsonify, redirect, url_for
from datetime import time, datetime, timedelta

from app import db

# as the models file contains all the models, import what you need
# from app.models import Shoe
from app.models import Venue, Lines

def timeify(timeString):
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
        current_day = datetime.today().weekday()
        # formatting the data for the client 
        for venue in venues:
            
            data = {
                "venue-id" : venue.venue_id,
                "venue" : venue.venue,
                "venue-url" : venue.venue_url,
                "venue-city" : venue.venue_city,
                "venue-icon-address" : venue.venue_icon,
                "desc" : venue.description,
                "capacity" : venue.line_capacity,
            }
            # only retrieve the business hours for today
            if current_day == 0:
                data["mon_open"] = venue.mon_open.strftime("%H:%M")
                data["mon_close"] = venue.mon_close.strftime("%H:%M")

            if current_day == 1:
                data["tue_open"] = venue.tue_open.strftime("%H:%M")
                data["tue_close"] = venue.tue_close.strftime("%H:%M")

            if current_day == 2:
                data["wed_open"] = venue.wed_open.strftime("%H:%M")
                data["wed_close"] = venue.wed_close.strftime("%H:%M")

            if current_day == 3:
                data["thu_open"] = venue.thu_open.strftime("%H:%M")
                data["thu_close"] = venue.thu_close.strftime("%H:%M")

            if current_day == 4:
                data["fri_open"] = venue.fri_open.strftime("%H:%M")
                data["fri_close"] = venue.fri_close.strftime("%H:%M")

            if current_day == 5:
                data["sat_open"] = venue.sat_open.strftime("%H:%M")
                data["sat_close"] = venue.sat_close.strftime("%H:%M")

            if current_day == 6:
                data["sun_open"] = venue.sun_open.strftime("%H:%M")
                data["sun_close"] = venue.sun_close.strftime("%H:%M")

            output.append(data)

        for line in lines:
            # retrieves all line times and their current capacity (whether the timeslot is used or not)
            data = {
                "venue_id" : line.venue_id,
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
    
    def create_list(self, venue_id, capacity, the_date=datetime.today().strftime('%m/%d/%Y'), is_tomorrow=False):
        # creates an instance of a Line list for a venue for a specific date. the x00000030 values can be translated as: (x)(00:00)(00:30)
        if is_tomorrow == True:
            date = (datetime.today() + timedelta(days=1)).strftime('%m/%d/%Y')
        else: 
            date = the_date

        if Venue.get_by_id(venue_id) and Lines.get_line(venue_id, date) is None:
            l_list = Lines(
                venue_id = venue_id, 
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
            venue_name = l_list.save()
            # returns and displays the following information if successful
            data = {
                "venue list created for venue ID": venue_id
            }
        else:
            # returns and displays the following information if NOT successful
            data = {
                "Sorry The following venue ID does not exist or it already has a line created: ": venue_id
            }
        return jsonify(data)
    
    def create_venue(self, venue, description, venue_url, venue_city, venue_icon, mon_open, mon_close, tue_open, tue_close, 
    wed_open, wed_close, thu_open, thu_close, fri_open, fri_close, sat_open, sat_close, sun_open, sun_close, line_capacity):        
        # Creates a new vanue and a linelist for today and tomorrows date
        venue_icon_address = "../../static/assets/venue_icons/" + venue_icon
        venue = Venue(venue=venue, description=description, venue_url=venue_url, venue_city=venue_city, venue_icon=venue_icon_address, 
        mon_open=timeify(mon_open), mon_close=timeify(mon_close), tue_open=timeify(tue_open), tue_close=timeify(tue_close), wed_open=timeify(wed_open), 
        wed_close=timeify(wed_close), thu_open=timeify(thu_open), thu_close=timeify(thu_close), fri_open=timeify(fri_open), fri_close=timeify(fri_close), 
        sat_open=timeify(sat_open), sat_close=timeify(sat_close), sun_open=timeify(sun_open), sun_close=timeify(sun_close), line_capacity=line_capacity)
        venue_id = venue.save()
        self.create_list(venue_id, line_capacity)
        tomorrow = datetime.today() + timedelta(days=1)
        self.create_list(venue_id, line_capacity, tomorrow.strftime('%m/%d/%Y') )

        # returns and displays the following information if successful
        data = {
            "venue_id": venue_id
        }
        return jsonify(data)

    def delete_venue(self, id):
        Venue.delete(id)
        Lines.delete_by_id(id)
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