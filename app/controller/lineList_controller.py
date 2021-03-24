from flask import render_template, jsonify, redirect, url_for
from datetime import time, datetime, timedelta

from app import db

from app.models import Venue, Lines, Spot
from app.controller.userLines_controller import userLines_controller
from app.controller.admin_controller import admin_controller

def timeify(timeString):
    x = timeString.partition(':')

    return time(int(x[0]), int(x[2]))

class LineListController(object):

    def create_Spot(self, venueID, userID, timeSlot):
        # Creates a new vanue and a linelist for today and tomorrows date
        spot = Spot(venueID = venueID, userID = userID, date = datetime.today().strftime('%m/%d/%Y'), timeSlot = timeSlot, arrived = False)
        spotid = spot.save()
        # returns and displays the following information if successful
        data = {
            "venueID": spotid,
            "time" : spot.timeSlot
        }
        return jsonify(data)

    def index(self):
        return render_template("lineList/index.html")

    def home(self):
        return render_template("lineList/home.html")

    
    def lineUp (self, lineTime, venueID, venueClose):
        # reduces the occupency of the chosen time if it is not already 0
        # will determine if the chosen time is today or early morning tomorrow
        if Spot.getByUserID(datetime.today().strftime('%m/%d/%Y'), 1, lineTime) is None:

            #determins if the time chosen is for today or early morning tomorrow
            if int(lineTime[0 : 2 ]) <= int(venueClose[0 : 2 ]) and int(venueClose[0 : 2 ]) < 10:
                tomorrow = datetime.today() + timedelta(days=1)
                theLine = Lines.getLine(venueID, tomorrow.strftime('%m/%d/%Y'))
            else:
                theLine = Lines.getLine(venueID, datetime.today().strftime('%m/%d/%Y'))
            
            # then reduced the occupancy of that time by 1 if it is not already 0
            if lineTime == "00:00" and theLine.x00000030 != 0:
                theLine.x00000030 = theLine.x00000030 - 1
            elif lineTime == "00:30" and theLine.x00300100 != 0:
                theLine.x00300100 = theLine.x00300100 - 1        
            elif lineTime == "01:00" and theLine.x01000130 != 0:
                theLine.x01000130 = theLine.x01000130 - 1        
            elif lineTime == "01:30" and theLine.x01300200 != 0:
                theLine.x01300200 = theLine.x01300200 - 1        
            elif lineTime == "02:00" and theLine.x02000230 != 0:
                theLine.x02000230 = theLine.x02000230 - 1        
            elif lineTime == "02:30" and theLine.x02300300 != 0:
                theLine.x02300300 = theLine.x02300300 - 1        
            elif lineTime == "03:00" and theLine.x03000330 != 0:
                theLine.x03000330 = theLine.x03000330 - 1        
            elif lineTime == "03:30" and theLine.x03300400 != 0:
                theLine.x03300400 = theLine.x03300400 - 1        
            elif lineTime == "04:00" and theLine.x04000430 != 0:
                theLine.x04000430 = theLine.x04000430 - 1        
            elif lineTime == "04:30" and theLine.x04300500 != 0:
                theLine.x04300500 = theLine.x04300500 - 1        
            elif lineTime == "05:00" and theLine.x05000530 != 0:
                theLine.x05000530 = theLine.x05000530 - 1        
            elif lineTime == "05:30" and theLine.x05300600 != 0:
                theLine.x05300600 = theLine.x05300600 - 1        
            elif lineTime == "06:00" and theLine.x06000630 != 0:
                theLine.x06000630 = theLine.x06000630 - 1        
            elif lineTime == "06:30" and theLine.x06300700 != 0:
                theLine.x06300700 = theLine.x06300700 - 1        
            elif lineTime == "07:00" and theLine.x07000730 != 0:
                theLine.x07000730 = theLine.x07000730 - 1        
            elif lineTime == "07:30" and theLine.x07300800 != 0:
                theLine.x07300800 = theLine.x07300800 - 1        
            elif lineTime == "08:00" and theLine.x08000830 != 0:
                theLine.x08000830 = theLine.x08000830 - 1        
            elif lineTime == "08:30" and theLine.x08300900 != 0:
                theLine.x08300900 = theLine.x08300900 - 1        
            elif lineTime == "09:00" and theLine.x09000930 != 0:
                theLine.x09000930 = theLine.x09000930 - 1        
            elif lineTime == "09:30" and theLine.x09301000 != 0:
                theLine.x09301000 = theLine.x09301000 - 1        
            elif lineTime == "10:00" and theLine.x10001030 != 0:
                theLine.x10001030 = theLine.x10001030 - 1        
            elif lineTime == "10:30" and theLine.x10301100 != 0:
                theLine.x10301100 = theLine.x10301100 - 1        
            elif lineTime == "11:00" and theLine.x11001130 != 0:
                theLine.x11001130 = theLine.x11001130 - 1        
            elif lineTime == "11:30" and theLine.x11301200 != 0:
                theLine.x11301200 = theLine.x11301200 - 1        
            elif lineTime == "12:00" and theLine.x12001230 != 0:
                theLine.x12001230 = theLine.x12001230 - 1        
            elif lineTime == "12:30" and theLine.x12301300 != 0:
                theLine.x12301300 = theLine.x12301300 - 1        
            elif lineTime == "13:00" and theLine.x13001330 != 0:
                theLine.x13001330 = theLine.x13001330 - 1        
            elif lineTime == "13:30" and theLine.x13301400 != 0:
                theLine.x13301400 = theLine.x13301400 - 1        
            elif lineTime == "14:00" and theLine.x14001430 != 0:
                theLine.x14001430 = theLine.x14001430 - 1        
            elif lineTime == "14:30" and theLine.x14301500 != 0:
                theLine.x14301500 = theLine.x14301500 - 1        
            elif lineTime == "15:00" and theLine.x15001530 != 0:
                theLine.x15001530 = theLine.x15001530 - 1        
            elif lineTime == "15:30" and theLine.x15301600 != 0:
                theLine.x15301600 = theLine.x15301600 - 1        
            elif lineTime == "16:00" and theLine.x16001630 != 0:
                theLine.x16001630 = theLine.x16001630 - 1        
            elif lineTime == "16:30" and theLine.x16301700 != 0:
                theLine.x16301700 = theLine.x16301700 - 1        
            elif lineTime == "17:00" and theLine.x17001730 != 0:
                theLine.x17001730 = theLine.x17001730 - 1        
            elif lineTime == "17:30" and theLine.x17301800 != 0:
                theLine.x17301800 = theLine.x17301800 - 1        
            elif lineTime == "18:00" and theLine.x18001830 != 0:
                theLine.x18001830 = theLine.x18001830 - 1        
            elif lineTime == "18:30" and theLine.x18301900 != 0:
                theLine.x18301900 = theLine.x18301900 - 1        
            elif lineTime == "19:00" and theLine.x19001930 != 0:
                theLine.x19001930 = theLine.x19001930 - 1        
            elif lineTime == "19:30" and theLine.x19302000 != 0:
                theLine.x19302000 = theLine.x19302000 - 1        
            elif lineTime == "20:00" and theLine.x20002030 != 0:
                theLine.x20002030 = theLine.x20002030 - 1        
            elif lineTime == "20:30" and theLine.x20302100 != 0:
                theLine.x20302100 = theLine.x20302100 - 1        
            elif lineTime == "21:00" and theLine.x21002130 != 0:
                theLine.x21002130 = theLine.x21002130 - 1        
            elif lineTime == "21:30" and theLine.x21302200 != 0:
                theLine.x21302200 = theLine.x21302200 - 1        
            elif lineTime == "22:00" and theLine.x22002230 != 0:
                theLine.x22002230 = theLine.x22002230 - 1        
            elif lineTime == "22:30" and theLine.x22302300 != 0:
                theLine.x22302300 = theLine.x22302300 - 1        
            elif lineTime == "23:00" and theLine.x23002330 != 0:
                theLine.x23002330 = theLine.x23002330 - 1        
            elif lineTime == "23:30" and theLine.x23300000 != 0:
                theLine.x23300000 = theLine.x23300000 - 1 
            else:
                data = {
                    "The following time was not Availible, please go back and try another time: ": lineTime
                }
                return jsonify(data)
            # if successful updates the line with reduced value and returns and displays a success message
            theLine.update()

            self.create_Spot(venueID, 1, lineTime)

        return userLines_controller.First()

    def build_venue_object(self, venueObj):
        # builds, formats and returns a venue object from a query result object
        currentDay = datetime.today().weekday()

        data = {
            "venueID" : venueObj.venueID,
            "venue" : venueObj.venue,
            "venueURL": venueObj.venueURL,
            "venueCity": venueObj.venueCity,
            "venueIconAddress": venueObj.venueIcon,
            "desc" : venueObj.description,
            "lines" : [],
        }
        if currentDay == 0:
            data["yesterdaysClose"] = venueObj.sunClose.strftime("%H:%M")
            data["Open"] = venueObj.monOpen.strftime("%H:%M")
            data["Close"] = venueObj.monClose.strftime("%H:%M")

        if currentDay == 1:
            data["yesterdaysClose"] = venueObj.monClose.strftime("%H:%M")
            data["Open"] = venueObj.tueOpen.strftime("%H:%M")
            data["Close"] = venueObj.tueClose.strftime("%H:%M")

        if currentDay == 2:
            data["yesterdaysClose"] = venueObj.tueClose.strftime("%H:%M")
            data["Open"] = venueObj.wedOpen.strftime("%H:%M")
            data["Close"] = venueObj.wedClose.strftime("%H:%M")

        if currentDay == 3:
            data["yesterdaysClose"] = venueObj.wedClose.strftime("%H:%M")
            data["Open"] = venueObj.thuOpen.strftime("%H:%M")
            data["Close"] = venueObj.thuClose.strftime("%H:%M")

        if currentDay == 4:
            data["yesterdaysClose"] = venueObj.thuClose.strftime("%H:%M")
            data["Open"] = venueObj.friOpen.strftime("%H:%M")
            data["Close"] = venueObj.friClose.strftime("%H:%M")

        if currentDay == 5:
            data["yesterdaysClose"] = venueObj.friClose.strftime("%H:%M")
            data["Open"] = venueObj.satOpen.strftime("%H:%M")
            data["Close"] = venueObj.satClose.strftime("%H:%M")

        if currentDay == 6:
            data["yesterdaysClose"] = venueObj.satClose.strftime("%H:%M")
            data["Open"] = venueObj.sunOpen.strftime("%H:%M")
            data["Close"] = venueObj.sunClose.strftime("%H:%M")

        return data

    def get_venues_line_times_list(self, venueObj, isTomorrow = False):
        # Returns the requested list. if it doesn't exist, create it.
        day = datetime.today()

        if isTomorrow == True:
            day = day + timedelta(days=1)

        lines = Lines.getLine(venueObj.venueID, day.strftime('%m/%d/%Y'))

        if lines is None:
            admin_controller.create_list(venueObj.venueID, venueObj.lineCapacity)
            lines = Lines.getLine(venueObj.venueID, datetime.today().strftime('%m/%d/%Y'))
        
        return lines

    def create_list_of_lines(self, open, close, todays_line_list, tomorrows_line_list):
        # generates a list of availible line times based on the open, close and current time.
        # ONLY returns line times that are withing opening and closing time and that have a capacity greater than 0
        # note because the closing time can be on the next day, confirms capacity for tomorrows linelist if necessary
        # open and close time should be formatted like 9:00

        # helper variables use in for loop below
        start_iter = False
        start_open = False
        # container for early morning times from midnight till closing
        end_times = []
        #container for from opening to closing
        start_times = []

        print(datetime.today().strftime('%H'))

        # a list of all potenital line times in a day
        line_times = ["00:00 - 00:30", "00:30 - 01:00", "01:00 - 01:30", "01:30 - 02:00", "02:00 - 02:30", "02:30 - 03:00", "03:00 - 03:30", "03:30 - 04:00", "04:00 - 04:30", "04:30 - 05:00", "05:00 - 05:30", "05:30 - 06:00", "06:00 - 06:30", "06:30 - 07:00", "07:00 - 07:30", "07:30 - 08:00", "08:00 - 08:30", "08:30 - 09:00", "09:00 - 09:30", "09:30 - 10:00", "10:00 - 10:30", "10:30 - 11:00", "11:00 - 11:30", "11:30 - 12:00", "12:00 - 12:30", "12:30 - 13:00", "13:00 - 13:30", "13:30 - 14:00", "14:00 - 14:30", "14:30 - 15:00", "15:00 - 15:30", "15:30 - 16:00", "16:00 - 16:30", "16:30 - 17:00", "17:00 - 17:30", "17:30 - 18:00", "18:00 - 18:30", "18:30 - 19:00", "19:00 - 19:30", "19:30 - 20:00", "20:00 - 20:30", "20:30 - 21:00", "21:00 - 21:30", "21:30 - 22:00", "22:00 - 22:30", "22:30 - 23:00", "23:00 - 23:30", "23:30 - 00:00"]
        
        # a list of today and tomorrows linetime capacities
        todays_lineValues = [todays_line_list.x00000030, todays_line_list.x00300100, todays_line_list.x01000130, todays_line_list.x01300200, todays_line_list.x02000230, todays_line_list.x02300300, todays_line_list.x03000330, todays_line_list.x03300400, todays_line_list.x04000430, todays_line_list.x04300500, todays_line_list.x05000530, todays_line_list.x05300600, todays_line_list.x06000630, todays_line_list.x06300700, todays_line_list.x07000730, todays_line_list.x07300800, todays_line_list.x08000830, todays_line_list.x08300900, todays_line_list.x09000930, todays_line_list.x09301000, todays_line_list.x10001030, todays_line_list.x10301100, todays_line_list.x11001130, todays_line_list.x11301200, todays_line_list.x12001230, todays_line_list.x12301300, todays_line_list.x13001330, todays_line_list.x13301400, todays_line_list.x14001430, todays_line_list.x14301500, todays_line_list.x15001530, todays_line_list.x15301600, todays_line_list.x16001630, todays_line_list.x16301700, todays_line_list.x17001730, todays_line_list.x17301800, todays_line_list.x18001830, todays_line_list.x18301900, todays_line_list.x19001930, todays_line_list.x19302000, todays_line_list.x20002030, todays_line_list.x20302100, todays_line_list.x21002130, todays_line_list.x21302200, todays_line_list.x22002230, todays_line_list.x22302300, todays_line_list.x23002330, todays_line_list.x23300000]
        tomorrows_lineValues = [tomorrows_line_list.x00000030, tomorrows_line_list.x00300100, tomorrows_line_list.x01000130, tomorrows_line_list.x01300200, tomorrows_line_list.x02000230, tomorrows_line_list.x02300300, tomorrows_line_list.x03000330, tomorrows_line_list.x03300400, tomorrows_line_list.x04000430, tomorrows_line_list.x04300500, tomorrows_line_list.x05000530, tomorrows_line_list.x05300600, tomorrows_line_list.x06000630, tomorrows_line_list.x06300700, tomorrows_line_list.x07000730, tomorrows_line_list.x07300800, tomorrows_line_list.x08000830, tomorrows_line_list.x08300900, tomorrows_line_list.x09000930, tomorrows_line_list.x09301000, tomorrows_line_list.x10001030, tomorrows_line_list.x10301100, tomorrows_line_list.x11001130, tomorrows_line_list.x11301200, tomorrows_line_list.x12001230, tomorrows_line_list.x12301300, tomorrows_line_list.x13001330, tomorrows_line_list.x13301400, tomorrows_line_list.x14001430, tomorrows_line_list.x14301500, tomorrows_line_list.x15001530, tomorrows_line_list.x15301600, tomorrows_line_list.x16001630, tomorrows_line_list.x16301700, tomorrows_line_list.x17001730, tomorrows_line_list.x17301800, tomorrows_line_list.x18001830, tomorrows_line_list.x18301900, tomorrows_line_list.x19001930, tomorrows_line_list.x19302000, tomorrows_line_list.x20002030, tomorrows_line_list.x20302100, tomorrows_line_list.x21002130, tomorrows_line_list.x21302200, tomorrows_line_list.x22002230, tomorrows_line_list.x22302300, tomorrows_line_list.x23002330, tomorrows_line_list.x23300000]
        
        def is_after_curr_time(line_time):
            # checks to see if the linetime is past the current time
            if int(datetime.today().strftime('%H')) <= int(line_time[0:2]):

                if datetime.today().strftime('%H') == line_time[0:2] and int(datetime.today().strftime('%M')) < int(line_time[3:5]): 
                    return line_time
                elif datetime.today().strftime('%H') != line_time[0:2]:
                    return line_time
            
            return -1

        #loops through, adding early moring times to end_times first. then adds 
        for i in range(len(line_times)):

            # is closing time for today actually early morning tomorrow.
            if int(close[0:2]) < 10 and line_times[i] == "00:00 - 00:30":
                startiter = True
            
            # if so add every time until closing to the end_times list
            if startiter == True and line_times[i][ 8 : 13 ] != close:
                if tomorrows_lineValues[i] != 0:
                    if is_after_curr_time(line_times[i]) != -1:
                        end_times.append(line_times[i])
            elif startiter == True and line_times[i][ 8 : 13 ] == close:
                if tomorrows_lineValues[i] != 0:
                    if is_after_curr_time(line_times[i]) != -1:
                        end_times.append(line_times[i])
                startiter = False

            # does the current linetime match the opening time.
            if startiter == False and start_open == False and line_times[i][0 : 5] == open:
                start_open = True

            # if so start adding times to data["lines"] until you reach the end of the list or the closing time
            if start_open == True and line_times[i][ 8 : 13 ] != close:
                if todays_lineValues[i] != 0:
                    if is_after_curr_time(line_times[i]) != -1:
                        start_times.append(line_times[i])
            elif start_open == True and line_times[i][ 8 : 13 ] == close:
                if todays_lineValues[i] != 0:
                    if is_after_curr_time(line_times[i]) != -1:
                        start_times.append(line_times[i])
                break

        # if there were items added to the endTimes list add them to the start_times
        if len(end_times) != 0:
            start_times.extend(end_times)
        print(start_times)
        return start_times  


    def get_venues(self, venueName):
        # Searches db for venues with names like venueName. then returns venue information and all potential lines. 
        venues = Venue.get(venueName)
        
        # so if any venues were found using venueName to search 
        if len(venues) != 0:
            output = []

            # adds all venue information to data object
            for venue in venues:
                
                data = self.build_venue_object(venue)
                
                linesToday = self.get_venues_line_times_list(venue)
                linesTomorrow = self.get_venues_line_times_list(venue, isTomorrow=True)

                data["lines"].extend(self.create_list_of_lines(data["Open"], data["Close"], linesToday, linesTomorrow))
                output.append(data)

            return render_template("lineList/index.html",  results=output)
        else:
            return render_template("lineList/empty.html")

lineList_controller = LineListController()