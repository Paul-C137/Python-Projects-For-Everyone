import requests

BASE_URL = "http://dataservice.accuweather.com/locations/v1/cities/search?"
KEY = "apikey=PUT YOUR OWN KEY HERE."

choice = input('Please enter a city name.')

resp = requests.get(f"{BASE_URL}{KEY}&q={choice}").json()
print(resp)