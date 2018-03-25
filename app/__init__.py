from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# SQL-Alchemy init
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# app main parts init
from app import routes
from app import models
