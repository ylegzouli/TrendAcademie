#%%
import pandas as pd
from data_class import News
import json

DATA = pd.read_csv("data/sephora.csv")
data_similar = json.load(open("data/products_data_with_idx.json", "r"))

#%%

def get_product_id(product_name: str) -> int:
    """
    """
    try:
        return DATA[DATA["Product"] == product_name].index.values[0]
    except:
        return 0

def get_product_image(product_name: str) -> str:
    """
    """
    try:
        return DATA[DATA["Product"] == product_name]["image"].values[0]
    except:
        return ""
    
def get_product_name(product_id: int) -> str:
    """
    """
    try:
        return DATA[DATA.index == product_id]["Product"].values[0]
    except:
        return ""

def get_product_brand(product_id: int) -> str:
    """
    """
    try:
        return DATA[DATA.index == product_id]["Brand"].values[0]
    except:
        return ""

def get_product_description(product_id: int) -> str:
    """
    """
    try:
        return DATA[DATA.index == product_id]["description"].values[0]
    except:
        return ""

def get_influencer(product_id: int, news: list[News]) -> str:
    """
    """
    influencer = []
    try:
        for n in news:
            if get_product_name(product_id) in n.product_list:
                influencer.append(n.username)
        return list(set(influencer))
    except:
        return []
    

def get_similar(product_id: int) -> list:
    """
    """
    try:
        return data_similar[get_product_name(product_id)]
    except:
        return []


#%%

import plotly.express as px
from datetime import datetime, timedelta
from typing import List, Optional, Any
from pydantic import BaseModel, Field

# Assuming the News class is defined as provided
def plot_product_mentions(news_list: List[News], product_name: str):
    # Filter news items that mention the product
    filtered_news = [news for news in news_list if product_name in news.product_list]

    # Extract dates and count mentions
    mention_dates = {}
    for news in filtered_news:
        date = news.publishedAt
        # Convert Unix timestamp to datetime
        f_date = datetime.fromtimestamp(date).strftime('%Y-%m-%d')
        date = datetime.strptime(f_date, '%Y-%m-%d')
        mention_dates[date] = mention_dates.get(date, 0) + 1

    # return mention_dates

    # # Create a date range covering all dates
    if mention_dates:
        start_date = min(mention_dates.keys())
        end_date = max(mention_dates.keys())
        total_days = (end_date - start_date).days
        date_range = [start_date + timedelta(days=x) for x in range(total_days + 1)]
    else:
        return "No data available for this product."
    


    # Prepare DataFrame
    df = pd.DataFrame(date_range, columns=['Date'])
    df.set_index('Date', inplace=True)
    df['Mentions'] = 0

    # Fill in the mentions
    for date in mention_dates:
        df.at[date, 'Mentions'] = mention_dates[date]

    # return df

    # Rolling sum for the past 7 days
    df['CumulativeMentions'] = df['Mentions'].rolling('7D').sum()

    # Reset index to use Date in plotting
    df.reset_index(inplace=True)

    # Plotting
    fig = px.line(df, x='Date', y='Mentions' * 4, title=f'7-Day Rolling Sum of {product_name} Mentions in News')
    fig.update_xaxes(
        tickformat='%Y-%m-%d',
        dtick="D1",  # Daily ticks
        ticklabelmode="period"
    )
    fig.show()

#%%
import pickle

sample_news = pickle.load(open("data/news_data.pkl", "rb"))[0]


# Sample product list
# product_list = ["Master Mattes™ Liquid Eyeliner", "Blush/Bronzer Duo"]
product_list = DATA["Product"].values.tolist()

