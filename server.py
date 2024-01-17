from fastapi import FastAPI
from ranking import mock_products

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/products")
def get_products():
    return mock_products()
