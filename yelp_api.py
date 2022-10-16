# client ID
# 4s0I-9PIRrJJo4-cEcpocA
# endpoint:
# https://api.yelp.com/v3
import json
from yelp.client import Client
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("YELP_API_KEY")
API_HOST = 'https://api.yelp.com'
BUSINESS_PATH = '/v3/businesses/'
HEADERS = {'Authorization': 'Bearer %s' % API_KEY}

# search for a business using the business id
def get_business(business_id):
    business_path = BUSINESS_PATH + business_id
    url = API_HOST + business_path + '/reviews'
    headers = {'Authorization': f"Bearer {API_KEY}"}

    response = requests.get(url, headers=headers)

    return response.json()

############################################################################################################
# search for a business
def search(params):
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers, params=params)
    print("Status Code: ", response.status_code)
    return response


#### Parameters for search
search_terms = "Delis, Mexican"         # string
location = "Orange, CA"                 # string
limit = 5                               # int (max 50)
radius = 10000                          # int (max 40000) in meters
sort_by = "best_match"                  # string (best_match, rating, review_count, distance)
price = "1, 2, 3, 4"                    # string ("1" OR "1,2" OR "1,2,3" OR "1, 2, 3, 4") 
open_now = True                         # bool (True indicates only return open restaurants) (False returns all restaurants)
categories = "food"                     # string (filter by category)
latitude = 33.7879                      # float (latitude of location)
longitude = -117.8531                   # float (longitude of location)
attributes = "reservations"             # string (filter by attributes) "waitlist_reservation"

# use latitude and longitude OR location


# params = {'term': search_terms, 
#           'location': location, 
#           'limit': limit, 
#           'radius': radius, 
#           'sort_by': sort_by, 
#           'price': price, 
#           'open_now': open_now, 
#           'categories': categories, 
#           'latitude': latitude, 
#           'longitude': longitude, 
#           'attributes': attributes}

params = {  'term': search_terms,
            'location': location,
            'limit': limit,
            'price': price,
            'categories': categories}


# response = search(params)
# response = ""
# parsed = json.loads(response.text)

# businesses = parsed["businesses"]
# for business in businesses:
#     print("Name:    ", business["name"])
#     print("Rating:  ", business["rating"])
#     print("Price:   ", business["price"])
#     print("Phone:   ", business["phone"])
#     print("Address: ", ", ".join(business["location"]["display_address"]))
#     print()
