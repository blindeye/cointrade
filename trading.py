from poloniex import Poloniex
import coinoneBalance as Bal
import coinoneBuy as Buy
import keyfile
import sys
import simulate


polo = Poloniex(keyfile.polokey, keyfile.polosecret)

coinone_balance = Bal.get_result()


if coinone_balance['krw']['avail'] < 100:
    #termSum()
    sys.exit(0)
else:
    #storage = strage()
    Buy.ACCESS_TOKEN=keyfile.coinoneKey
    Buy.SECRET_KEY=keyfile.coinoneSecret
    Buy.PAYLOAD['price'] = simulate.FindXRP
    Buy.PAYLOAD['qty'] = simulate.myXRP
    Buy.PAYLOAD['currency']


