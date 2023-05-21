import requests
import json
import tkinter as tk

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

def get_weather():
    country = entry_country.get()
    city = entry_city.get()
    num_days = int(entry_days.get())
    
    current_temp = get_current_weather(country)
    label_temp.config(text=f"Temperature in {city}, {country} is {current_temp}°C")
    
    forecast_data = get_forecast(city, num_days)
    forecast_days = forecast_data["forecast"]["forecastday"]
    
    forecast_text = ""
    for day in forecast_days:
        forecast_date = day["date"]
        forecast_temp = day["day"]["avgtemp_c"]
        forecast_text += f"Forecast for {forecast_date}: {forecast_temp}°C\n"
    label_forecast.config(text=forecast_text)
    
    air_quality_index = get_air_quality(city)
    label_aqi.config(text=f"AQI in {city} is {air_quality_index}")

window = tk.Tk()

label_country = tk.Label(window, text="Select the country:")
label_country.pack()

entry_country = tk.Entry(window)
entry_country.pack()

label_city = tk.Label(window, text="Select the city:")
label_city.pack()

entry_city = tk.Entry(window)
entry_city.pack()

label_days = tk.Label(window, text="Enter the number of days:")
label_days.pack()

entry_days = tk.Entry(window)
entry_days.pack()

button = tk.Button(window, text="Get Weather", command=get_weather)
button.pack()

label_temp = tk.Label(window)
label_temp.pack()

label_forecast = tk.Label(window)
label_forecast.pack()

label_aqi = tk.Label(window)
label_aqi.pack()

window.mainloop()
