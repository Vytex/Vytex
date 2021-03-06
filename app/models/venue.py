from app import db
import datetime

class Venue(db.Model):
    
    venueID = db.Column(db.Integer, primary_key=True)
    venue = db.Column(db.NVARCHAR(30))
    description = db.Column(db.NVARCHAR(500))
    mon = db.Column(db.TIME(4))
    tue = db.Column(db.TIME(4))
    wed = db.Column(db.TIME(4))
    thu = db.Column(db.TIME(4))
    fri = db.Column(db.TIME(4))
    sat = db.Column(db.TIME(4))
    sun = db.Column(db.TIME(4))

    # override python print
    # def __repr__(self):
    #     return '<Venue {}>'.format(self.model)

    #CREATE
    def save(self):
        # saving shoe
        db.session.add(self)
        # commit transaction
        db.session.commit()

        return self.venueID

    #READ
    # Shoe.query.get()
    def get_all():
        # get all shoes
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