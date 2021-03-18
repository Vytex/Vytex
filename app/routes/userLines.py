from flask import request, redirect, url_for

from app import app
from app.controller.userLines_controller import userLines_controller

@app.route('/userLines')
def userLines():
    return userLines_controller.index()