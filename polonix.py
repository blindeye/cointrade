from poloniex import Poloniex
import keyfile


polo = Poloniex(keyfile.polokey, keyfile.polosecret)

print(polo.returnTicker()['BTC_ETH'])
print(keyfile.polokey)

balance = polo.returnBalances()
print("I have %s ETH" % balance['ETH'])