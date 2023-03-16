import yfinance as yf
import json
import pandas as pd
from db import stockcollection
from datetime import datetime
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

#Returns info on a specific stock
def stockPrice(stock, Period, Interval):
  data = yf.download(tickers= stock, period= Period, interval= Interval)
  return data

#Returns closing value on defined period
def closingPrice(data):
   return data.tail(1).iloc[-1]["Close"]


pd1 = stockPrice('msft','1d','1h').tail(1)[['Close']]
print (pd1)

#print(type(stockPrice('msft','1d','1h').tail(1)[['Close']]))
#print(stockPrice('msft','1d','1h').tail(1)[['Close']])
#data = pd1['Datetime']

#data = pd.DataFrame(pd1, columns = ['Datetime', 'price'])
#print (data)

microsoft = yf.Ticker('msft')
amd = yf.Ticker('amd')
apple = yf.Ticker('aapl')
google = yf.Ticker('goog')
#print(msft.fast_info)
#print([msft.fast_info['timezone'],msft.fast_info['lastPrice']])
now = datetime.now().strftime('%H:%M:%S')
#print(now)
dct = {'Microsoft':{'datetime': now, 'price' :microsoft.fast_info['lastPrice'] },
       'AMD': {'datetime': now, 'price': amd.fast_info['lastPrice']},
       'Apple': {'datetime': now, 'price': apple.fast_info['lastPrice']},
       'Google': {'datetime': now, 'price': amd.fast_info['lastPrice']},
       }
#print (dct)
file = json.dumps(dct, indent = 4)
print (file)

# Enviar Datos a ka Colección
data = json.loads(file)
try:
      stockcollection.insert_one(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)