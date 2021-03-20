from app import db
import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    username = db.Column(db.String(1000))

    def __repr__(self):
        return'<User {}>'.format(self.username)
