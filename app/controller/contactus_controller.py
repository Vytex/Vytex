from flask import render_template, jsonify, redirect, url_for, Blueprint, request, flash, session, logging
from flask_login import login_user, login_required, current_user, logout_user
from app.models import User

from app import db

# as the models file contains all the models, import what you need
# from app.models import Shoe


class ContactUsController(object):
    def index(self):
        if current_user != None and current_user.is_authenticated:
            print(current_user)
            image_file= url_for('static', filename='assets/' + current_user.image_file)
            return render_template("contact/index.html", image_file=image_file)
        else:
            image_file= url_for('static', filename='assets/profileButtonPlaceholder.jpg')
            return render_template("contact/index.html", image_file=image_file)    

contactus_controller = ContactUsController()
