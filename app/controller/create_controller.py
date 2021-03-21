from flask import render_template, jsonify, redirect, url_for, Blueprint, request, flash, session, logging
from flask_login import login_user, login_required, current_user, logout_user


from app import db
from app.models import User
# as the models file contains all the models, import what you need
# from app.models import Shoe


class CreateController(object):
    def index(self):
        return render_template("create/index.html")


    

create_controller = CreateController()
