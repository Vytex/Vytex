from flask import render_template, jsonify

from app import db

from random import randint

# as the models file contains all the models, import what you need
from app.models import Shoe

class ShoeController(object):
    def index(self):
        shoes = Shoe.get_all()
        for shoe in shoes:
            print(shoe.id, shoe.brand, shoe.model)
        return render_template("shoe/index.html", shoes=shoes)
    def get_shoes(self):
        shoes = Shoe.get_all()
        output = []

        # formatting the data for the client 
        for shoe in shoes:
            output.append(
                {
                    "id": shoe.id,
                    "brand": shoe.brand,
                    "model": shoe.model,
                    "size": shoe.size
                }
            )
        
        return jsonify(output)
    
    def save(self):
        # shoe = Shoe(size=12, brand='reebook', model='n%d' % (randint(0, 100)))
        # saving shoe
        # shoe_id = shoe.save()
        return render_template("shoe/save.html")

    def create_shoe(self, size, brand, model):
        # create a shoe
        shoe = Shoe(size=size, brand=brand, model=model)
        shoe_id = shoe.save()
        # give this object back to the client
        data = {
            "id": shoe_id
        }
        return jsonify(data)
    
    def delete_shoe(self, id):
        Shoe.delete(id)

        data = {
            "success": True
        }
        return jsonify(data)

    def save_shoe(self, shoe):
        # shoe = Shoe(size=12, brand='reebook', model='n%d' % (randint(0, 100)))
        # saving shoe
        shoe_id = shoe.save()
        # success or fail page
        # return render_template("shoe/index.html", shoe_id = shoe_id)
        data = {
            "success": True
        }

        print("data", data)
        return jsonify(data)

shoe_controller = ShoeController()