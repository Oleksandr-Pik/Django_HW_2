from django.urls import path
from main.views import hello_by_name, json, file, math

urlpatterns = [
    path("hello/", hello_by_name),
    path("hello/<str:name>/", hello_by_name),
    path("json/", json),
    path("file/", file),
    path("math/<int:num1>/<int:num2>/", math),
]
