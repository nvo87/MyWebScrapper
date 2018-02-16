from flask import Flask, render_template, request, redirect

from dbconnect import UseDatabase, dbconfig
from web_scrapper import Scrapper

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def main_page():
    if request.method == 'GET':
        with UseDatabase(dbconfig) as cursor:
            SQL_select = """ select name, url, selector from scrappers """
            cursor.execute(SQL_select)
            scrappers_data = cursor.fetchall()

        scrappers=[]
        for scrapper_data_item in scrappers_data:
            scrapper = Scrapper(name=scrapper_data_item[0],
                                url=scrapper_data_item[1], 
                                selector=scrapper_data_item[2])
            scrapper.result = scrapper.get_scrapped_value()
            scrappers.append(scrapper)

        context = {
            'scrappers': scrappers
        }
        
    elif request.method == 'POST':
        url = request.form['url']
        selector = request.form['selector']
        wrapper_name = request.form['wrapper_name']

        context = {
            'scrappers': scrappers
        }

        
    return render_template('index.html', **context)

if __name__=="__main__":
    app.run(debug=True)
