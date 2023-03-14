from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pymongo

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {
  'symbol': 'BNB,BTC,ETH,USDT',
  'convert': 'USD'
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'f1aa2948-2111-459a-8927-2cd2a269383f',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    # print(data)
    
    # Conectar a la base de datos de MongoDB Atlas
    CONNECTION_STRING = "mongodb+srv://erikasalazar:GJcbRabchO@currencymonitoring.au9jkqk.mongodb.net/?retryWrites=true&w=majority"
    client = pymongo.MongoClient(CONNECTION_STRING)
    db = client.get_database('database')
    collection = pymongo.collection.Collection(db, 'coin_market_cap')
    collection.insert_one(data)
    
    print("Datos guardados en MongoDB Atlas!")
    
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)