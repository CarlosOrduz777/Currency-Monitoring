from flask import Flask, Response, g
from flask_pymongo import pymongo
from bson import json_util
from werkzeug.local import LocalProxy
import db
from db import user_collection

app = Flask(__name__)

@app.route('/coins',methods=['GET'])
def get_criptocoins():
    coins = user_collection.find()
    response = json_util.dumps(coins)
    return Response(response,mimetype='application/json')

if __name__== "__main__":
    app.run(debug=True)