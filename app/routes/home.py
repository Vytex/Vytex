from random import randint
import datetime

from flask import request, redirect, url_for

from app import app
from app.controller.home_controller import home_controller

@app.route('/')
def index():
    return home_controller.index()

@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        venue = request.form['searchin']
        return redirect(url_for("lineList", venue = venue))

    return home_controller.index()