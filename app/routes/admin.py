from random import randint
import datetime

from flask import request, redirect, url_for

from app import app
from app.controller.admin_controller import admin_controller


@app.route('/admin', methods=['POST', 'GET'])
def admin():
    return admin_controller.index()

@app.route('/admin-api', methods=['POST', 'GET'])
@app.route('/admin-api/<id>', methods=['DELETE'])
def admin_api(id=None):
    if request.method == "GET":
        return admin_controller.get_venues()
    elif request.method == "POST":
        # get data from client in the form of json ()
        data = request.json

        return admin_controller.create_admin(size=12, brand=data['brand'], model='n%d' % (randint(0,1000)))
    elif request.method == "DELETE":
        return admin_controller.delete_venue(id)
    else:
        # TODO replace with error controller function if they try to do sonmething other than get for example
        return admin_controller.index()
