# client ID
# 4s0I-9PIRrJJo4-cEcpocA
# endpoint:
# https://api.yelp.com/v3
import json
from yelp.client import Client
import requests

API_KEY = 'HIHXOVLf-jSEn24ROb755mxQYjhp6SAyKBMZseH-KpUV5dehqGJDKyHkO1Ah5U8sYnlz_xMekjLhrWh6eiZSFlWwbGzF0lWIdPuJtjyeRTFX_MY3_bSHRJ4opu5KY3Yx'
API_HOST = 'https://api.yelp.com'
BUSINESS_PATH = '/v3/businesses/'
HEADERS = {'Authorization': 'Bearer %s' % API_KEY}

def get_business(business_id):
    business_path = BUSINESS_PATH + business_id
    url = API_HOST + business_path + '/reviews'
    headers = {'Authorization': f"Bearer {API_KEY}"}

    response = requests.get(url, headers=headers)

    return response.json()

###############
def search(params):
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers, params=params)
    print("Status Code: ", response.status_code)
    return response


params = {'term':'food, delis', 'location':'Orang, CA', 'limit': 5}

response = search(params)

parsed = json.loads(response.text)

businesses = parsed["businesses"]
for business in businesses:
    print(business["name"])