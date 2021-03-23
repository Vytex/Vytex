from app import db
import datetime

class Spot(db.Model):
    user_id =  db.Column(db.Integer, primary_key=True)
    venue_id =  db.Column(db.Integer)
    date = db.Column(db.VARCHAR(8), primary_key=True)
    time_slot = db.Column(db.VARCHAR(8), primary_key=True)
    arrived = db.Column(db.Boolean)
    

    def save(self):
        db.session.add(self)
        db.session.commit()

        return self.venue_id

    #READ
    def get_all():
        return Spot.query.all()


    def get_spot_venue(venue_id, date):
        return db.session.query(Spot).filter(Spot.venue_id == venue_id, Spot.date == date).all()

    def get_spot_user(user_id, date):
        return db.session.query(Spot).filter(Spot.user_id == user_id, Spot.date == date).all()

    def get_spots_by_id(user_id):
        return db.session.query(Spot).filter(Spot.user_id == user_id).all()

    def get_by_user_id(date, user_id, time_slot):
        return db.session.query(Spot).filter(Spot.user_id == user_id, Spot.date == date, Spot.time_slot == time_slot).first()

    def get_latest_spot(user_id, date):
        spots = db.session.query(Spot).filter(Spot.user_id == user_id, Spot.date == date).all()
        # allSpots = 
        latest_spot = None
        if len(spots) != 0:

            for spot in spots:

                if latest_spot == None:
                    latest_spot = spot
                else:
                    if int(latest_spot.time_slot[0:2]) == int(spot.time_slot[0:2]):
                        if int(latest_spot.time_slot[3:4]) < int(spot.time_slot[3:4]):
                            latest_spot = spot
                    elif int(spot.time_slot[0:2]) < 5:
                        if int(latest_spot.time_slot[0:2]) < 5:
                            if int(latest_spot.time_slot[0:2]) < int(spot.time_slot[0:2]):
                                latest_spot = spot
                        else:
                            latest_spot = spot
                    elif int(latest_spot.time_slot[0:2]) >= 5 and int(latest_spot.time_slot[0:2]) < int(spot.time_slot[0:2]):
                        latest_spot = spot

            return latest_spot

        return -1


