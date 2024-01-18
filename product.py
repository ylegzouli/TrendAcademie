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

