import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "imperial"}  # If you're from somewhere other than here change imperal to metric
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data["main"]["temp"]
    else:
        print("Error fetching weather data.")
        return None

def suggest_outfit(temperature):
    if temperature > 80:
        return "It's hot! How about shorts and a t-shirt, or a dress?"
    elif 60 <= temperature <= 80:
        return "Not too hot, not too cold. Jeans and a jacket should do."
    else:
        return "It's COLD!"

def main():
    #put your own api key here.  Don't save secrets to Github
    api_key = <INSERT API KEY>

    city = input("Enter your city: ")

    temperature = get_weather(api_key, city)

    if temperature is not None:
        outfit_suggestion = suggest_outfit(temperature)
        print(f"Suggested outfit: {outfit_suggestion}")

if __name__ == "__main__":
    main()