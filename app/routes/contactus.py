from random import randint
import datetime

from flask import Blueprint, request, redirect, url_for, render_template, flash, session, logging
from flask_login import login_user, login_required, current_user, logout_user

authorization = Blueprint('auth', __name__)

from app import app
from app.controller.contactus_controller import contactus_controller

#TODO either alter or remove bellow

@app.route('/contact', methods=['POST', 'GET'])
def contactus():
    if request.method == 'POST':
        venue = request.form['searchin']
        return redirect(url_for("Home", venue = venue))

    return contactus_controller.index()

@authorization.route('/profile', methods=['GET'])
@login_required
def profile():
    #process to load profile icon if user logged in
    image_file = url_for('static', filename='assets/' + current_user.image_file)
    return render_template('Profile/profile.html', username=current_user.username, image_file=image_file)


