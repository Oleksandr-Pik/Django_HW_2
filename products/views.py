from django.shortcuts import render
from products.utils import get_all_categories, get_categori_data_by_slug
from django.http import HttpRequest, HttpResponseNotFound
from products.exceptions import CategoriNotFoundError


def all_categori_page(request: HttpRequest):
    categories = get_all_categories()

    context = {
        "categories": categories
    }

    return render(request, "products/index.html", context)


def categori_page(request: HttpRequest, categori_slug: str):
    try:
        categori = get_categori_data_by_slug(categori_slug)
    except CategoriNotFoundError:
        return HttpResponseNotFound("Categori not found")

    context = {
        'categori': categori
    }

    return render(request, "products/categori.html", context)
