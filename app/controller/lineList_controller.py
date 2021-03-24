from flask import render_template, jsonify, redirect, url_for
from datetime import time, datetime, timedelta

from app import db

from app.models import Venue, Lines, Spot
from app.controller.userLines_controller import user_lines_controller

def timeify(timeString):
    x = timeString.partition(':')

    return time(int(x[0]), int(x[2]))

class LineListController(object):

    def create_Spot(self, venue_id, user_id, time_slot):
        # Creates a new vanue and a linelist for today and tomorrows date
        spot = Spot(venue_id = venue_id, user_id = user_id, date = datetime.today().strftime('%m/%d/%Y'), time_slot = time_slot, arrived = False)
        spot_id = spot.save()
        # returns and displays the following information if successful
        data = {
            "venue_id": spot_id,
            "time" : spot.time_slot
        }
        return jsonify(data)

    def index(self):
        return render_template("lineList/index.html")

    def home(self):
        return render_template("lineList/home.html")

    
    def line_up (self, line_time, venue_id, venue_close):
        # reduces the occupency of the chosen time if it is no already 0
        # will determine if the chosen time is today or early morning tomorrow
        if Spot.get_by_user_id(datetime.today().strftime('%m/%d/%Y'), 1, line_time) is None:

            #determins if the time chosen is for today or early morning tomorrow
            if int(line_time[0 : 2 ]) <= int(venue_close[0 : 2 ]) and int(venue_close[0 : 2 ]) < 10:
                tomorrow = datetime.today() + timedelta(days=1)
                the_line = Lines.get_line(venue_id, tomorrow.strftime('%m/%d/%Y'))
            else:
                the_line = Lines.get_line(venue_id, datetime.today().strftime('%m/%d/%Y'))
            
            # then reduced the occupancy of that time by 1 if it is not already 0
            if line_time == "00:00" and the_line.x00000030 != 0:
                the_line.x00000030 = the_line.x00000030 - 1
            elif line_time == "00:30" and the_line.x00300100 != 0:
                the_line.x00300100 = the_line.x00300100 - 1        
            elif line_time == "01:00" and the_line.x01000130 != 0:
                the_line.x01000130 = the_line.x01000130 - 1        
            elif line_time == "01:30" and the_line.x01300200 != 0:
                the_line.x01300200 = the_line.x01300200 - 1        
            elif line_time == "02:00" and the_line.x02000230 != 0:
                the_line.x02000230 = the_line.x02000230 - 1        
            elif line_time == "02:30" and the_line.x02300300 != 0:
                the_line.x02300300 = the_line.x02300300 - 1        
            elif line_time == "03:00" and the_line.x03000330 != 0:
                the_line.x03000330 = the_line.x03000330 - 1        
            elif line_time == "03:30" and the_line.x03300400 != 0:
                the_line.x03300400 = the_line.x03300400 - 1        
            elif line_time == "04:00" and the_line.x04000430 != 0:
                the_line.x04000430 = the_line.x04000430 - 1        
            elif line_time == "04:30" and the_line.x04300500 != 0:
                the_line.x04300500 = the_line.x04300500 - 1        
            elif line_time == "05:00" and the_line.x05000530 != 0:
                the_line.x05000530 = the_line.x05000530 - 1        
            elif line_time == "05:30" and the_line.x05300600 != 0:
                the_line.x05300600 = the_line.x05300600 - 1        
            elif line_time == "06:00" and the_line.x06000630 != 0:
                the_line.x06000630 = the_line.x06000630 - 1        
            elif line_time == "06:30" and the_line.x06300700 != 0:
                the_line.x06300700 = the_line.x06300700 - 1        
            elif line_time == "07:00" and the_line.x07000730 != 0:
                the_line.x07000730 = the_line.x07000730 - 1        
            elif line_time == "07:30" and the_line.x07300800 != 0:
                the_line.x07300800 = the_line.x07300800 - 1        
            elif line_time == "08:00" and the_line.x08000830 != 0:
                the_line.x08000830 = the_line.x08000830 - 1        
            elif line_time == "08:30" and the_line.x08300900 != 0:
                the_line.x08300900 = the_line.x08300900 - 1        
            elif line_time == "09:00" and the_line.x09000930 != 0:
                the_line.x09000930 = the_line.x09000930 - 1        
            elif line_time == "09:30" and the_line.x09301000 != 0:
                the_line.x09301000 = the_line.x09301000 - 1        
            elif line_time == "10:00" and the_line.x10001030 != 0:
                the_line.x10001030 = the_line.x10001030 - 1        
            elif line_time == "10:30" and the_line.x10301100 != 0:
                the_line.x10301100 = the_line.x10301100 - 1        
            elif line_time == "11:00" and the_line.x11001130 != 0:
                the_line.x11001130 = the_line.x11001130 - 1        
            elif line_time == "11:30" and the_line.x11301200 != 0:
                the_line.x11301200 = the_line.x11301200 - 1        
            elif line_time == "12:00" and the_line.x12001230 != 0:
                the_line.x12001230 = the_line.x12001230 - 1        
            elif line_time == "12:30" and the_line.x12301300 != 0:
                the_line.x12301300 = the_line.x12301300 - 1        
            elif line_time == "13:00" and the_line.x13001330 != 0:
                the_line.x13001330 = the_line.x13001330 - 1        
            elif line_time == "13:30" and the_line.x13301400 != 0:
                the_line.x13301400 = the_line.x13301400 - 1        
            elif line_time == "14:00" and the_line.x14001430 != 0:
                the_line.x14001430 = the_line.x14001430 - 1        
            elif line_time == "14:30" and the_line.x14301500 != 0:
                the_line.x14301500 = the_line.x14301500 - 1        
            elif line_time == "15:00" and the_line.x15001530 != 0:
                the_line.x15001530 = the_line.x15001530 - 1        
            elif line_time == "15:30" and the_line.x15301600 != 0:
                the_line.x15301600 = the_line.x15301600 - 1        
            elif line_time == "16:00" and the_line.x16001630 != 0:
                the_line.x16001630 = the_line.x16001630 - 1        
            elif line_time == "16:30" and the_line.x16301700 != 0:
                the_line.x16301700 = the_line.x16301700 - 1        
            elif line_time == "17:00" and the_line.x17001730 != 0:
                the_line.x17001730 = the_line.x17001730 - 1        
            elif line_time == "17:30" and the_line.x17301800 != 0:
                the_line.x17301800 = the_line.x17301800 - 1        
            elif line_time == "18:00" and the_line.x18001830 != 0:
                the_line.x18001830 = the_line.x18001830 - 1        
            elif line_time == "18:30" and the_line.x18301900 != 0:
                the_line.x18301900 = the_line.x18301900 - 1        
            elif line_time == "19:00" and the_line.x19001930 != 0:
                the_line.x19001930 = the_line.x19001930 - 1        
            elif line_time == "19:30" and the_line.x19302000 != 0:
                the_line.x19302000 = the_line.x19302000 - 1        
            elif line_time == "20:00" and the_line.x20002030 != 0:
                the_line.x20002030 = the_line.x20002030 - 1        
            elif line_time == "20:30" and the_line.x20302100 != 0:
                the_line.x20302100 = the_line.x20302100 - 1        
            elif line_time == "21:00" and the_line.x21002130 != 0:
                the_line.x21002130 = the_line.x21002130 - 1        
            elif line_time == "21:30" and the_line.x21302200 != 0:
                the_line.x21302200 = the_line.x21302200 - 1        
            elif line_time == "22:00" and the_line.x22002230 != 0:
                the_line.x22002230 = the_line.x22002230 - 1        
            elif line_time == "22:30" and the_line.x22302300 != 0:
                the_line.x22302300 = the_line.x22302300 - 1        
            elif line_time == "23:00" and the_line.x23002330 != 0:
                the_line.x23002330 = the_line.x23002330 - 1        
            elif line_time == "23:30" and the_line.x23300000 != 0:
                the_line.x23300000 = the_line.x23300000 - 1 
            else:
                data = {
                    "The following time was not Availible, please go back and try another time: ": line_time
                }
                return jsonify(data)
            # if successful updates the line with reduced value and returns and displays a success message
            the_line.update()

            self.create_Spot(venue_id, 1, line_time)

        # TODO change so it redirects to user lines page if logged in or user login page if not.
        return userLines_controller.First()

    def get_venues(self, venue_name):
        # Searches db for venues with names like venue_name. then returns venue information and all potential lines. 
        venues = Venue.get(venue_name)
        
        # so if any venues were found using venue_name to search 
        if len(venues) != 0:
            output = []
            current_day = datetime.today().weekday()

            # adds all venue information to data object
            for venue in venues:
                
                data = {
                    "venue_id" : venue.venue_id,
                    "venue" : venue.venue,
                    "venue_url": venue.venue_url,
                    "venue_city": venue.venue_city,
                    "venue_icon_address": venue.venueIcon,
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
                line_times = ["00:00 - 00:30", "00:30 - 01:00", "01:00 - 01:30", "01:30 - 02:00", "02:00 - 02:30", "02:30 - 03:00", "03:00 - 03:30", "03:30 - 04:00", "04:00 - 04:30", "04:30 - 05:00", "05:00 - 05:30", "05:30 - 06:00", "06:00 - 06:30", "06:30 - 07:00", "07:00 - 07:30", "07:30 - 08:00", "08:00 - 08:30", "08:30 - 09:00", "09:00 - 09:30", "09:30 - 10:00", "10:00 - 10:30", "10:30 - 11:00", "11:00 - 11:30", "11:30 - 12:00", "12:00 - 12:30", "12:30 - 13:00", "13:00 - 13:30", "13:30 - 14:00", "14:00 - 14:30", "14:30 - 15:00", "15:00 - 15:30", "15:30 - 16:00", "16:00 - 16:30", "16:30 - 17:00", "17:00 - 17:30", "17:30 - 18:00", "18:00 - 18:30", "18:30 - 19:00", "19:00 - 19:30", "19:30 - 20:00", "20:00 - 20:30", "20:30 - 21:00", "21:00 - 21:30", "21:30 - 22:00", "22:00 - 22:30", "22:30 - 23:00", "23:00 - 23:30", "23:30 - 00:00"]
                # a list of today and tomorrows line_time capacities
                todays_line_values = [lines_today.x00000030, lines_today.x00300100, lines_today.x01000130, lines_today.x01300200, lines_today.x02000230, lines_today.x02300300, lines_today.x03000330, lines_today.x03300400, lines_today.x04000430, lines_today.x04300500, lines_today.x05000530, lines_today.x05300600, lines_today.x06000630, lines_today.x06300700, lines_today.x07000730, lines_today.x07300800, lines_today.x08000830, lines_today.x08300900, lines_today.x09000930, lines_today.x09301000, lines_today.x10001030, lines_today.x10301100, lines_today.x11001130, lines_today.x11301200, lines_today.x12001230, lines_today.x12301300, lines_today.x13001330, lines_today.x13301400, lines_today.x14001430, lines_today.x14301500, lines_today.x15001530, lines_today.x15301600, lines_today.x16001630, lines_today.x16301700, lines_today.x17001730, lines_today.x17301800, lines_today.x18001830, lines_today.x18301900, lines_today.x19001930, lines_today.x19302000, lines_today.x20002030, lines_today.x20302100, lines_today.x21002130, lines_today.x21302200, lines_today.x22002230, lines_today.x22302300, lines_today.x23002330, lines_today.x23300000]
                tomorrows_line_values = [lines_tomorrow.x00000030, lines_tomorrow.x00300100, lines_tomorrow.x01000130, lines_tomorrow.x01300200, lines_tomorrow.x02000230, lines_tomorrow.x02300300, lines_tomorrow.x03000330, lines_tomorrow.x03300400, lines_tomorrow.x04000430, lines_tomorrow.x04300500, lines_tomorrow.x05000530, lines_tomorrow.x05300600, lines_tomorrow.x06000630, lines_tomorrow.x06300700, lines_tomorrow.x07000730, lines_tomorrow.x07300800, lines_tomorrow.x08000830, lines_tomorrow.x08300900, lines_tomorrow.x09000930, lines_tomorrow.x09301000, lines_tomorrow.x10001030, lines_tomorrow.x10301100, lines_tomorrow.x11001130, lines_tomorrow.x11301200, lines_tomorrow.x12001230, lines_tomorrow.x12301300, lines_tomorrow.x13001330, lines_tomorrow.x13301400, lines_tomorrow.x14001430, lines_tomorrow.x14301500, lines_tomorrow.x15001530, lines_tomorrow.x15301600, lines_tomorrow.x16001630, lines_tomorrow.x16301700, lines_tomorrow.x17001730, lines_tomorrow.x17301800, lines_tomorrow.x18001830, lines_tomorrow.x18301900, lines_tomorrow.x19001930, lines_tomorrow.x19302000, lines_tomorrow.x20002030, lines_tomorrow.x20302100, lines_tomorrow.x21002130, lines_tomorrow.x21302200, lines_tomorrow.x22002230, lines_tomorrow.x22302300, lines_tomorrow.x23002330, lines_tomorrow.x23300000]
                
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

                    # does the current line_time match the opening time.
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

            return render_template("lineList/index.html",  results = output)
        else:
            return render_template("lineList/empty.html")

line_list_controller = LineListController()