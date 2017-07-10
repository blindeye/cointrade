from poloniex import Poloniex
import keyfile


polo = Poloniex(keyfile.polokey, keyfile.polosecret)

print(polo.returnTicker()['BTC_ETH'])
print(keyfile.polokey)

BTC2ETH = polo.returnTicker()['BTC_ETH']

#balance = polo.returnBalances()
#print("I have %s ETH" % balance['ETH'])