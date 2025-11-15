from products.data import PRODUCTS
from products.exceptions import CategoriNotFoundError

def get_all_categories():
    return [
        {
            "slug": categori_key,
            "title": categori_data["title"],
            "description": categori_data["description"]
        }
        for categori_key, categori_data in PRODUCTS.items()
    ]

def get_categori_data_by_slug(slug):
    if slug not in PRODUCTS:
        raise CategoriNotFoundError
    categori_data = PRODUCTS[slug]
    return {
        "title": categori_data["title"],
        "products": [
            {
                "id": idx,
                "name": product["name"],
                "brand": product["brand"],
                "price": product["price"],
                "stock": product["stock"],
                # "type": product["type"],
                "image_url": product["image_url"],
            }
            for idx, product in enumerate(categori_data["products"])
        ],
    }
