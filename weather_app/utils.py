import json
from requests import get
from weather_app.keys import WEATHER_API_KEY

city = "Odesa"

# GET IT FROM https://home.openweathermap.org/api_keys
key = WEATHER_API_KEY
# GET IT FROM https://home.openweathermap.org/api_keys

def get_weather_by_city(city: str):
    weather_api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}&units=metric"
    response = get(weather_api)
    data = json.loads(response.text)
    return data

get_weather_by_city(city)
