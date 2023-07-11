import requests

# Set up the request parameters
url = "https://data.usajobs.gov/api/search"
headers = {
    "Host": "data.usajobs.gov",
    "User-Agent": "INSERT YOUR EMAIL AS A STRING",
    "Authorization-Key": "INSERT YOUR KEY AS A STRING"
}
search_param = "?JobCategoryCode=2210&Keyword=Software Development&LocationName=Washington&ResultsPerPage=1"

# Send the GET request
response = requests.get(url + search_param, headers=headers)

# Check the response status code
if response.status_code == 200:
    # Request successful
    data = response.json()

    # Write the response data to a file
    with open("response_data.json", "w") as file:
        file.write(str(data))

    print("Request successful! Response data saved to 'response_data.json'.")
else:
    # Request failed
    print("Request failed with status code:", response.status_code)
