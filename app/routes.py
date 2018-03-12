from flask import render_template, request

from app import app
from .web_scrapper import ScrappersList


@app.route('/', methods=['GET', 'POST'])
def main_page():
    scrappers = ScrappersList()

    # Добавляем скраппер
    if request.method == 'POST':
        scrappers.add_scrapper(request.form['name'],
                               request.form['url'],
                               request.form['selector'])

    context = {
        'scrappers': scrappers.get_all_scrappers()
    }

    print(context['scrappers'])
    return render_template('index.html', **context)


@app.route('/delete-scrapper/', methods=['POST'])
def del_scrapper():
    scrappers = ScrappersList()
    scrappers.del_scrapper(request.form['scrapper_id'])
    return 'ok'