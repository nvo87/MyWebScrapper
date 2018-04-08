from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import logging
from logging.handlers import RotatingFileHandler

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# SQL-Alchemy init
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# logging to file
if not os.path.exists('logs'):
    os.mkdir('logs')
file_handler = RotatingFileHandler('logs/events.log', maxBytes=10240,
                                   backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

app.logger.setLevel(logging.INFO)
app.logger.info('Microblog startup')

# app main parts init
from app import routes
from app import models
