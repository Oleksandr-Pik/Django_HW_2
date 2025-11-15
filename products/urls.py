from django.urls import path
from products.views import all_categori_page, categori_page

urlpatterns = [
    path("", all_categori_page, name="all_categori_page"),
    path("<slug:categori_slug>/", categori_page, name="categori_page"),
]
