#!/usr/bin/python3
"""Example accessing Korean Won to Dollar Exchange rate using 
   currencyapi.com.  This API requires a key.  The free tier
   limits calls and updates once a day. Install the requests
   library before running. | P. Lack"""

# Import third-party requests library
import requests

# Set up the base URL according to the documentation found online
BASE_URL = "https://api.currencyapi.com/v3/latest?"
# Insert the key you got from currencyapi.com
KEY = "INSERT YOUR KEY HERE!!!"

# Send the GET request
response = requests.get(BASE_URL + KEY)

# Check the response status code so we know that it worked.
if response.status_code == 200:
    # Request successful
    # Strip off the json.  'data' is now a Python dictionary.
    data = response.json()
    # Dig into the dictionary by using the dictionary keys and pring
    # the exchange rate for Korean Won.  The base rate is USD.
    print(data['data']['KRW']['value'])     
      
else:
    # If you got back a response code other than '200', this will print.
    print("Request failed with status code:", response.status_code)
