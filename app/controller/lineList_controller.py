from flask import render_template, jsonify
from datetime import time, datetime, timedelta

from app import db

from app.models import Venue, Lines

def timeify(timeString):
    x = timeString.partition(':')

    return time(int(x[0]), int(x[2]))

class LineListController(object):
    def index(self):
        return render_template("lineList/index.html")

    def home(self):
        return render_template("lineList/home.html")
    
    def lineUp (self, lineTime, venueID, venueClose):
        #check if venue closes the next day and if the time chosen falls into the early morning
        #then gets the appropriate days line to change occupency
        
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
                "did't update the following time slot ": lineTime
            }
            return jsonify(data)
        theLine.update()
        data = {
                "following time slot reduced by 1 ": lineTime
            }
        return jsonify(data)

    def get_venues(self, venueName):
        venues = Venue.get(venueName)
        

        if len(venues) != 0:
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

                print("---------------venue id-------------------")
                print(venue.venueID)
                print("-----------date----------")
                print(datetime.today())
                linesToday = Lines.getLine(venue.venueID, datetime.today().strftime('%m/%d/%Y'))
                tomorrow = datetime.today() + timedelta(days=1)
                print(tomorrow)
                linesTomorrow = Lines.getLine(venue.venueID, tomorrow.strftime('%m/%d/%Y'))
                startiter = False
                startOpen = False
                endTimes = []
                lineTimes = ["00:00 - 00:30", "00:30 - 01:00", "01:00 - 01:30", "01:30 - 02:00", "02:00 - 02:30", "02:30 - 03:00", "03:00 - 03:30", "03:30 - 04:00", "04:00 - 04:30", "04:30 - 05:00", "05:00 - 05:30", "05:30 - 06:00", "06:00 - 06:30", "06:30 - 07:00", "07:00 - 07:30", "07:30 - 08:00", "08:00 - 08:30", "08:30 - 09:00", "09:00 - 09:30", "09:30 - 10:00", "10:00 - 10:30", "10:30 - 11:00", "11:00 - 11:30", "11:30 - 12:00", "12:00 - 12:30", "12:30 - 13:00", "13:00 - 13:30", "13:30 - 14:00", "14:00 - 14:30", "14:30 - 15:00", "15:00 - 15:30", "15:30 - 16:00", "16:00 - 16:30", "16:30 - 17:00", "17:00 - 17:30", "17:30 - 18:00", "18:00 - 18:30", "18:30 - 19:00", "19:00 - 19:30", "19:30 - 20:00", "20:00 - 20:30", "20:30 - 21:00", "21:00 - 21:30", "21:30 - 22:00", "22:00 - 22:30", "22:30 - 23:00", "23:00 - 23:30", "23:30 - 00:00"]
                todaysLineValues = [linesToday.x00000030, linesToday.x00300100, linesToday.x01000130, linesToday.x01300200, linesToday.x02000230, linesToday.x02300300, linesToday.x03000330, linesToday.x03300400, linesToday.x04000430, linesToday.x04300500, linesToday.x05000530, linesToday.x05300600, linesToday.x06000630, linesToday.x06300700, linesToday.x07000730, linesToday.x07300800, linesToday.x08000830, linesToday.x08300900, linesToday.x09000930, linesToday.x09301000, linesToday.x10001030, linesToday.x10301100, linesToday.x11001130, linesToday.x11301200, linesToday.x12001230, linesToday.x12301300, linesToday.x13001330, linesToday.x13301400, linesToday.x14001430, linesToday.x14301500, linesToday.x15001530, linesToday.x15301600, linesToday.x16001630, linesToday.x16301700, linesToday.x17001730, linesToday.x17301800, linesToday.x18001830, linesToday.x18301900, linesToday.x19001930, linesToday.x19302000, linesToday.x20002030, linesToday.x20302100, linesToday.x21002130, linesToday.x21302200, linesToday.x22002230, linesToday.x22302300, linesToday.x23002330, linesToday.x23300000]
                tomorrowsLineValues = [linesTomorrow.x00000030, linesTomorrow.x00300100, linesTomorrow.x01000130, linesTomorrow.x01300200, linesTomorrow.x02000230, linesTomorrow.x02300300, linesTomorrow.x03000330, linesTomorrow.x03300400, linesTomorrow.x04000430, linesTomorrow.x04300500, linesTomorrow.x05000530, linesTomorrow.x05300600, linesTomorrow.x06000630, linesTomorrow.x06300700, linesTomorrow.x07000730, linesTomorrow.x07300800, linesTomorrow.x08000830, linesTomorrow.x08300900, linesTomorrow.x09000930, linesTomorrow.x09301000, linesTomorrow.x10001030, linesTomorrow.x10301100, linesTomorrow.x11001130, linesTomorrow.x11301200, linesTomorrow.x12001230, linesTomorrow.x12301300, linesTomorrow.x13001330, linesTomorrow.x13301400, linesTomorrow.x14001430, linesTomorrow.x14301500, linesTomorrow.x15001530, linesTomorrow.x15301600, linesTomorrow.x16001630, linesTomorrow.x16301700, linesTomorrow.x17001730, linesTomorrow.x17301800, linesTomorrow.x18001830, linesTomorrow.x18301900, linesTomorrow.x19001930, linesTomorrow.x19302000, linesTomorrow.x20002030, linesTomorrow.x20302100, linesTomorrow.x21002130, linesTomorrow.x21302200, linesTomorrow.x22002230, linesTomorrow.x22302300, linesTomorrow.x23002330, linesTomorrow.x23300000]
                
                for i in range(len(lineTimes)):
                    
                    if int(data["Close"][0:2]) < 12 and lineTimes[i] == "00:00 - 00:30":
                        startiter = True
                    
                    if startiter == True and lineTimes[i][ 8 : 13 ] != data["Close"]:
                        if tomorrowsLineValues[i] != 0:
                            endTimes.append(lineTimes[i])
                    elif lineTimes[i][ 8 : 13 ] == data["Close"]:
                        if tomorrowsLineValues[i] != 0:
                            endTimes.append(lineTimes[i])
                        startiter = False


                    if startiter == False and startOpen == False and lineTimes[i][0 : 5] == data["Open"]:
                        startOpen = True

                    if startOpen == True and lineTimes[i][ 8 : 13 ] != data["Close"]:
                        if todaysLineValues[i] != 0:
                            data["lines"].append(lineTimes[i])
                    elif startOpen == True and lineTimes[i][ 8 : 13 ] == data["Close"]:
                        if todaysLineValues[i] != 0:
                            data["lines"].append(lineTimes[i])
                            print(data["lines"])
                            break

                if len(endTimes) != 0:
                    data["lines"].extend(endTimes)                                    

                
                    # if len(lines) != 0:
                    #     print("--------------------------------------staring linelist jimjam-----------------------------------------")
                    #     print(len(lines))
                    #     for line in lines:
                    #         if line.venueID == venue.venueID:
                    #             print(venue.friOpen.strftime("%H%M"))
                    #             print(line[0])
                    #             data = {
                    #                 "venueID" : line.venueID,
                    #                 "date" : line.date,
                    #                 "00:00 - 00:30" : line.x00000030,
                    #                 "00:30 - 01:00" : line.x00300100,
                    #                 "01:00 - 01:30" : line.x01000130,
                    #                 "01:30 - 02:00" : line.x01300200,
                    #                 "02:00 - 02:30" : line.x02000230,
                    #                 "02:30 - 03:00" : line.x02300300,
                    #                 "03:00 - 03:30" : line.x03000330,
                    #                 "03:30 - 04:00" : line.x03300400,
                    #                 "04:00 - 04:30" : line.x04000430,
                    #                 "04:30 - 05:00" : line.x04300500,
                    #                 "05:00 - 05:30" : line.x05000530,
                    #                 "05:30 - 06:00" : line.x05300600,
                    #                 "06:00 - 06:30" : line.x06000630,
                    #                 "06:30 - 07:00" : line.x06300700,
                    #                 "07:00 - 07:30" : line.x07000730,
                    #                 "07:30 - 08:00" : line.x07300800,
                    #                 "08:00 - 08:30" : line.x08000830,
                    #                 "08:30 - 09:00" : line.x08300900,
                    #                 "09:00 - 09:30" : line.x09000930,
                    #                 "09:30 - 10:00" : line.x09301000,
                    #                 "10:00 - 10:30" : line.x10001030,
                    #                 "10:30 - 11:00" : line.x10301100,
                    #                 "11:00 - 11:30" : line.x11001130,
                    #                 "11:30 - 12:00" : line.x11301200,
                    #                 "12:00 - 12:30" : line.x12001230,
                    #                 "12:30 - 13:00" : line.x12301300,
                    #                 "13:00 - 13:30" : line.x13001330,
                    #                 "13:30 - 14:00" : line.x13301400,
                    #                 "14:00 - 14:30" : line.x14001430,
                    #                 "14:30 - 15:00" : line.x14301500,
                    #                 "15:00 - 15:30" : line.x15001530,
                    #                 "15:30 - 16:00" : line.x15301600,
                    #                 "16:00 - 16:30" : line.x16001630,
                    #                 "16:30 - 17:00" : line.x16301700,
                    #                 "17:00 - 17:30" : line.x17001730,
                    #                 "17:30 - 18:00" : line.x17301800,
                    #                 "18:00 - 18:30" : line.x18001830,
                    #                 "18:30 - 19:00" : line.x18301900,
                    #                 "19:00 - 19:30" : line.x19001930,
                    #                 "19:30 - 20:00" : line.x19302000,
                    #                 "20:00 - 20:30" : line.x20002030,
                    #                 "20:30 - 21:00" : line.x20302100,
                    #                 "21:00 - 21:30" : line.x21002130,
                    #                 "21:30 - 22:00" : line.x21302200,
                    #                 "22:00 - 22:30" : line.x22002230,
                    #                 "22:30 - 23:00" : line.x22302300,
                    #                 "23:00 - 23:30" : line.x23002330,
                    #                 "23:30 - 00:00" : line.x23300000
                    #             }

                output.append(data)

            return render_template("lineList/index.html", results=output)
        else:
            return render_template("lineList/empty.html")

lineList_controller = LineListController()