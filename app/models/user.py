from app import db
from flask_login import UserMixin
import datetime

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    username = db.Column(db.String(1000))
    image_file = db.Column(db.String(60), nullable=False, default="Userprofile.png")
    def __repr__(self):
        return '<User {}>'.format(self.username)    