def generate_product_ranking_dataframe(news_list: List[News], products: List[str]) -> pd.DataFrame:
    
        # Convert 'publishedAt' from timestamp to formatted date string in each News object
    for news in news_list:
        # Convert to datetime object and format
        news.publishedAt = datetime.fromtimestamp(news.publishedAt).strftime('%Y-%m-%d')

    # Convert 'publishedAt' back to datetime objects for further processing
    for news in news_list:
        news.publishedAt = datetime.strptime(news.publishedAt, '%Y-%m-%d')
    
    # Find the last news date
    last_news_date = max(news.publishedAt for news in news_list)

    # Calculate date range (one month before last news date to last news date)
    start_date = last_news_date - timedelta(days=30)
    date_range = pd.date_range(start=start_date, end=last_news_date)

    # Initialize a dictionary to hold product mention counts
    product_mentions = {date: {product: 0 for product in products} for date in date_range}

    # Count cumulative product mentions for each day
    for news in news_list:
        if news.publishedAt >= start_date:
            for date in date_range[date_range >= news.publishedAt]:
                for product in news.product_list:
                    if product in products:
                        product_mentions[date][product] += 1

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame.from_dict(product_mentions, orient='index')

    # Rank products for each day
    for date in df.index:
        df.loc[date] = df.loc[date].rank(method='min', ascending=False)

    return df


def generate_7day_product_ranking_dataframe(news_list: List[News], products: List[str]) -> pd.DataFrame:
    
        # Convert 'publishedAt' from timestamp to formatted date string in each News object
    for news in news_list:
        # Convert to datetime object and format
        news.publishedAt = datetime.fromtimestamp(news.publishedAt).strftime('%Y-%m-%d')

    # Convert 'publishedAt' back to datetime objects for further processing
    for news in news_list:
        news.publishedAt = datetime.strptime(news.publishedAt, '%Y-%m-%d')
    
    # Find the last news date
    last_news_date = max(news.publishedAt for news in news_list)

    # Calculate date range (one month before last news date to last news date)
    start_date = last_news_date - timedelta(days=30)
    date_range = pd.date_range(start=start_date, end=last_news_date)

    # Initialize a dictionary to hold product mention counts
    product_mentions = {date: {product: 0 for product in products} for date in date_range}

    # Count product mentions within a rolling 7-day window for each day
    for date in date_range:
        start_window = date - timedelta(days=7)
        for news in news_list:
            if start_window < news.publishedAt <= date:
                for product in news.product_list:
                    if product in products:
                        product_mentions[date][product] += 1

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame.from_dict(product_mentions, orient='index')

    # Rank products for each day
    for date in df.index:
        df.loc[date] = df.loc[date].rank(method='min', ascending=False)

    return df



# Generate the DataFrame
# df = generate_7day_product_ranking_dataframe(sample_news, product_list)
# df = generate_product_ranking_dataframe(sample_news, product_list)
# df.head()  # Display the first few rows of the DataFrame
# #%%

# print(df["Master Mattes™ Liquid Eyeliner"].index)


#%%

# fig = px.line(df, x=df.index, y='Master Mattes™ Liquid Eyeliner', title=f'Ranking evolution of sephora products')
# # fig = px.line(df, x=df.index, y='Lip Liner', title=f'7-Day Rolling Sum of Mentions in News')
# fig.update_xaxes(
#         tickformat='%Y-%m-%d',
#         dtick="D1",  # Daily ticks
#         ticklabelmode="period"
#     )
# fig.update_yaxes(autorange='reversed') 
# fig.show()



#%%

# df.to_csv("data/product_ranking_7day.csv")



#%%
    

def process_news(news_list: List[News]):
    all_news = news_list
    if not news_list:
        return [], [], []

    # Convert publishedAt to datetime if necessary and find the latest date
    def to_datetime(date):
        if isinstance(date, str):
            return datetime.fromisoformat(date)
        elif isinstance(date, int):
            return datetime.fromtimestamp(date)
        return date

    # Find the latest date among the news and convert it to datetime
    last_news_timestamp = max(news.publishedAt for news in news_list)
    last_news_date = to_datetime(last_news_timestamp)

    def is_recent(news, reference_date, days):
        """ Check if the news is within the given days before the reference date """
        news_date = to_datetime(news.publishedAt)
        return news_date >= reference_date - timedelta(days=days)

    last_7_days_news = [news for news in news_list if is_recent(news, last_news_date, 7)]
    last_day_news = [news for news in news_list if is_recent(news, last_news_date, 1)]

    return all_news, last_7_days_news, last_day_news

# %%