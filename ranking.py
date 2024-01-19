from collections import Counter
from typing import List
from data_class import News
from news_to_csv import mock_news
import pandas as pd
import ast

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

def news_to_sephora_products(df_news: pd.DataFrame, df_sephora: pd.DataFrame) -> pd.DataFrame:
    """
    This function takes two dataframes as input, one containing news data and the other containing Sephora product data.
    It extracts the product names from the news data, finds the corresponding Sephora product IDs, and creates a new dataframe
    that maps each product name to its Sephora ID and the IDs of the news articles where it's mentioned.
    """

    df_news['product_list'] = df_news['product_list'].apply(ast.literal_eval)
    product_names = sum(df_news['product_list'].tolist(), [])
    product_names = list(set(product_names))

    df_products = pd.DataFrame([], columns=['product_name', 'id_sephora', 'id_news'])

    for product_name in product_names:
        id_news = df_news[df_news.product_list.apply(lambda x: product_name in x)].index.tolist()
        id_sephora = df_sephora[df_sephora.Product == product_name].index.tolist()[0]
        df_products = df_products._append({'product_name': product_name, 'id_sephora': id_sephora, 'id_news': id_news}, ignore_index=True)
    return df_products

def news_to_sephora_brands(df_news: pd.DataFrame) -> pd.DataFrame:

    df_news['brand_list'] = df_news['brand_list'].apply(ast.literal_eval)
    brand_names = sum(df_news['brand_list'].tolist(), [])
    brand_names = list(set(brand_names))

    df_brands = pd.DataFrame([], columns=['brand_name', 'id_news'])

    for brand_name in brand_names:
        id_news = df_news[df_news.brand_list.apply(lambda x: brand_name in x)].index.tolist()
        df_brands = df_brands._append({'brand_name': brand_name, 'id_news': id_news}, ignore_index=True)
    return df_brands

def get_top_products(df_products: pd.DataFrame, df_sephora: pd.DataFrame, n: int):
    """
    Sorts df_products by the length of 'id_news', takes the top n products, and returns the corresponding rows from df_sephora.
    """
    df_products['id_news_len'] = df_products['id_news'].apply(len)
    df_products = df_products.sort_values('id_news_len', ascending=False)
    df_products = df_products.drop(columns=['id_news_len'])

    top_product_names = df_products.head(n)['product_name'].values

    df_sephora_rows = pd.DataFrame()
    for product_name in top_product_names:
        df_sephora_row = df_sephora[df_sephora['Product'] == product_name]
        df_sephora_rows = pd.concat([df_sephora_rows, df_sephora_row])

    return df_sephora_rows

def get_top_brands(df_brands: pd.DataFrame, n: int):
    df_brands['id_news_len'] = df_brands['id_news'].apply(len)
    df_brands = df_brands.sort_values('id_news_len', ascending=False)
    df_brands = df_brands.drop(columns=['id_news_len'])
    top_brand_names = df_brands.head(n)['brand_name'].values
    return top_brand_names

# Function to calculate cumulative likes for a product
def get_cumulative_likes(product_name: str, news_list: List[News]) -> int:
    total_likes = 0
    for news in news_list:
        if product_name in news.product_list:
            total_likes += news.likes
    if total_likes <= 0:
        return 0
    return total_likes


def main():
    df_news = pd.read_csv('data/news.csv')
    df_sephora = pd.read_csv('data/sephora.csv')

    df_products = news_to_sephora_products(df_news, df_sephora)
    print(df_products)

    df_top_products = get_top_products(df_products, df_sephora, 1)
    print(df_top_products)

    df_brands = news_to_sephora_brands(df_news)
    print(df_brands)

    df_top_brands = get_top_brands(df_brands, 1)
    print(df_top_brands)

if __name__ == "__main__":
    main()
