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

# import plotly.express as px
# from datetime import datetime, timedelta
# from typing import List, Optional, Any
# from pydantic import BaseModel, Field

# # Assuming the News class is defined as provided
# def plot_product_mentions(news_list: List[News], product_name: str):
#     # Filter news items that mention the product
#     filtered_news = [news for news in news_list if product_name in news.product_list]

#     # Extract dates and count mentions
#     mention_dates = {}
#     for news in filtered_news:
#         date = news.publishedAt
#         # Convert Unix timestamp to datetime
#         date = datetime.fromtimestamp(date)
#         mention_dates[date] = mention_dates.get(date, 0) + 1

#     # Create a date range covering all dates
#     if mention_dates:
#         start_date = min(mention_dates.keys())
#         end_date = max(mention_dates.keys())
#         total_days = (end_date - start_date).days
#         date_range = [start_date + timedelta(days=x) for x in range(total_days + 1)]
#     else:
#         return "No data available for this product."

#     # Prepare DataFrame
#     df = pd.DataFrame(date_range, columns=['Date'])
#     df.set_index('Date', inplace=True)
#     df['Mentions'] = 0

#     # Fill in the mentions
#     for date in mention_dates:
#         df.at[date, 'Mentions'] = mention_dates[date]

#     # Cumulative sum
#     df['CumulativeMentions'] = df['Mentions'].cumsum()

#     # Reset index to use Date in plotting
#     # df.reset_index(inplace=True)

#     # return df

#     # Plotting
#     fig = px.line(df, x=df.index, y='CumulativeMentions', title=f'Cumulative Time Series of {product_name} Mentions in News')
#     fig.update_xaxes(
#         tickformat='%Y-%m-%d',
#         dtick="D1",  # Daily ticks
#         ticklabelmode="period"
#     )
#     fig.show()

# %%


# from data_class import News
# import pickle

# news = pickle.load(open("data/news_data.pkl", "rb"))[0]

# df = plot_product_mentions(news, "Lash Paint™ Mascara")


# %%
