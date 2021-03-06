# flask import
from flask import Flask

# flask extensions
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# first party imports
from config import Config

# initialize the application
app = Flask(__name__)

# config
app.config.from_object(Config)

# db
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes