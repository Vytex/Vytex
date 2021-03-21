from random import randint
import datetime
from flask import Blueprint, request, redirect, url_for,render_template, flash, session, logging
from flask import request, redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user
from app import app
from app.controller.home_controller import home_controller

@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        venue = request.form['searchin']
        return redirect(url_for("lineList", venue = venue))

    return home_controller.index()
