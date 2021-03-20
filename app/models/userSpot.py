from app import db
import datetime

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


    def getSpotVenue(venueID, date):
        return db.session.query(Spot).filter(Spot.venueID == venueID, Spot.date == date).all()

    def getSpotUser(userID, date):
        return db.session.query(Spot).filter(Spot.userID == userID, Spot.date == date).all()

    def getSpotsByID(userID):
        return db.session.query(Spot).filter(Spot.userID == userID).all()

    def getByUserID(date, userID, timeSlot):
        return db.session.query(Spot).filter(Spot.userID == userID, Spot.date == date, Spot.timeSlot == timeSlot).first()

    def getLatestSpot(userID, date):
        spots = db.session.query(Spot).filter(Spot.userID == userID, Spot.date == date).all()
        # allSpots = 
        latestSpot = None
        if len(spots) != 0:

            for spot in spots:

                if latestSpot == None:
                    latestSpot = spot
                else:
                    if int(latestSpot.timeSlot[0:2]) < int(spot.timeSlot[0:2]):
                        latestSpot = spot

            return latestSpot

        return -1


