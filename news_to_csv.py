from data_class import News
from typing import List
from faker import Faker
import csv

def news_to_csv(news_list: List[News]):
    """
    Function to convert a list of News objects into a CSV file.
    """
    headers = ['idx', 'username', 'likes', 'comments', 'url', 'source_type', 'content', 'is_video', 'video_url', 'video_view_count', 'publishedAt', 'product_list', 'brand_list']
    with open('data/news.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for news in news_list:
            writer.writerow(news.model_dump())

def mock_news(n: int) -> List[News]:
    """
    Function to generate a list of n News objects with fake data for testing purposes.
    """
    fake = Faker()
    news_list = []
    product_names = [
        'Master Mattes™ Liquid Eyeliner',
        'Liquid Touch Foundation Brush',
        'EF 2 Makeup Brush',
        'Eye Basics Primer',
        'KissKiss Liplift Lipstick Primer',
        'Benefiance NutriPerfect Night Cream'
    ]
    for _ in range(n):
        news = News(
            idx=fake.random_int(),
            username=fake.name(),
            likes=fake.random_int(min=0, max=1000),
            comments=fake.random_int(min=0, max=1000),
            url=fake.url(),
            source_type=fake.word(),
            content=fake.text(),
            is_video=fake.boolean(),
            video_url=fake.url() if fake.boolean() else None,
            video_view_count=fake.random_int(min=0, max=10000) if fake.boolean() else None,
            publishedAt=fake.date_time(),
            product_list=[fake.random_element(product_names) for _ in range(2)],
            brand_list=[fake.word() for _ in range(2)]
        )
        news_list.append(news)
    return news_list

def main():
    news = mock_news(3)
    news_to_csv(news)

if __name__ == "__main__":
    main()