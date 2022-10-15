# client ID
# 4s0I-9PIRrJJo4-cEcpocA
# endpoint:
# https://api.yelp.com/v3

import requests
from yelp.client import Client

MY_API_KEY = HIHXOVLf-jSEn24ROb755mxQYjhp6SAyKBMZseH-KpUV5dehqGJDKyHkO1Ah5U8sYnlz_xMekjLhrWh6eiZSFlWwbGzF0lWIdPuJtjyeRTFX_MY3_bSHRJ4opu5KY3Yx

client = Client(MY_API_KEY)

example = requests.get('https://api.yelp.com/v3/businesses/search?term=delis')

print(example)