# flask import
from flask import Flask

# flask extensions
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_apscheduler import APScheduler

# first party imports
from config import Config

# initialize the application
app = Flask(__name__)

# config
app.config.from_object(Config)

# scheduler
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


# db
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.scheduledTasks import *
from app import routes