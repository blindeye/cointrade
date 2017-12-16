import json
from six.moves import urllib
#import urllib.request

from poloniex import Poloniex
import logging
import datetime
import time
import sys, os

import numpy as np

#get polonix trading ratio
#polo = Poloniex()
#priceInfo = polo.returnTicker()
#ETH2BTC = priceInfo['BTC_ETH']['last']
#XRP2BTC = priceInfo['BTC_XRP']['last']
#BCH2BTC = priceInfo['BTC_BCH']['last']

startTime = time.time()
startDate = datetime.datetime.now()

file_name = sys.argv[0].split('/')[-1].replace('.py', '')
logFileName ='./log' + '/' + file_name + '_' + datetime.datetime.now().strftime('%Y%m%d') + '.log'
logger = logging.getLogger("crumbs")
logger.setLevel(logging.INFO)

formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')

fileHandler = logging.FileHandler(logFileName)
streamHandler = logging.StreamHandler()
fileHandler.setFormatter(formatter)
streamHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)

logger.info("Program Start")
#get coinone coin price
urlTicker = urllib.request.urlopen('https://api.coinone.co.kr/ticker/?currency=all')
readTicker = urlTicker.read()
jsonTicker = json.loads(readTicker)

beta = np.exp(np.random.rand(1000)) 

mybalance = 500000.0
now_price = dict()
coin_amount = dict()
coinlist = ["BTC", "ETH", "LTC", "XRP", "BCH", "BTG", "QTUM", "IOTA"]

for i in coinlist:
	Findcoin = jsonTicker[i.lower()]['last']
	now_price[i] = int(Findcoin)

coin_amount['mybalance']=mybalance

for i in coinlist:
	coin_amount[i]=dict()

def buy(coin_type, buying, now_price):
	coin_amount = (1.-0.0015) * buying/now_price[coin_type]
	return coin_amount

def sell(coin_type, selling, now_price):
	coin_amount = (1.+0.0015) * (selling/now_price[coin_type])
	return coin_amount

if os.path.isfile("./last_val.json"):
	f = open("./last_val.json", "r")
	line = f.read().strip("\n")
	last_price = json.loads(line)
	f.close()
else:
	f = open("./last_val.json", "w")
	f.write(json.dumps(now_price))
	f.close()
	sys.exit(0)

if os.path.isfile("./last_bal.json"):
	f = open("./last_bal.json", "r")
	line = f.read().strip("\n")
	coin_amount = json.loads(line)
	f.close()
else:
	f = open("./last_bal.json", "w")
	f.write(json.dumps(coin_amount))
	f.close()
	sys.exit(0)

for i in coinlist: 
	rate = float(now_price[i] - last_price[i])/last_price[i]
	if rate < 0:
		coin_amount['mybalance'], coin_amount[i] = buy(coin_amount[i],coin_amount['mybalance'],rate,beta,now_price[i])
	else:
		coin_amount['mybalance'], coin_amount[i] = sell(coin_amount[i],coin_amount['mybalance'],rate,beta,now_price[i])

tot=coin_amount['mybalance']
for i in coinlist:
	tot += coin_amount[i]*now_price[i] 

logger.info("total money : %s" % str(tot))

f = open("./last_val.json", "w")
f.write(json.dumps(now_price))
f.close()
f = open("./last_bal.json", "w")
f.write(json.dumps(coin_amount))
f.close()

logger.info("Program End")

