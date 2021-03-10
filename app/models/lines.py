from app import db
import datetime

class Lines(db.Model):
        
    venueID = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DATE, primary_key=True)
    x00000030 = db.Column(db.Integer)
    x00300100 = db.Column(db.Integer)
    x01000130 = db.Column(db.Integer)
    x01300200 = db.Column(db.Integer)
    x02000230 = db.Column(db.Integer)
    x02300300 = db.Column(db.Integer)
    x03000330 = db.Column(db.Integer)
    x03300400 = db.Column(db.Integer)
    x04000430 = db.Column(db.Integer)
    x04300500 = db.Column(db.Integer)
    x05000530 = db.Column(db.Integer)
    x05300600 = db.Column(db.Integer)
    x06000630 = db.Column(db.Integer)
    x06300700 = db.Column(db.Integer)
    x07000730 = db.Column(db.Integer)
    x07300800 = db.Column(db.Integer)
    x08000830 = db.Column(db.Integer)
    x08300900 = db.Column(db.Integer)
    x09000930 = db.Column(db.Integer)
    x09301000 = db.Column(db.Integer)
    x10001030 = db.Column(db.Integer)
    x10301100 = db.Column(db.Integer)
    x11001130 = db.Column(db.Integer)
    x11301200 = db.Column(db.Integer)
    x12001230 = db.Column(db.Integer)
    x12301300 = db.Column(db.Integer)
    x13001330 = db.Column(db.Integer)
    x13301400 = db.Column(db.Integer)
    x14001430 = db.Column(db.Integer)
    x14301500 = db.Column(db.Integer)
    x15001530 = db.Column(db.Integer)
    x15301600 = db.Column(db.Integer)
    x16001630 = db.Column(db.Integer)
    x16301700 = db.Column(db.Integer)
    x17001730 = db.Column(db.Integer)
    x17301800 = db.Column(db.Integer)
    x18001830 = db.Column(db.Integer)
    x18301900 = db.Column(db.Integer)
    x19001930 = db.Column(db.Integer)
    x19302000 = db.Column(db.Integer)
    x20002030 = db.Column(db.Integer)
    x20302100 = db.Column(db.Integer)
    x21002130 = db.Column(db.Integer)
    x21302200 = db.Column(db.Integer)
    x22002230 = db.Column(db.Integer)
    x22302300 = db.Column(db.Integer)
    x23002330 = db.Column(db.Integer)
    x23300000 = db.Column(db.Integer)

    #CREATE
    def save(self):
        db.session.add(self)
        db.session.commit()

        return self.venueID

    #READ
    def get_all():
        return Lines.query.all()

    def get(venueID):
        venueID = venueID
        todaysdate = datetime.today()
        return db.session.query(Lines).filter(Lines.venueID == venueID, Lines.date == todaysdate).first()

    def getLine(venueID, date):
        # helper method used to return a line that matches a specific venueid and date
        return db.session.query(Lines).filter(Lines.venueID == venueID, Lines.date == date).first()

    #UPDATE
    def update(self):
        # session is th connection with the database
        db.session.commit()

    #DELETE
    def delete(venueID, date):
        lList = Lines.getLine(venueID=venueID, date=date)
        db.session.delete(lList)
        db.session.commit()