import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Для Flask-WTF - работа с формами
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'superSecretKey'
    CSRF_ENABLED = True

    dbconf = {
        'host': '127.0.0.1',
        'user': 'mws_user',
        'password': 'mws2010',
        'database': 'mywebscrapper',
    }
