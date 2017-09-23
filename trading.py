from poloniex import Poloniex
import coinoneBalance as Bal
import coinoneBuy as Buy
import coinoneSend as Send
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
    Buy.PAYLOAD = {
        "access_token": Buy.ACCESS_TOKEN,
        "price": simulate.XRP,
        "qty": simulate.myXRP,
        "currency": "xrp"
    }
    print Buy.get_result()

    Send.ACCESS_TOKEN=keyfile.coinoneKey
    Send.SECRET_KEY=keyfile.coinoneSecret
    Send.PAYLOAD = {
        "access_token": Send.ACCESS_TOKEN,
        "address": "receiver address",
        "auth_number": 123456,
        "qty": simulate.myXRP,
        "currency": "xrp",
    }
    Send.get_result()


