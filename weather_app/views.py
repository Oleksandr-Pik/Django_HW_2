import json
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from weather_app.utils import get_weather_by_city


def weather_page(request:HttpRequest):
    return render(request, "weather_app/index.html")


def get_weather(request: HttpRequest, city: str):

    data = get_weather_by_city(city)
    
    weather_text =f"Зараз погода:\nТемпература повітря 🌡️ {data["main"]["temp"]}℃\nВологість {data["main"]["humidity"]}%\nШвидкість вітру 💨 {data["wind"]["speed"]}м/с\n{data["weather"][0]["description"]}"

    context = {
        "city": city,
        "text": weather_text,
    }

    return render(request, "weather_app/city_weather.html", context)

def get_weather_json(request: HttpRequest, city: str):

    resp = get_weather_by_city(city)

    context = {
        "city": city,
    }

    return JsonResponse(resp)
