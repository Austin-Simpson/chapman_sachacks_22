# client ID
# 4s0I-9PIRrJJo4-cEcpocA
# endpoint:
# https://api.yelp.com/v3
from yelp.client import Client
import requests

API_KEY = 'HIHXOVLf-jSEn24ROb755mxQYjhp6SAyKBMZseH-KpUV5dehqGJDKyHkO1Ah5U8sYnlz_xMekjLhrWh6eiZSFlWwbGzF0lWIdPuJtjyeRTFX_MY3_bSHRJ4opu5KY3Yx'
API_HOST = 'https://api.yelp.com'
BUSINESS_PATH = '/v3/businesses/'

def get_business(business_id):
    business_path = BUSINESS_PATH + business_id
    url = API_HOST + business_path + '/reviews'
    headers = {'Authorization': f"Bearer {API_KEY}"}

    response = requests.get(url, headers=headers)

    return response.json()



results = get_business('la-taqueria-san-francisco-2')
print(results)
