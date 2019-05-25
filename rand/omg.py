import json
from pprint import pprint

with open('rpPurchases.json') as f:
    data = json.load(f)

l = []

for idx in data:
    l.append((idx["amount"],idx["paymentType"]))

rp = 0

for a in l:
	rp += a[0]

print(rp)


