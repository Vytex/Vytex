from app import db
import datetime

class Spot(db.Model):
    spotID =  db.Column(db.Integer, primary_key=True)
    venueID =  db.Column(db.Integer, primary_key=True)
    date = db.Column(db.VARCHAR(8), primary_key=True)
    

    def save(self):
        db.session.add(self)
        db.session.commit()

        return self.venueID

    #READ
    def get_all():
        return Spot.query.all()

    def get(venueID):
        venueID = venueID
        todaysdate = datetime.today().strftime('%m/%d/%Y')
        return db.session.query(Spot).filter(Spot.venueID == venueID, Spot.date == todaysdate).first()
   
    def getByDate(date):
        # date formate m/d/Y 11/11/11
        return db.session.query(Spot).filter(Spot.date == date).all()

    def getSpot():
        # helper method used to return a line that matches a specific venueid and date
        # date formate m/d/Y 11/11/11
        return db.session.query(Spot).filter(Spot.venueID == venueID, Spot.date == date).first()

