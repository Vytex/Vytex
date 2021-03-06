from random import randint

from flask import request

from app import app
from app.controller.shoe_controller import shoe_controller
from app.models import Shoe

@app.route('/shoe')
def shoe():
    return shoe_controller.index()

@app.route('/shoe-api', methods=['POST', 'GET'])
@app.route('/shoe-api/<id>', methods=['DELETE'])
def shoe_api(id=None):
    if request.method == "GET":
        return shoe_controller.get_shoes()
    elif request.method == "POST":
        # get data from client in the form of json ()
        data = request.json

        return shoe_controller.create_shoe(size=12, brand=data['brand'], model='n%d' % (randint(0,1000)))
    elif request.method == "DELETE":
        return shoe_controller.delete_shoe(id)
    else:
        # TODO replace with error controller function if they try to do sonmething other than get for example
        return shoe_controller.index()

# @app.route('/shoe')
# @app.route('/shoe/<option>', methods=["POST", "GET"])
# def shoe(option=None):
#     if option == "save":
#         print("request.method", request.method)
#         if request.method == "GET":
#             return shoe_controller.save()
#         elif request.method == "POST":
#             print("request methods is post")
#             data = request.json

#             print("data is data", data)

#             shoe = Shoe(size=12, brand=data["name"], model='n%d' % (randint(0, 100)))

#             print("SAVING SHOE")
#             return shoe_controller.save_shoe(shoe)
#     else:
#         return shoe_controller.index()