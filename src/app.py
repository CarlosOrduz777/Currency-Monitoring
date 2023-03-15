from flask import Flask, Response, render_template 
from flask_pymongo import pymongo
from bson import json_util
from werkzeug.local import LocalProxy
from db import CMC_collection

app = Flask(__name__)

@app.route('/')
def index():
    dataCMC = CMC_collection.find_one()
    return render_template('index.html', dataCMC=dataCMC)

if __name__== "__main__":
    app.run(debug=True)