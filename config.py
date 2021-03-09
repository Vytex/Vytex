import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('password')
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'smeggins'
    MYSQL_PASSWORD = r'3001'
    MYSQL_DB = 'app'
    MYSQL_PORT = 3306

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    
    # disables signalling to the application every time
    # a change is made to the database
    SQLALCHEMY_TRACK_MODIFICATIONS = False