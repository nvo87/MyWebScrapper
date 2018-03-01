from flask import Flask, render_template, request, redirect

from web_scrapper import Scrapper, ScrappersList

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def main_page():
    scrappers = ScrappersList()

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

if __name__=="__main__":
    app.run(debug=True, port=8001)
