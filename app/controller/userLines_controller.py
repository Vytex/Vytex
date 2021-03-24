from flask import render_template, jsonify, redirect, url_for
from datetime import time, datetime, timedelta

from app import db

from app.models import Venue, Lines, Spot

class UserLinesController(object):
    def first(self):
        # this takes care of the first time slot.
        current_day = datetime.today().weekday()
        latest = Spot.get_latest_spot(1, datetime.today().strftime('%m/%d/%Y'))
        if latest != -1:

            venue = Venue.get_by_id(latest.venue_id)
            latest_spot = {
                        "venue-id" : venue.venue_id,
                        "venue" : venue.venue,
                        "venue-url": venue.venue_url,
                        "venue-city": venue.venue_city,
                        "venue-icon": venue.venue_icon,
                        "desc" : venue.description,
                        "spot" : latest.time_slot,
                    }
            if current_day == 0:
                latest_spot["Open"] = venue.mon_open.strftime("%H:%M")
                latest_spot["Close"] = venue.mon_close.strftime("%H:%M")

            if current_day == 1:
                latest_spot["Open"] = venue.tue_open.strftime("%H:%M")
                latest_spot["Close"] = venue.tue_close.strftime("%H:%M")

            if current_day == 2:
                latest_spot["Open"] = venue.wed_open.strftime("%H:%M")
                latest_spot["Close"] = venue.wed_close.strftime("%H:%M")

            if current_day == 3:
                latest_spot["Open"] = venue.thu_open.strftime("%H:%M")
                latest_spot["Close"] = venue.thu_close.strftime("%H:%M")

            if current_day == 4:
                latest_spot["Open"] = venue.fri_open.strftime("%H:%M")
                latest_spot["Close"] = venue.fri_close.strftime("%H:%M")

            if current_day == 5:
                latest_spot["Open"] = venue.sat_open.strftime("%H:%M")
                latest_spot["Close"] = venue.sat_close.strftime("%H:%M")

            if current_day == 6:
                latest_spot["Open"] = venue.sun_open.strftime("%H:%M")
                latest_spot["Close"] = venue.sun_close.strftime("%H:%M")
            
            # and now the list of venues in order that you last liked up
            venue_history = Spot.get_spots_by_id(1)
            output = []

            for venue_h in venue_history:
                
                venue = Venue.get_by_id(venue_h.venue_id)
                    
                data = {
                    "venue-id" : venue.venue_id,
                    "venue" : venue.venue,
                    "venue-url": venue.venue_url,
                    "venue-city": venue.venue_city,
                    "venue-icon-address": venue.venue_icon,
                    "desc" : venue.description,
                    "lines" : [],
                }
                if current_day == 0:
                    data["Open"] = venue.mon_open.strftime("%H:%M")
                    data["Close"] = venue.mon_close.strftime("%H:%M")

                if current_day == 1:
                    data["Open"] = venue.tue_open.strftime("%H:%M")
                    data["Close"] = venue.tue_close.strftime("%H:%M")

                if current_day == 2:
                    data["Open"] = venue.wed_open.strftime("%H:%M")
                    data["Close"] = venue.wed_close.strftime("%H:%M")

                if current_day == 3:
                    data["Open"] = venue.thu_open.strftime("%H:%M")
                    data["Close"] = venue.thu_close.strftime("%H:%M")

                if current_day == 4:
                    data["Open"] = venue.fri_open.strftime("%H:%M")
                    data["Close"] = venue.fri_close.strftime("%H:%M")

                if current_day == 5:
                    data["Open"] = venue.sat_open.strftime("%H:%M")
                    data["Close"] = venue.sat_close.strftime("%H:%M")

                if current_day == 6:
                    data["Open"] = venue.sun_open.strftime("%H:%M")
                    data["Close"] = venue.sun_close.strftime("%H:%M")

                # gets line-list information for that venue. 
                # ONLY returns line times that are withing opening and closing time and that have a capacity greater than 0
                # note because the closing time can be on the next day, confirms capacity for tomorrows linelist if necessary
                lines_today = Lines.get_line(venue.venue_id, datetime.today().strftime('%m/%d/%Y'))
                tomorrow = datetime.today() + timedelta(days=1)
                lines_tomorrow = Lines.get_line(venue.venue_id, tomorrow.strftime('%m/%d/%Y'))
                start_iter = False
                start_open = False
                end_times = []
                # a list of all potenital line times in a day
                line_times = ["00:00 - 00:30", "00:30 - 01:00", "01:00 - 01:30", "01:30 - 02:00", "02:00 - 02:30", "02:30 - 03:00", "03:00 - 03:30", 
                "03:30 - 04:00", "04:00 - 04:30", "04:30 - 05:00", "05:00 - 05:30", "05:30 - 06:00", "06:00 - 06:30", "06:30 - 07:00", "07:00 - 07:30",
                 "07:30 - 08:00", "08:00 - 08:30", "08:30 - 09:00", "09:00 - 09:30", "09:30 - 10:00", "10:00 - 10:30", "10:30 - 11:00", "11:00 - 11:30",
                  "11:30 - 12:00", "12:00 - 12:30", "12:30 - 13:00", "13:00 - 13:30", "13:30 - 14:00", "14:00 - 14:30", "14:30 - 15:00", "15:00 - 15:30",
                   "15:30 - 16:00", "16:00 - 16:30", "16:30 - 17:00", "17:00 - 17:30", "17:30 - 18:00", "18:00 - 18:30", "18:30 - 19:00", "19:00 - 19:30",
                    "19:30 - 20:00", "20:00 - 20:30", "20:30 - 21:00", "21:00 - 21:30", "21:30 - 22:00", "22:00 - 22:30", "22:30 - 23:00", "23:00 - 23:30",
                     "23:30 - 00:00"]
                # a list of today and tomorrows linetime capacities
                todays_line_values = [lines_today.x00000030, lines_today.x00300100, lines_today.x01000130, lines_today.x01300200, lines_today.x02000230, 
                lines_today.x02300300, lines_today.x03000330, lines_today.x03300400, lines_today.x04000430, lines_today.x04300500, lines_today.x05000530, 
                lines_today.x05300600, lines_today.x06000630, lines_today.x06300700, lines_today.x07000730, lines_today.x07300800, lines_today.x08000830, 
                lines_today.x08300900, lines_today.x09000930, lines_today.x09301000, lines_today.x10001030, lines_today.x10301100, lines_today.x11001130, 
                lines_today.x11301200, lines_today.x12001230, lines_today.x12301300, lines_today.x13001330, lines_today.x13301400, lines_today.x14001430, 
                lines_today.x14301500, lines_today.x15001530, lines_today.x15301600, lines_today.x16001630, lines_today.x16301700, lines_today.x17001730,
                 lines_today.x17301800, lines_today.x18001830, lines_today.x18301900, lines_today.x19001930, lines_today.x19302000, lines_today.x20002030, 
                 lines_today.x20302100, lines_today.x21002130, lines_today.x21302200, lines_today.x22002230, lines_today.x22302300, lines_today.x23002330, 
                 lines_today.x23300000]

                tomorrows_line_values = [lines_tomorrow.x00000030, lines_tomorrow.x00300100, lines_tomorrow.x01000130, lines_tomorrow.x01300200, 
                lines_tomorrow.x02000230, lines_tomorrow.x02300300, lines_tomorrow.x03000330, lines_tomorrow.x03300400, lines_tomorrow.x04000430, 
                lines_tomorrow.x04300500, lines_tomorrow.x05000530, lines_tomorrow.x05300600, lines_tomorrow.x06000630, lines_tomorrow.x06300700, 
                lines_tomorrow.x07000730, lines_tomorrow.x07300800, lines_tomorrow.x08000830, lines_tomorrow.x08300900, lines_tomorrow.x09000930, 
                lines_tomorrow.x09301000, lines_tomorrow.x10001030, lines_tomorrow.x10301100, lines_tomorrow.x11001130, lines_tomorrow.x11301200, 
                lines_tomorrow.x12001230, lines_tomorrow.x12301300, lines_tomorrow.x13001330, lines_tomorrow.x13301400, lines_tomorrow.x14001430, 
                lines_tomorrow.x14301500, lines_tomorrow.x15001530, lines_tomorrow.x15301600, lines_tomorrow.x16001630, lines_tomorrow.x16301700, 
                lines_tomorrow.x17001730, lines_tomorrow.x17301800, lines_tomorrow.x18001830, lines_tomorrow.x18301900, lines_tomorrow.x19001930, 
                lines_tomorrow.x19302000, lines_tomorrow.x20002030, lines_tomorrow.x20302100, lines_tomorrow.x21002130, lines_tomorrow.x21302200, 
                lines_tomorrow.x22002230, lines_tomorrow.x22302300, lines_tomorrow.x23002330, lines_tomorrow.x23300000]
                
                for i in range(len(line_times)):
                    
                    # is closing time for today actually early morning tomorrow.
                    if int(data["Close"][0:2]) < 10 and line_times[i] == "00:00 - 00:30":
                        start_iter = True
                    
                    # if so add every time until closing to the end_times list
                    if start_iter == True and line_times[i][ 8 : 13 ] != data["Close"]:
                        if tomorrows_line_values[i] != 0:
                            end_times.append(line_times[i])
                    elif line_times[i][ 8 : 13 ] == data["Close"]:
                        if tomorrows_line_values[i] != 0:
                            end_times.append(line_times[i])
                        start_iter = False

                    # does the current linetime match the opening time.
                    if start_iter == False and start_open == False and line_times[i][0 : 5] == data["Open"]:
                        start_open = True

                    # if so start adding times to data["lines"] until you reach the end of the list or the closing time
                    if start_open == True and line_times[i][ 8 : 13 ] != data["Close"]:
                        if todays_line_values[i] != 0:
                            data["lines"].append(line_times[i])
                    elif start_open == True and line_times[i][ 8 : 13 ] == data["Close"]:
                        if todays_line_values[i] != 0:
                            data["lines"].append(line_times[i])
                        break

                # if there were items added to the end_times list add them to the data["lines"]
                if len(end_times) != 0:
                    data["lines"].extend(end_times)                                    

                output.append(data)

            return render_template("userLines/index.html", results = output, top_result = latest_spot)

        return render_template("userLines/index.html")

user_lines_controller = UserLinesController()