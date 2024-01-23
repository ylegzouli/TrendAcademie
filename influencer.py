import pandas as pd
from typing import List, Dict
from data_class import News
import os
from collections import Counter
from product import get_product_brand, get_product_id, get_product_image

DATA = pd.read_csv("data/influencers.csv")

def get_influencer_id(influencer_name: str) -> int:
    try:
        return DATA[DATA["name"] == influencer_name].index.values[0]
    except:
        return 0

# def get_influencer_image(influencer_name: str) -> str:
#     try:
#         return DATA[DATA["name"] == influencer_name]["image"].values[0]
#         return os.path.splitext(DATA[DATA["name"] == influencer_name]["image"].values[0])[0]
#     except:
#         return ""

# def get_influencer_followers(influencer_id: int) -> str:
#     try:
#         return DATA[DATA.index == influencer_id]["followers"].values[0]
#     except:
#         return ""

def get_influencer_total_likes(news_list: List[News]) -> Dict[str, int]:
    influencer_likes = {}
    for news in news_list:
        if news.username in influencer_likes:
            influencer_likes[news.username] += news.likes
        else:
            influencer_likes[news.username] = news.likes
    sorted_influencer_likes = dict(sorted(influencer_likes.items(), key=lambda item: item[1], reverse=True))
    return sorted_influencer_likes

def get_influencer_top_products(news: List[News], username: str):
    products = []
    for new in news:
        if new.username == username:
            for product in new.product_list:
                products.append(product)
    top_products = {}
    product_counts = Counter(products)
    top_products = dict(sorted(product_counts.items(), key=lambda item: item[1], reverse=True))
    if not top_products:
        return ""
    ret = []
    for product, count in top_products.items():
        ret.append({
            "id": str(get_product_id(product)),
            "name": product,
            "image": get_product_image(product),
            "brand": get_product_brand(get_product_id(product))
        })
    return ret