import requests
import os

API_KEY = os.environ.get("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

# Check status code
if response.status_code == 200:
  data = response.json()
  
  weather = data['weather'][0]
  print(f"Right now {city.capitalize()} has {weather['description']}") 

  temp_data = data['main']
  temperature = round(temp_data['temp'] - 273.15, 2)
  print(f"\nTemperature: {temperature}°C")
  print(f"Feels like: {temp_data['feels_like']}")

  print(f"The min is: {temp_data['temp_min']} and the max is: {temp_data['temp_max']}")
else:
  print("An error occurred.")
