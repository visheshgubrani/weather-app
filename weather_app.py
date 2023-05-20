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

def get_forecast(city, days):
    endpoint = "/forecast.json"
    request_url = f"{base_url}{endpoint}?key={api_key}&q={city}&days={days}"
    response = requests.get(request_url)
    forecast_data = response.json()
    return forecast_data

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
    num_days = int(input("Enter the No. of days: "))
    

    current_temp = get_current_weather(country)
    print(f"Temprature in {city}, {country} is {current_temp}C")
    
    def print_forecast(forecast_data):
        forecast_days = forecast_data["forecast"]["forecastday"]

        for day in forecast_days:
            forecast_date = day["date"]
            forecast_temp = day["day"]["avgtemp_c"]
            print(f"forecast for {forecast_date}: {forecast_temp}C")
    forecast_data = get_forecast(city, num_days)
    print_forecast(forecast_data)
    
    
    air_quality_index = get_air_quality(city)
    print(f"AQI in {city} is {air_quality_index}")

if __name__ == "__main__":
    main()
