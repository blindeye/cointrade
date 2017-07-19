import json
import urllib.request

import coinone
from poloniex import Poloniex

#get polonix trading ratio
polo = Poloniex()
priceInfo = polo.returnTicker()
ETH2BTC = priceInfo['BTC_ETH']['last']
XRP2BTC = priceInfo['BTC_XRP']['last']

#get coinone coin price
urlTicker = urllib.request.urlopen('https://api.coinone.co.kr/ticker/?currency=all')
readTicker = urlTicker.read()
jsonTicker = json.loads(readTicker)
FindETC = jsonTicker['etc']['last']
ETC = int(FindETC)
FindBTC = jsonTicker['btc']['last']
BTC = int(FindBTC)
FindETH = jsonTicker['eth']['last']
ETH = int(FindETH)
FindXRP = jsonTicker['xrp']['last']
XRP = int(FindXRP)

mybalance = 500000.0
myBTC = mybalance/BTC
myBTC = myBTC * (1.0 - 0.0015)
#coinone trans
myBTC = myBTC - 0.0005
myETH = myBTC / float(ETH2BTC)
myETH = myETH * (1.0 - 0.0025)
#poloniex trans
myETH = myETH - 0.005
BTC_polo_ETH = myETH * ETH * (1.0 - 0.0015)

myETH = mybalance/ETH
myETH = myETH * (1.0 - 0.0015)
#coinone trans
myETH = myETH - 0.01
myBTC = myETH * float(ETH2BTC)
myBTC = myBTC * (1.0 - 0.0015)
#poloniex trans
myBTC = myBTC - 0.0001
ETH_polo_BTC = myBTC * BTC * (1.0 - 0.0015)

myBTC = mybalance/BTC
myBTC = myBTC * (1.0 - 0.0015)
#coinone trans
myBTC = myBTC - 0.0005
myXRP = myBTC / float(XRP2BTC)
myXRP = myXRP * (1.0 - 0.0025)
#poloniex trans
myXRP = myXRP - 0.15
BTC_polo_XRP = myXRP * XRP * (1.0 - 0.0015)

myXRP = mybalance/XRP
myXRP = myXRP * (1.0 - 0.0015)
#coinone trans
myXRP = myXRP - 0.01
myBTC = myXRP * float(XRP2BTC)
myBTC = myBTC * (1.0 - 0.0015)
#poloniex trans
myBTC = myBTC - 0.0001
XRP_polo_BTC = myBTC * BTC * (1.0 - 0.0015)

print("mybalance is ")
print(mybalance)
print("bitcoin to etherium")
print(BTC_polo_ETH)
print("etherium to bitcoin")
print(ETH_polo_BTC)
print("bitcoin to ripple")
print(BTC_polo_XRP)
print("ripple to bitcoin")
print(XRP_polo_BTC)
