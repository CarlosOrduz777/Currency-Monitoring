from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pymongo
from db import CMCHistorycollection
from datetime import datetime

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

def save_in_database():
  try:
      response = session.get(url, params=parameters)
      dataCMC = json.loads(response.text)

      # Agregar fecha y hora al registro
      now = datetime.now()
      dataCMC['timestamp'] = now.strftime('%Y-%m-%d %H:%M:%S')

      # Insertar registro en la colección de historial
      CMCHistorycollection.insert_one(dataCMC)
      print("Datos guardados en MongoDB Atlas!")
      
  except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)