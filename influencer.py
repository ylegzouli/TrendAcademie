import pandas as pd
from typing import List, Dict
from data_class import News

DATA = pd.read_csv("data/influencers.csv")

def get_influencer_id(influencer_name: str) -> int:
    try:
        return DATA[DATA["name"] == influencer_name].index.values[0]
    except:
        return 0

def get_influencer_image(influencer_name: str) -> str:
    try:
        return DATA[DATA["name"] == influencer_name]["image"].values[0]
    except:
        return ""

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
