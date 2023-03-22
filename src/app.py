from flask import Flask, Response, render_template 
from flask_pymongo import pymongo
from bson import json_util
from werkzeug.local import LocalProxy
from db import CMCcollection
from apscheduler.schedulers.background import BackgroundScheduler
import os
from stocks import load_current_stock_prices
from CMC import save_in_database
import time


scheduler = BackgroundScheduler(daemon=True)
#scheduler.add_job(save_in_database, 'interval', seconds=60)
scheduler.add_job(load_current_stock_prices, 'interval', seconds=300)
scheduler.start()



app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    data = CMCcollection.find_one()
    return render_template('index.html', data = data)

if __name__== "__main__":
    app.run(debug=True)