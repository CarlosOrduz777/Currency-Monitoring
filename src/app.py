from flask import Flask, Response, render_template 
from flask_pymongo import pymongo
from bson import json_util
from werkzeug.local import LocalProxy
from db import CMCcollection

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    data = CMCcollection.find_one()
    return render_template('index.html', data = data)

if __name__== "main_":
    app.run(debug=True)