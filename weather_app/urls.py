from django.urls import path
from weather_app.views import weather_page, get_weather, get_weather_json

urlpatterns = [
    path("", weather_page),
    path("<str:city>/", get_weather),
    path("<str:city>/json/", get_weather_json),
]
