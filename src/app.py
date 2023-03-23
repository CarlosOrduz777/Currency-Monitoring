from flask import Flask, Response
from flask_cors import CORS
from flask_pymongo import pymongo
from bson import json_util
from db import CMCHistorycollection
from werkzeug.local import LocalProxy
from db import CMCcollection
from apscheduler.schedulers.background import BackgroundScheduler
import os
from stocks import load_current_stock_prices
from CMC import save_in_database
import time
import atexit

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(load_current_stock_prices, 'interval', seconds=60)
scheduler.add_job(save_in_database, 'interval', seconds=300)
scheduler.start()

atexit.register(lambda : scheduler.shutdown())

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route('/v3/coins', methods=['GET'])
def get_coins():
    data_coins = CMCHistorycollection.find().sort('timestamp', pymongo.ASCENDING)
    response = json_util.dumps(data_coins)
    return Response(response, mimetype='application/json')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET')
    return response

if __name__ == "__main__":
    app.run(debug=True)