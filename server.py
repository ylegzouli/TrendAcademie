from fastapi import FastAPI
from ranking import mock_products, mock_brands

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/products")
def get_products():
    return mock_products()

@app.get("/brands")
def get_brands():
    return mock_brands()
