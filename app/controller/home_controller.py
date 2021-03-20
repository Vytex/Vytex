from flask import render_template, jsonify, redirect, url_for

from app import db

from app.models import Venue

class HomeController(object):
    def index(self):
        return render_template("Home/index.html")

home_controller = HomeController()