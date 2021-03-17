from flask import render_template, jsonify, redirect, url_for


class UserLinesController(object):
    def index(self):
        return render_template("userLines/index.html")

userLines_controller = UserLinesController()