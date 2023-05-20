import requests
import json

base_url = "http://api.weatherapi.com/v1"
endpoint = "/current.json"
api_key = "e69e523d9ed04abf8a2162555231705"
country = input("Select the Country")

request_url = f"{base_url}{endpoint}?key={api_key}&q={country}"

response = requests.get(request_url)

weather_data = response.json()

current_temp = weather_data["current"]["temp_c"]

print(f"Temprature of {country} is {current_temp}C")

city = input()
