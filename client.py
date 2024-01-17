import requests
from pprint import pprint

response = requests.get("http://localhost:8000/products")
pprint(response.json())