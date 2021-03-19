from flask import render_template, jsonify, redirect, url_for
from datetime import time, datetime, timedelta

from app import db

from app.models import Venue, Lines

class UserLinesController(object):
    def index(self):
        return render_template("userLines/index.html")


userLines_controller = UserLinesController()        




