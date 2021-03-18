from random import randint

from flask import request, redirect, url_for

from app import app
from app.controller.home_controller import home_controller
from app.controller.userLines_controller import userLines_controller
from app.models import User

@app.route('/userLines')
def userLines():
    return userLines_controller.index()

@app.route('/userSpot')
