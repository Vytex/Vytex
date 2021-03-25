from flask import render_template, jsonify, redirect, url_for, Blueprint, request, flash, session, logging
from flask_login import login_user, login_required, current_user, logout_user

from app import db
from app.models import User

# as the models file contains all the models, import what you need
# from app.models import Shoe
#from app.models.user import User
#u = User(username='Client', email='client@example.com')

class LoginController(object):

    def index(self):
        if current_user != None and current_user.is_authenticated:
            print(current_user)
            image_file = url_for('static', filename='assets/' + current_user.image_file)
            return render_template("LogIn/index.html", image_file=image_file)
        else:
            image_file = url_for('static', filename='assets/profileButtonPlaceholder.jpg')
            return render_template("LogIn/index.html", image_file=image_file)

login_controller = LoginController()
