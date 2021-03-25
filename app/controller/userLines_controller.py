from flask import render_template, jsonify, redirect, url_for, Blueprint, request, flash, session, logging
from flask_login import login_user, login_required, current_user, logout_user

from datetime import time, datetime, timedelta

from app import db

from app.models import Venue, Lines, Spot, User

class UserLinesController(object):
    def index(self):
        if current_user != None and current_user.is_authenticated:
            print(current_user)
            image_file = url_for('static', filename='assets/' + current_user.image_file)
            return render_template("userLines/index.html", image_file=image_file)
        else:
            image_file = url_for('static', filename='assets/profileButtonPlaceholder.jpg')
            return render_template("LogIn/index.html", image_file=image_file)

    def First(self):
        # this takes care of the first time slot.
        currentDay = datetime.today().weekday()
        latest = Spot.getLatestSpot(current_user.id, datetime.today().strftime('%m/%d/%Y'))
        print(latest)
        if latest != -1:
            print("latest!=1")

            venue = Venue.getByID(latest.venueID)
            
            latestSpot = {
                        "venueID" : venue.venueID,
                        "venue" : venue.venue,
                        "venueURL": venue.venueURL,
                        "venueCity": venue.venueCity,
                        "venueIconAddress": venue.venueIcon,
                        "desc" : venue.description,
                        "spot" : latest.timeSlot,
                    }
            if currentDay == 0:
                latestSpot["Open"] = venue.monOpen.strftime("%H:%M")
                latestSpot["Close"] = venue.monClose.strftime("%H:%M")

            if currentDay == 1:
                latestSpot["Open"] = venue.tueOpen.strftime("%H:%M")
                latestSpot["Close"] = venue.tueClose.strftime("%H:%M")

            if currentDay == 2:
                latestSpot["Open"] = venue.wedOpen.strftime("%H:%M")
                latestSpot["Close"] = venue.wedClose.strftime("%H:%M")

            if currentDay == 3:
                latestSpot["Open"] = venue.thuOpen.strftime("%H:%M")
                latestSpot["Close"] = venue.thuClose.strftime("%H:%M")

            if currentDay == 4:
                latestSpot["Open"] = venue.friOpen.strftime("%H:%M")
                latestSpot["Close"] = venue.friClose.strftime("%H:%M")

            if currentDay == 5:
                latestSpot["Open"] = venue.satOpen.strftime("%H:%M")
                latestSpot["Close"] = venue.satClose.strftime("%H:%M")

            if currentDay == 6:
                latestSpot["Open"] = venue.sunOpen.strftime("%H:%M")
                latestSpot["Close"] = venue.sunClose.strftime("%H:%M")
            
            # and now the list of venues in order that you last liked up
            venueHistory = Spot.getSpotsByID(current_user.id)
            output = []

            for VH in venueHistory:
                
                venue = Venue.getByID(VH.venueID)
                    
                data = {
                    "venueID" : venue.venueID,
                    "venue" : venue.venue,
                    "venueURL": venue.venueURL,
                    "venueCity": venue.venueCity,
                    "venueIconAddress": venue.venueIcon,
                    "desc" : venue.description,
                    "lines" : [],
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

                # gets line-list information for that venue. 
                # ONLY returns line times that are withing opening and closing time and that have a capacity greater than 0
                # note because the closing time can be on the next day, confirms capacity for tomorrows linelist if necessary
                linesToday = Lines.getLine(venue.venueID, datetime.today().strftime('%m/%d/%Y'))
                tomorrow = datetime.today() + timedelta(days=1)
                linesTomorrow = Lines.getLine(venue.venueID, tomorrow.strftime('%m/%d/%Y'))
                start_iter = False
                startOpen = False
                endTimes = []
                # a list of all potenital line times in a day
                lineTimes = ["00:00 - 00:30", "00:30 - 01:00", "01:00 - 01:30", "01:30 - 02:00", "02:00 - 02:30", "02:30 - 03:00", "03:00 - 03:30", "03:30 - 04:00", "04:00 - 04:30", "04:30 - 05:00", "05:00 - 05:30", "05:30 - 06:00", "06:00 - 06:30", "06:30 - 07:00", "07:00 - 07:30", "07:30 - 08:00", "08:00 - 08:30", "08:30 - 09:00", "09:00 - 09:30", "09:30 - 10:00", "10:00 - 10:30", "10:30 - 11:00", "11:00 - 11:30", "11:30 - 12:00", "12:00 - 12:30", "12:30 - 13:00", "13:00 - 13:30", "13:30 - 14:00", "14:00 - 14:30", "14:30 - 15:00", "15:00 - 15:30", "15:30 - 16:00", "16:00 - 16:30", "16:30 - 17:00", "17:00 - 17:30", "17:30 - 18:00", "18:00 - 18:30", "18:30 - 19:00", "19:00 - 19:30", "19:30 - 20:00", "20:00 - 20:30", "20:30 - 21:00", "21:00 - 21:30", "21:30 - 22:00", "22:00 - 22:30", "22:30 - 23:00", "23:00 - 23:30", "23:30 - 00:00"]
                # a list of today and tomorrows linetime capacities
                todaysLineValues = [linesToday.x00000030, linesToday.x00300100, linesToday.x01000130, linesToday.x01300200, linesToday.x02000230, linesToday.x02300300, linesToday.x03000330, linesToday.x03300400, linesToday.x04000430, linesToday.x04300500, linesToday.x05000530, linesToday.x05300600, linesToday.x06000630, linesToday.x06300700, linesToday.x07000730, linesToday.x07300800, linesToday.x08000830, linesToday.x08300900, linesToday.x09000930, linesToday.x09301000, linesToday.x10001030, linesToday.x10301100, linesToday.x11001130, linesToday.x11301200, linesToday.x12001230, linesToday.x12301300, linesToday.x13001330, linesToday.x13301400, linesToday.x14001430, linesToday.x14301500, linesToday.x15001530, linesToday.x15301600, linesToday.x16001630, linesToday.x16301700, linesToday.x17001730, linesToday.x17301800, linesToday.x18001830, linesToday.x18301900, linesToday.x19001930, linesToday.x19302000, linesToday.x20002030, linesToday.x20302100, linesToday.x21002130, linesToday.x21302200, linesToday.x22002230, linesToday.x22302300, linesToday.x23002330, linesToday.x23300000]
                tomorrowsLineValues = [linesTomorrow.x00000030, linesTomorrow.x00300100, linesTomorrow.x01000130, linesTomorrow.x01300200, linesTomorrow.x02000230, linesTomorrow.x02300300, linesTomorrow.x03000330, linesTomorrow.x03300400, linesTomorrow.x04000430, linesTomorrow.x04300500, linesTomorrow.x05000530, linesTomorrow.x05300600, linesTomorrow.x06000630, linesTomorrow.x06300700, linesTomorrow.x07000730, linesTomorrow.x07300800, linesTomorrow.x08000830, linesTomorrow.x08300900, linesTomorrow.x09000930, linesTomorrow.x09301000, linesTomorrow.x10001030, linesTomorrow.x10301100, linesTomorrow.x11001130, linesTomorrow.x11301200, linesTomorrow.x12001230, linesTomorrow.x12301300, linesTomorrow.x13001330, linesTomorrow.x13301400, linesTomorrow.x14001430, linesTomorrow.x14301500, linesTomorrow.x15001530, linesTomorrow.x15301600, linesTomorrow.x16001630, linesTomorrow.x16301700, linesTomorrow.x17001730, linesTomorrow.x17301800, linesTomorrow.x18001830, linesTomorrow.x18301900, linesTomorrow.x19001930, linesTomorrow.x19302000, linesTomorrow.x20002030, linesTomorrow.x20302100, linesTomorrow.x21002130, linesTomorrow.x21302200, linesTomorrow.x22002230, linesTomorrow.x22302300, linesTomorrow.x23002330, linesTomorrow.x23300000]
                
                for i in range(len(lineTimes)):
                    
                    # is closing time for today actually early morning tomorrow.
                    if int(data["Close"][0:2]) < 10 and lineTimes[i] == "00:00 - 00:30":
                        start_iter = True
                    
                    # if so add every time until closing to the endtimes list
                    if start_iter == True and lineTimes[i][ 8 : 13 ] != data["Close"]:
                        if tomorrowsLineValues[i] != 0:
                            endTimes.append(lineTimes[i])
                    elif lineTimes[i][ 8 : 13 ] == data["Close"]:
                        if tomorrowsLineValues[i] != 0:
                            endTimes.append(lineTimes[i])
                        start_iter = False

                    # does the current linetime match the opening time.
                    if start_iter == False and startOpen == False and lineTimes[i][0 : 5] == data["Open"]:
                        startOpen = True

                    # if so start adding times to data["lines"] until you reach the end of the list or the closing time
                    if startOpen == True and lineTimes[i][ 8 : 13 ] != data["Close"]:
                        if todaysLineValues[i] != 0:
                            data["lines"].append(lineTimes[i])
                    elif startOpen == True and lineTimes[i][ 8 : 13 ] == data["Close"]:
                        if todaysLineValues[i] != 0:
                            data["lines"].append(lineTimes[i])
                        break

                # if there were items added to the endTimes list add them to the data["lines"]
                if len(endTimes) != 0:
                    data["lines"].extend(endTimes)                                    

                output.append(data)
                output.reverse()
            #process to load profile icon if user logged in
            image_file = url_for('static', filename='assets/' + current_user.image_file)
            return render_template("userLines/index.html", results=output, topResult=latestSpot, image_file=image_file)
        #process to load profile icon if user logged in
        image_file = url_for('static', filename='assets/' + current_user.image_file)
        return render_template("userLines/empty.html",image_file=image_file)

userLines_controller = UserLinesController()
