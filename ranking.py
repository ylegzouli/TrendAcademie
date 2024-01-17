from collections import Counter
from typing import List
from data_class import News
from news_to_csv import mock_news
import pandas as pd

def news_to_product_occurence(news_list: List[News]) -> pd.DataFrame:
    """
    Counts the occurrences of each product in the news list and returns a DataFrame.
    """
    product_list = [product for news in news_list for product in news.product_list]
    product_counts = dict(Counter(product_list))
    df = pd.DataFrame(list(product_counts.items()), columns=['product_name', 'occurrences'])
    df.sort_values(by='occurrences', ascending=False, inplace=True)
    return df

def news_to_brand_occurence(news_list: List[News]) -> pd.DataFrame:
    """
    Counts the occurrences of each brand in the news list and returns a DataFrame.
    """
    brand_list = [brand for news in news_list for brand in news.brand_list]
    brand_counts = dict(Counter(brand_list))
    df = pd.DataFrame(list(brand_counts.items()), columns=['brand_name', 'occurrences'])
    df.sort_values(by='occurrences', ascending=False, inplace=True)
    return df

def mock_products():
    return news_to_product_occurence(mock_news(20)).to_dict(orient='records')

def mock_brands():
    return news_to_brand_occurence(mock_news(20)).to_dict(orient='records')