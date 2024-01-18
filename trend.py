"""
"""
#%%
import openai
import json
from typing import List, Optional, Tuple
import pandas as pd
from fuzzywuzzy import fuzz
from dotenv import load_dotenv
import os

from data_class import News

#%%
load_dotenv()

API_KEY = os.getenv("API_KEY")
ASSISTANT_ID = os.getenv("ASSISTANT_ID")
DATA = pd.read_csv("data/sephora.csv")

#%%
# use openAI Assistant to extract product and brand from article content

def find_product_and_brand(article_content: str) -> Optional[dict]:
    """
    """
    messages = [
        {"role": "user", "content": article_content},
    ]
    client = openai.OpenAI(api_key=API_KEY)
    assistant = client.beta.assistants.retrieve(
        ASSISTANT_ID
    )
    thread = client.beta.threads.create(
        messages=messages
    )
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id
    )
    tool_outputs = []
    while run.status != 'completed':
        run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
                )
        messages = client.beta.threads.messages.list(
                thread_id=thread.id
                )
        if run.required_action and run.required_action.submit_tool_outputs and run.required_action.submit_tool_outputs.tool_calls:
            for tool_call in run.required_action.submit_tool_outputs.tool_calls:
                tool_call_id = tool_call.id
                arguments = json.loads(tool_call.function.arguments)
                response = arguments  # arguments is the response
                tool_outputs.append({
                    "tool_call_id": tool_call_id,
                    "outputs": {"response": response}
                })
                return response
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        if run.status =="succeeded":
            #Actual code never enter here
            messages = client.beta.threads.messages.list(
                thread_id=thread.id
            )
            return messages
        elif run.status == "cancelled" or run.status == "failed":
            raise "thread cancelled"
        elif run.status == "in_progress":
            #wait for next iteration
            import time
            time.sleep(5)

    return None

def get_raw_product_and_brand(article_content: str) -> Tuple[List[str], List[str]]:
    """
    """
    list_of_product = []
    list_of_brand = []
    try:
        raw_product_and_brand = find_product_and_brand(article_content)
        keys = list(raw_product_and_brand.keys())
        for key in keys:
            if key == "products":
                list_of_product.extend(raw_product_and_brand[key].split(", "))
            if key == "brands":
                list_of_brand.extend(raw_product_and_brand[key].split(", "))
    except Exception as e:
        print(e)
        pass
    
    return list_of_product, list_of_brand


#%%
# Match product and brand with database

def calculate_similarity(series, input_string):
    """
    calculate similarity between input string and a series of string
    """
    return series.apply(lambda x: fuzz.ratio(x, input_string))


def match_product_and_brand(list_of_product: List[str], list_of_brand: List[str]) -> Tuple[List[str], List[str]]:
    """
    Compare list of product and brand with database
    """
    product_data = DATA['Product']
    brand_data = DATA['Brand']
    product_match = []
    brand_match = []
    for product in list_of_product:
        similarity_scores = calculate_similarity(product_data, product)
        if similarity_scores.max() > 75:
            print(DATA.iloc[similarity_scores.idxmax()])
            print(f"product: {product}")
            print(f"score: {similarity_scores.max()}")
            print("--------------------------------------------------")
            product_match.append(DATA.iloc[similarity_scores.idxmax()]['Product'])

    for brand in list_of_brand:
        similarity_scores = calculate_similarity(brand_data, brand)
        if similarity_scores.max() > 80:
            print(DATA.iloc[similarity_scores.idxmax()])
            print(f"brand: {brand}")
            print(f"score: {similarity_scores.max()}")
            print("--------------------------------------------------")
            brand_match.append(DATA.iloc[similarity_scores.idxmax()]['Brand'])

    return product_match, brand_match

#%%

def run_trend(new: News) -> News:
    """
    """
    print(f"\nProcessing {new.url}")
    product_list, brand_list = get_raw_product_and_brand(new.content)
    new.product_list, new.brand_list = match_product_and_brand(product_list, brand_list)

    return news


def run_trend_for_list_of_news(news_list: List[News]) -> List[News]:
    """
    """
    news_list_ok = []
    for new in news_list:
        new_ok = run_trend(new)
        news_list_ok.append(new_ok) 

    return news_list_ok


#%%
# Test

from extractor import extractor

news = extractor(nb_days=30)
print(len(news))

#%%

news = run_trend_for_list_of_news(news)


#%%
# import pickle 
# print(len(news))

# print("Serialize and save the list using pickle")
# with open('data/news_data.pkl', 'wb') as file:
#     pickle.dump(news, file)

#%%
# news_to_csv(news)
import pickle 
with open('data/news_data.pkl', 'rb') as file:
    loaded_news_list = pickle.load(file)

#%%
print(loaded_news_list[0])


#%%
from ranking import news_to_product_occurence, news_to_brand_occurence

df_product = news_to_product_occurence(loaded_news_list[0])

#%%

df_brand = news_to_brand_occurence(loaded_news_list[0])

#%%

print(df_product)

# %%

for new in loaded_news_list[0]:
    if new.is_video:
        print(new.video_url)

# for product in products:
#     print(product)

# print("--------------------------------------------------")

# for brand in brands:
#     print(brand)
# print("--------------------------------------------------")

# %%

# %%

data = pd.read_csv("data/news.csv")

# %%
