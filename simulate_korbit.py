import json
from urllib.request import Request, urlopen
from poloniex import Poloniex
import datetime

#get polonix trading ratio
polo = Poloniex()
priceInfo = polo.returnTicker()
ETH2BTC = priceInfo['BTC_ETH']['last']
XRP2BTC = priceInfo['BTC_XRP']['last']

reqBTC = Request('https://api.korbit.co.kr/v1/ticker?currency_pair=btc_krw' , headers={'User-Agent': 'Mozilla/5.0'})
readBTC = urlopen(reqBTC).read()
jsonBTC = json.loads(readBTC.decode('utf-8'))
FindBTC = jsonBTC['last']
BTC = int(FindBTC)
reqETH = Request('https://api.korbit.co.kr/v1/ticker?currency_pair=eth_krw' , headers={'User-Agent': 'Mozilla/5.0'})
readETH = urlopen(reqETH).read()
jsonETH = json.loads(readETH.decode('utf-8'))
FindETH = jsonETH['last']
ETH = int(FindETH)
reqETC = Request('https://api.korbit.co.kr/v1/ticker?currency_pair=etc_krw' , headers={'User-Agent': 'Mozilla/5.0'})
readETC = urlopen(reqETC).read()
jsonETC = json.loads(readETC.decode('utf-8'))
FindETC = jsonETC['last']
ETC = int(FindETC)
reqXRP = Request('https://api.korbit.co.kr/v1/ticker?currency_pair=xrp_krw' , headers={'User-Agent': 'Mozilla/5.0'})
readXRP = urlopen(reqXRP).read()
jsonXRP = json.loads(readXRP.decode('utf-8'))
FindXRP = jsonXRP['last']
XRP = int(FindXRP)

mybalance = 500000.0
myBTC = mybalance/BTC
myBTC = myBTC * (1.0 - 0.002)
#coinone trans
myBTC = myBTC - 0.0005
myETH = myBTC / float(ETH2BTC)
myETH = myETH * (1.0 - 0.0025)
#poloniex trans
myETH = myETH - 0.005
BTC_polo_ETH = myETH * ETH * (1.0 - 0.002)

myETH = mybalance/ETH
myETH = myETH * (1.0 - 0.002)
#coinone trans
myETH = myETH - 0.01
myBTC = myETH * float(ETH2BTC)
myBTC = myBTC * (1.0 - 0.0015)
#poloniex trans
myBTC = myBTC - 0.0001
ETH_polo_BTC = myBTC * BTC * (1.0 - 0.002)

myBTC = mybalance/BTC
myBTC = myBTC * (1.0 - 0.002)
#coinone trans
myBTC = myBTC - 0.0005
myXRP = myBTC / float(XRP2BTC)
myXRP = myXRP * (1.0 - 0.0025)
#poloniex trans
myXRP = myXRP - 0.15
BTC_polo_XRP = myXRP * XRP * (1.0 - 0.002)

myXRP = mybalance/XRP
myXRP = myXRP * (1.0 - 0.002)
#coinone trans
myXRP = myXRP - 0.2
myBTC = myXRP * float(XRP2BTC)
myBTC = myBTC * (1.0 - 0.0015)
#poloniex trans
myBTC = myBTC - 0.0001
XRP_polo_BTC = myBTC * BTC * (1.0 - 0.002)

#print("mybalance is ")
#print(mybalance)
#print("bitcoin to etherium")
#print(BTC_polo_ETH)
#print("etherium to bitcoin")
#print(ETH_polo_BTC)
#print("bitcoin to ripple")
#print(BTC_polo_XRP)
#print("ripple to bitcoin")
#print(XRP_polo_BTC)
print(datetime.datetime.now(), BTC_polo_ETH, ETH_polo_BTC, BTC_polo_XRP, XRP_polo_BTC)
