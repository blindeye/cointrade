import json
from six.moves import urllib
#import urllib.request

from poloniex import Poloniex
import logging
import datetime
import time
import sys, os

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

beta = float(sys.argv[1])

FindETC = jsonTicker['etc']['last']
ETC = int(FindETC)
FindBTC = jsonTicker['btc']['last']
BTC = int(FindBTC)
FindBCH = jsonTicker['bch']['last']
BCH = int(FindBCH)
FindETH = jsonTicker['eth']['last']
ETH = int(FindETH)
FindXRP = jsonTicker['xrp']['last']
XRP = int(FindXRP)
FindLTC = jsonTicker['ltc']['last']
LTC = int(FindLTC)

mybalance = 500000.0

now_price = dict()
coin_amount = dict()

coin_amount['mybalance']=mybalance
now_price['ETC']=ETC
now_price['BTC']=BTC
now_price['BCH']=BCH
now_price['ETH']=ETH
now_price['XRP']=XRP
now_price['LTC']=LTC

coinlist = ["BTC", "BCH", "ETH", "LTC", "XRP", "ETC"] 
for i in coinlist:
	coin_amount[i]=0.0

def buy(coin_amount, mybalance, rate, beta, price):
	mybalance = mybalance - beta * rate * price 
	coin_amount = coin_amount + beta * rate * (1.-0.0015)
	return mybalance, coin_amount

def sell(coin_amount, mybalance, rate, beta, price):
	coin_amount = coin_amount - beta * rate * (1.+0.0015) 
	mybalance = mybalance + beta * rate * price
	return mybalance, coin_amount

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

