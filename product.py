#%%
import pandas as pd
from data_class import News

DATA = pd.read_csv("data/sephora.csv")

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

    # Create a date range covering all dates
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

    # Rolling sum for the past 7 days
    df['CumulativeMentions'] = df['Mentions'].rolling('7D').sum()

    # Reset index to use Date in plotting
    df.reset_index(inplace=True)

    # Plotting
    fig = px.line(df, x='Date', y='CumulativeMentions', title=f'7-Day Rolling Sum of {product_name} Mentions in News')
    fig.update_xaxes(
        tickformat='%Y-%m-%d',
        dtick="D1",  # Daily ticks
        ticklabelmode="period"
    )
    fig.show()

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