# MyWebScrapper
My pet project using Flask framework. 
![N|Solid](https://api.monosnap.com/rpc/file/download?id=sgd85DYfmw7hrsjLKG9YnpOxrHP7tn)

### Overview
This app can scraps values you need from any sites. This values are saved into database and later you can browse history of data you want (ex. weather or bitcoin cost).
All you need is to know url and tag selector with data you want.

### Install (on Windows)
* Install your virtual environment 
```
pip install virtualenv
virtualenv venv
```
* Install requirements 
```
pip install -r requirements.txt
```
* Create new database (by default it's Mysql) and set its parametrs in ```config.py```
* Run project, just uncomment ```app.run``` in run.py before.
```
python run.py
```
Also you can use ```flask``` command in terminal. Therefore you shouldn't uncomment ```app.run``` line. You should type
```
set FLASK_APP = run.py
flask run
```
So, if you'll use ```flask shell``` command, all app environment (like DB) are loaded already.