from flask_pymongo import pymongo

CONNECTION_STRING = "mongodb+srv://carlosorduz:Endava2023@cluster0.njlnsoq.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('currency-monitoring')
CMCcollection = pymongo.collection.Collection(db, 'coin_market_cap')
CMCHistorycollection = pymongo.collection.Collection(db, 'coin_market_cap_history')
user_collection = pymongo.collection.Collection(db, 'user_1_items')