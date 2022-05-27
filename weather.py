import requests
import os

API_KEY = os.environ.get("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
KELVIN = 273.15

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

def to_celsius(temp):
  return f"{round(temp - KELVIN, 2)}°C"

# Check status code
if response.status_code == 200:
  data = response.json()
  
  weather = data['weather'][0]
  print(f"Right now {city.capitalize()} has {weather['description']}") 

  temp_data = data['main']

  print(f"\nTemperature: {to_celsius(temp_data['temp'])}")
  print(f"Feels like: {to_celsius(temp_data['feels_like'])}")

  print(
      f"The min is: {to_celsius(temp_data['temp_min'])} and the max is: {to_celsius(temp_data['temp_max'])}")
else:
  print("An error occurred.")
