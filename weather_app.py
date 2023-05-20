import requests
import json
import tkinter as tk
import urllib.request

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
    country = enter_country.get()
    city = enter_city.get()
    n_days = int(enter_days.get())

    current_temp = get_current_weather(country)
    label_temp.config(text=f"Temprature in {city}, {country} is {current_temp} ")

    forecast_data = get_forecast(city, n_days)
    forecast_days = forecast_data["forecast"]["forecastday"]

    forecast_text = ""
    for day in forecast_days:
        forecast_date = day["date"]
        forecast_temp = day["day"]["avgtemp_c"]
        forecast_text += f"forecast for {forecast_date} is {forecast_temp}C\n"
    label_forecast.config(text=forecast_text)

    air_quality_index = get_air_quality(city)
    label_aqi.config(text=f"Air Quality Index in {city} is {air_quality_index}")

window = tk.Tk()

label_country = tk.Label(window, text="Select the Country:")
label_country.pack()

enter_country = tk.Entry(window)
enter_country.pack()

label_city = tk.Label(window, text="Enter the city here:")
label_city.pack()

enter_city = tk.Entry(window)
enter_city.pack()

label_days = tk.Label(window, text="Enter the no. of days:")
label_days.pack()

enter_days = tk.Entry(window)
enter_days.pack()

button = tk.Button(window, text="Get Weather", command=get_weather)
button.pack()

label_temp = tk.Label(window)
label_temp.pack()

label_forecast = tk.Label(window)
label_forecast.pack()

label_aqi = tk.Label(window)
label_aqi.pack()

window.mainloop()






