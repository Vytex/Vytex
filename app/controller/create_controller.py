from flask import render_template, jsonify, redirect, url_for, Blueprint, request, flash, session, logging
from flask_login import login_user, login_required, current_user, logout_user


from app import db
from app.models import User
# as the models file contains all the models, import what you need


class CreateController(object):
    def index(self):
        #process to load profile icon if user logged in
        if current_user != None and current_user.is_authenticated:
            image_file= url_for('static', filename='assets/' + current_user.image_file)
            return render_template("create/index.html", image_file=image_file)
        #process to load profile icon if user not logged in
        else:
            image_file= url_for('static', filename='assets/profileButtonPlaceholder.jpg')
            return render_template("create/index.html", image_file=image_file)   

    

create_controller = CreateController()
