from flask import Flask, Response, render_template 
from flask_pymongo import pymongo
from bson import json_util
from werkzeug.local import LocalProxy
from Coin_Market_Cap import collection

app = Flask(__name__)

@app.route('/')
def index():
    # Conectar a la base de datos de MongoDB Atlas
    CONNECTION_STRING = "mongodb+srv://erikasalazar:GJcbRabchO@currencymonitoring.au9jkqk.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(CONNECTION_STRING)
    db = client.get_database('database')
    collection = pymongo.collection.Collection(db, 'coin_market_cap')
    data = collection.find_one()

    return render_template('index.html', data=data)



if __name__== "__main__":
    app.run(debug=True)