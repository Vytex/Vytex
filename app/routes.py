# imports the "router"
from app import app
from routes import home
from app.controller.home_controller import home_controller
from app.controller.lineList_controller import lineList_controller


@app.route('/')
def index():
    return 'index page'