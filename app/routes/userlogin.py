from random import randint
import datetime

from flask import Blueprint, request, redirect, url_for, render_template, flash, session, logging
from flask_login import login_user, login_required, current_user, logout_user
authorization = Blueprint('auth', __name__)


from app import app
from app.controller.login_controller import login_controller

#TODO either alter or remove bellow

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['authorization']
        return redirect(url_for("UserAccount", user = profileUser))

    return login_controller.index()


@authorization.route('/profile', methods=['GET'])
@login_required
def profile():
    #loads profile pic if user is identified
    image_file = url_for('static', filename='assets/' + current_user.image_file)
    return render_template('Profile/profile.html', username=current_user.username, image_file=image_file)
