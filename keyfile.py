import json

f = open('/Users/blindfish/keyfile','r')
kk = f.read()
keyfile = json.loads(kk)

coinoneKey = keyfile['coinonekey']
coinoneSecret = keyfile['coinonesecret']
