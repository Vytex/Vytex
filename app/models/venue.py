from app import db
import datetime

class Venue(db.Model):
        
    venueID = db.Column(db.Integer, primary_key=True)
    venue = db.Column(db.NVARCHAR(30))
    description = db.Column(db.NVARCHAR(500))
    venueURL = db.Column(db.VARCHAR(2083))
    venueCity = db.Column(db.NVARCHAR(500))
    venueIcon = db.Column(db.VARCHAR(500))
    
    monOpen = db.Column(db.TIME(4))
    monClose = db.Column(db.TIME(4))

    tueOpen = db.Column(db.TIME(4))
    tueClose = db.Column(db.TIME(4))

    wedOpen = db.Column(db.TIME(4))
    wedClose = db.Column(db.TIME(4))

    thuOpen = db.Column(db.TIME(4))
    thuClose = db.Column(db.TIME(4))

    friOpen = db.Column(db.TIME(4))
    friClose = db.Column(db.TIME(4))

    satOpen = db.Column(db.TIME(4))
    satClose = db.Column(db.TIME(4))

    sunOpen = db.Column(db.TIME(4))
    sunClose = db.Column(db.TIME(4))

    #CREATE
    def save(self):
        db.session.add(self)
        db.session.commit()

        return self.venueID

    #READ
    def get_all():
        return Venue.query.all()

    def get(venueName):
        venueN = '%{}%'.format(venueName)
        return db.session.query(Venue).filter(Venue.venue.like(venueN)).all()

    def getByID(id):
        return db.session.query(Venue).filter(Venue.venueID == id).first()

    #UPDATE
    def update(self):
        # session is th connection with the database
        db.session.commit()

    #DELETE
    def delete(id):
        venue = Venue.getByID(id=id)
        db.session.delete(venue)
        db.session.commit()