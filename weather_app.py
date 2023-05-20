import requests
import json

base_url = "http://api.weatherapi.com/v1"
api_key = "e69e523d9ed04abf8a2162555231705"

def get_current_weather(country):
    endpoint = "/current.json"
    request_url = f"{base_url}{endpoint}?key={api_key}&q={country}"
    response = requests.get(request_url)
    weather_data = response.json()
    current_temp = weather_data["current"]["temp_c"]
    return current_temp

def get_forecast(city):
    endpoint = "/forecast.json"
    request_url = f"{base_url}{endpoint}?key={api_key}&q={city}"
    response = requests.get(request_url)
    forecast_data = response.json()
    forecast_day = forecast_data["forecast"]["forecastday"][0]["date"]
    forecast_temp = forecast_data["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
    return forecast_day, forecast_temp

def get_air_quality(city):
    endpoint = "/current.json"
    request_url = f"{base_url}{endpoint}?key={api_key}&q={city}&aqi=yes"
    response = requests.get(request_url)
    air_quality_data = response.json()
    air_quality_index = air_quality_data["current"]["air_quality"]["pm2_5"]
    return air_quality_index

def main():
    country = input("Select the country: ")
    city = input("Select the city: ")

    current_temp = get_current_weather(country)
    forecast_day, forecast_temp = get_forecast(city)
    air_quality_index = get_air_quality(city)

    print(f"Temprature in {city}, {country} is {current_temp}C")
    print(f"Forecast for {city} on {forecast_day} is {forecast_temp}C")
    print(f"AQI in {city} is {air_quality_index}")

if __name__ == "__main__":
    main()
