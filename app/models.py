from datetime import datetime

from app import db
import app.web_scrapper as web_scrapper

# TODO get_new_value - как сохранить значение в scrapper_values


class Scrapper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    url = db.Column(db.String(256))
    selector = db.Column(db.String(128))
    # The lazy argument defines how the database query for the relationship will be issued
    values = db.relationship('Scrapper_values', backref='scrapper', lazy='dynamic')
    value_now = None

    def __repr__(self):
        return 'Scrapper {}'.format(self.name)

    def get_new_value(self):
        self.value_now = web_scrapper.get_new_value(self.url, self.selector)
        return self.value_now


class Scrapper_values(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scrapper_id = db.Column(db.Integer, db.ForeignKey('scrapper.id'))
    value = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
