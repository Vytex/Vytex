from flask import render_template, jsonify, redirect, url_for

from app import db

# as the models file contains all the models, import what you need
# from app.models import Shoe
from app.models.login import User
u = User(username='Client', email='client@example.com')

class LoginController(object):
    def index(self):
        return render_template("home/UserLogin.html")




  

login_controller = LoginController()