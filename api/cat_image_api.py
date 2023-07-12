import requests

# Set up the request parameters
url = "https://api.thecatapi.com/v1/images/search"
headers = {
    "x-api-key": "INSERT API KEY HERE!!!"
}

# Send the GET request
response = requests.get(url, headers=headers)

# Check the response status code
if response.status_code == 200:
    # Request successful
    data = response.json()
    image = requests.get(data[0]["url"])
    with open('cat.jpg', 'wb') as cat_file:
        cat_file.write(image.content)
else:
    # Request failed
    print("Request failed with status code:", response.status_code)
