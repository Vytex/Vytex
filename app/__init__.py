# flask import
from flask import Flask
from flask import Blueprint
from flask_login import LoginManager

# flask extensions
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_apscheduler import APScheduler

# first party imports
from config import Config
# connect database with routes
#from app.routes.create import authorization as auth_blueprint

# initialize the application
app = Flask(__name__)


# config
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# scheduler
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

# db

#db
#db = SQLAlchemy(app)
#db.init_app(app)

from app.scheduledTasks import *
from app import routes
from app.routes.create import authorization as auth_blueprint
app.register_blueprint(auth_blueprint)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))
