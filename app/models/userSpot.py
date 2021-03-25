from app import db
from datetime import datetime

class Spot(db.Model):
    userID =  db.Column(db.Integer, primary_key=True)
    venueID =  db.Column(db.Integer)
    date = db.Column(db.VARCHAR(8), primary_key=True)
    timeSlot = db.Column(db.VARCHAR(8), primary_key=True)
    arrived = db.Column(db.Boolean)
    

    def save(self):
        db.session.add(self)
        db.session.commit()

        return self.venueID

    #READ
    def get_all():
        return Spot.query.all()


    def get_spot_venue(venueID, date):
        return db.session.query(Spot).filter(Spot.venueID == venueID, Spot.date == date).all()

    def get_spot_user(userID, date):
        return db.session.query(Spot).filter(Spot.userID == userID, Spot.date == date).all()

    def get_spots_by_ID(userID):
        return db.session.query(Spot).filter(Spot.userID == userID).all()

    def get_by_user_ID(date, userID, timeSlot):
        return db.session.query(Spot).filter(Spot.userID == userID, Spot.date == date, Spot.timeSlot == timeSlot).first()

    def get_latest_spot(userID, date=datetime.today().strftime('%m/%d/%Y')):
        spots = db.session.query(Spot).filter(Spot.userID == userID, Spot.date == date).all()
        latestSpot = None
        if len(spots) != 0:
            for spot in spots:
                if latestSpot == None:
                    latestSpot = spot
                else:
                    if int(latestSpot.timeSlot[0:2]) == int(spot.timeSlot[0:2]):
                        if int(latestSpot.timeSlot[3:4]) < int(spot.timeSlot[3:4]):
                            latestSpot = spot
                    elif int(spot.timeSlot[0:2]) < 5:
                        if int(latestSpot.timeSlot[0:2]) < 5:
                            if int(latestSpot.timeSlot[0:2]) < int(spot.timeSlot[0:2]):
                                latestSpot = spot
                        else:
                            latestSpot = spot
                    elif int(latestSpot.timeSlot[0:2]) >= 5 and int(latestSpot.timeSlot[0:2]) < int(spot.timeSlot[0:2]):
                        latestSpot = spot

            return latestSpot
            
        return -1


