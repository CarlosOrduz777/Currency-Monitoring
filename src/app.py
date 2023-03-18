from flask import Flask, Response, render_template 
from flask_pymongo import pymongo
from bson import json_util
from werkzeug.local import LocalProxy
from db import CMCHistorycollection
import time
import os
from CMC import save_in_database
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(save_in_database, 'interval', seconds=300)
scheduler.start()


app = Flask(__name__)

@app.route('/v2/coins',methods=['GET'])
def index():
    data_coins = CMCHistorycollection.find().sort('timestamp', pymongo.DESCENDING).limit(1)[0]
    response = json_util.dumps(data_coins)
    return Response(response,mimetype='application/json')

if __name__== "__main__":
    app.run(debug=True)