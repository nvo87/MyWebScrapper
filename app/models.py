from datetime import datetime

from app import db
from app.web_scrapper import WebScrapper


class Scrapper(db.Model, WebScrapper):
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
        self.value_now = super().get_new_value(self.url, self.selector)
        return self.value_now


class Scrapper_values(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scrapper_id = db.Column(db.Integer, db.ForeignKey('scrapper.id'))
    value = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
