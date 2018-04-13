from flask import render_template, url_for, redirect, flash

from app import app, db
from .models import Scrapper, Scrapper_values
from .forms import ScrapperForm


@app.route('/')
def main_page():
    scrapper_form = ScrapperForm()
    scrappers = Scrapper.query.all()
    for scrapper in scrappers:
        try:
            scrapper.get_new_value()
        except Exception as err:
            flash('Error is: ' + str(err) + ' in ' + scrapper.name)
        else:
            new_value = Scrapper_values(scrapper_id=scrapper.id, value=scrapper.value_now)
            db.session.add(new_value)
    db.session.commit()
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


@app.route('/delete-scrapper/<scrapper_id>')
def del_scrapper(scrapper_id):
    """ Removing scrapper from DB by its id. """
    scrapper = Scrapper.query.filter_by(id=scrapper_id).first()
    db.session.delete(scrapper)
    db.session.commit()
    flash('Scrapper called "{}" has been deleted'.format(scrapper.name))
    return redirect(url_for('main_page'))


@app.route('/scrapper/<scrapper_id>')
def scrapper_info(scrapper_id):
    """ Get all values for scrapper"""
    form = ScrapperForm()
    scrapper = Scrapper.query.filter_by(id=scrapper_id).first()
    values = Scrapper_values.query.filter_by(scrapper_id=scrapper_id).order_by(Scrapper_values.timestamp.desc()).all()
    return render_template('scrapper_page.html', scrapper=scrapper, values=values, form=form)


@app.route('/edit-scrapper/<scrapper_id>', methods=['POST'])
def edit_scrapper(scrapper_id):
    """ Editing scrapper from DB by its id. """
    form = ScrapperForm()
    if form.validate_on_submit():
        scrapper = Scrapper.query.filter_by(id=scrapper_id).first()
        scrapper.name = form.name.data
        scrapper.url = form.url.data
        scrapper.selector = form.selector.data
        db.session.commit()
        flash('Scrapper called "{}" has been edited'.format(scrapper.name))
    return redirect(url_for('main_page'))
