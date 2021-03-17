# imports the "router"
from app import app
from routes import home
from app.controller.home_controller import home_controller
from app.controller.lineList_controller import lineList_controller
from app.controller.admin_controller import admin_controller
from app.controller.userLines_controller import userLines_controller



@app.route('/')
def index():
    return 'index page'