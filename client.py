import requests
from pprint import pprint

def get_products():
    response = requests.get("http://localhost:8000/products")
    pprint(response.json())

def get_brands():
    response = requests.get("http://localhost:8000/brands")
    pprint(response.json())

get_products()
get_brands()