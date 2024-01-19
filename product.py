#%%
import pandas as pd

DATA = pd.read_csv("data/sephora.csv")

#%%

def get_product_id(product_name: str) -> int:
    """
    """
    return DATA[DATA["Product"] == product_name].index.values[0]

def get_product_image(product_name: str) -> str:
    """
    """
    return DATA[DATA["Product"] == product_name]["image"].values[0]

def get_product_name(product_id: int) -> str:
    """
    """
    return DATA[DATA.index == product_id]["Product"].values[0]


def get_product_brand(product_id: int) -> str:
    """
    """
    return DATA[DATA.index == product_id]["Brand"].values[0]

def get_product_description(product_id: int) -> str:
    """
    """
    return DATA[DATA.index == product_id]["description"].values[0]


#%%
