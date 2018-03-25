from flask import render_template, url_for, redirect, flash

from app import app, db
from .models import Scrapper
from .forms import ScrapperForm


@app.route('/')
def main_page():
    scrapper_form = ScrapperForm()
    scrappers = Scrapper.query.all()
    for scrapper in scrappers:
        scrapper.get_new_value()
    return render_template('index.html', scrapper_form=scrapper_form, scrappers=scrappers)


@app.route('/add-scrapper', methods=['POST'])
def add_scrapper():
    """ Adding new scrapper to DB. """
    form = ScrapperForm()
    if form.validate_on_submit():
        scrapper = Scrapper(name=form.name.data, url=form.url.data, selector=form.selector.data)
        db.session.add(scrapper)
        db.session.commit()
        flash('New scrapper called "{}" has been added'.format(scrapper.name))
    return redirect(url_for('main_page'))


@app.route('/delete-scrapper/', methods=['POST'])
def del_scrapper():
    """ Removing scrapper from DB by its id. """
    form = ScrapperForm()
    if form.validate_on_submit():
        scrapper = Scrapper.query.filter_by(id=form.id.data).first()
        db.session.delete(scrapper)
        db.session.commit()
        flash('New scrapper called "{}" has been deleted'.format(scrapper.name))
    return redirect(url_for('main_page'))