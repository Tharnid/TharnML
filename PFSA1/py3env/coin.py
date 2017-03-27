import pprint

import urllib.request
import json

query_currencies = "http://www.coinbase.com/api/v1/currencies/"

with urllib.request.urlopen( query_currencies ) as document:
    print(document.info().items())
    currencies = json.loads( document.read ().decode("utf-8") )

#    print(currencies)
#    print( len(currencies) )

# USD and EUR are covered
for country, currency in currencies:
    if currency in ("PYG", "USD", "EUR", "GBP", "RSD"):
        print( country, currency)

import urllib.parse

def get_spot_rate( currency ):
    scheme_netloc_path= "https://coinbase.com/api/v1/prices/spot_rate"
    form= {"currency":currency}
    query= urllib.parse.urlencode(form)

    with urllib.request.urlopen( scheme_netloc_path+"?"+query ) as document:
        spot_rate= json.loads( document.read().decode("utf-8") )
    return spot_rate

    print(spot_rate)
