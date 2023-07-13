import requests

url = "https://baseball4.p.rapidapi.com/players?"

querystring = "personIds=676265"

headers = {
	"X-RapidAPI-Key": "INSERT YOUR OWN API KEY HERE",
	"X-RapidAPI-Host": "baseball4.p.rapidapi.com"
}

response = requests.get(url + querystring, headers=headers)

print(response.json())