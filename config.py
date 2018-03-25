import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    TEMPLATES_AUTO_RELOAD = True

    # Для Flask-WTF - работа с формами
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'superSecretKey'
    CSRF_ENABLED = True

    dbconf = {
        'host': '127.0.0.1',
        'user': 'mws_user',
        'password': 'mws2010',
        'database': 'mywebscrapper',
    }
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://' + dbconf['user'] + ':' + dbconf['password'] + '@' + dbconf['host'] + '/' + dbconf['database']

    # to disable a feature of Flask-SQLAlchemy, which is to signal
    # the application every time a change is about to be made in the database.
    SQLALCHEMY_TRACK_MODIFICATIONS = False