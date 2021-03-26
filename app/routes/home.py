from random import randint
import datetime
from flask import Blueprint, request, redirect, url_for, render_template, flash, session, logging
from flask_login import login_user, login_required, current_user, logout_user
from app import app
from app.controller.home_controller import home_controller

authorization = Blueprint('auth', __name__)

@app.route('/')
def index():
    return home_controller.index()

@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        venue = request.form['searchin']
        return redirect(url_for("lineList", venue = venue))

    return home_controller.index()

@authorization.route('/profile', methods=['GET'])
@login_required
def profile():
    #returns profile icon if user is logged in 
    image_file = url_for('static', filename='assets/' + current_user.image_file)
    return render_template('Profile/profile.html', username=current_user.username, image_file=image_file)
