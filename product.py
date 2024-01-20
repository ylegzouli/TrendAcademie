#%%
import pandas as pd
from data_class import News

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

def get_influencer(product_id: int, news: list[News]) -> str:
    """
    """
    influencer = []
    for n in news:
        if get_product_name(product_id) in n.product_list:
            influencer.append(n.username)
    return list(set(influencer))



#%%

import plotly.express as px
from datetime import datetime
from typing import List, Optional, Any
from pydantic import BaseModel, Field

# Assuming the News class is defined as provided

# def plot_product_mentions(news_list: List[News], product_name: str):
#     # Filter news items that mention the product
#     filtered_news = [news for news in news_list if product_name in news.product_list]

#     # Extract dates and count mentions
#     mention_dates = {}
#     for news in filtered_news:
#         date = news.publishedAt
#         # Assuming publishedAt is a datetime object; if not, convert it
#         if isinstance(date, str):
#             date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')  # Adjust the format as per your date string
#         mention_dates[date] = mention_dates.get(date, 0) + 1

#     # Create a DataFrame for plotting
#     import pandas as pd
#     df = pd.DataFrame(list(mention_dates.items()), columns=['Date', 'Mentions'])
#     df = df.sort_values('Date')

#     # Plotting
#     fig = px.line(df, x='Date', y='Mentions', title=f'Time Series of {product_name} Mentions in News')
#     fig.show()
# %%


# from data_class import News
# import pickle

# news = pickle.load(open("data/news_data.pkl", "rb"))[0]

# plot_product_mentions(news, "Lipstick")