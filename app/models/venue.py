from app import db
import datetime

class Venue(db.Model):
        
    venue_id = db.Column(db.Integer, primary_key=True)
    venue = db.Column(db.NVARCHAR(30))
    description = db.Column(db.NVARCHAR(500))
    venue_url = db.Column(db.VARCHAR(2083))
    venue_city = db.Column(db.NVARCHAR(500))
    venue_icon = db.Column(db.VARCHAR(500))
    
    mon_open = db.Column(db.TIME(4))
    mon_close = db.Column(db.TIME(4))

    tue_open = db.Column(db.TIME(4))
    tue_close = db.Column(db.TIME(4))

    wed_open = db.Column(db.TIME(4))
    wed_close = db.Column(db.TIME(4))

    thu_open = db.Column(db.TIME(4))
    thu_close = db.Column(db.TIME(4))

    fri_open = db.Column(db.TIME(4))
    fri_close = db.Column(db.TIME(4))

    sat_open = db.Column(db.TIME(4))
    sat_close = db.Column(db.TIME(4))

    sun_open = db.Column(db.TIME(4))
    sun_close = db.Column(db.TIME(4))

    line_capacity = db.Column(db.Integer)

    #CREATE
    def save(self):
        db.session.add(self)
        db.session.commit()

        return self.venue_id

    #READ
    def get_all():
        return Venue.query.all()

    def get(venue_name):
        venue_n = '%{}%'.format(venue_name)
        return db.session.query(Venue).filter(Venue.venue.like(venue_n)).all()

    def get_by_id(id):
        return db.session.query(Venue).filter(Venue.venue_id == id).first()

    #UPDATE
    def update(self):
        # session is th connection with the database
        db.session.commit()

    #DELETE
    def delete(id):
        venue = Venue.get_by_id(id=id)
        db.session.delete(venue)
        db.session.commit()