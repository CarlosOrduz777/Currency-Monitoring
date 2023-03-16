from flask import Flask, Response, render_template 
from flask_pymongo import pymongo
from bson import json_util
from werkzeug.local import LocalProxy
from db import CMCcollection
from apscheduler.schedulers.background import BackgroundScheduler
import os
from CMC import save_in_database
import time

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(save_in_database, 'interval', seconds=300)
scheduler.start()

app = Flask(__name__)

@app.route('/v1/coins',methods=['GET'])
def index():
    data_coins = CMCcollection.find_one()
    response = json_util.dumps(data_coins)
    return Response(response,mimetype='application/json')

if __name__== "__main__":
    app.run(debug=True)