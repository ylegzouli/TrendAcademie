
"""
This module contains the functions to extract data from multiple sources and create unified News objects.
"""

#%%
import feedparser
from datetime import datetime, timedelta
from newspaper import Article

from data_class import News

#%%
# FEEDS EXTRACTOR:

feed_urls = [
    "https://www.allure.com/feed/rss",
    "https://www.barbiesbeautybits.com/feeds/posts/default?alt=rss",
    "https://thedermreview.com/feed/",
    "http://www.beautycrazed.ca/feeds/posts/default?alt=rss",
    "https://feeds.feedburner.com/nymag/fashion", 
]

def extract_url_from_rss(rss_url: str, nb_days: int = 30) -> list:
    """
    Extracts the URLs from the RSS feed of a website.
        Args:
            rss_url (str): URL of the RSS feed.
            nb_days (int, optional): Number of days to look back. Defaults to 30.
        Returns:
            list: List of URLs.
    """
    # Parse the feed
    entries = []
    feed = feedparser.parse(rss_url)
    entries.extend(feed.entries)
    # Get the current date and time
    current_time = datetime.now()
    # List to store recent article links
    recent_articles = []
    # Iterate through the feed entries
    for entry in entries:
        # Parse the publish date of the article
        published_time = datetime(*entry.published_parsed[:6])
        # Check if the article is from the last 24 hours
        if current_time - published_time < timedelta(days=nb_days):
            article_url = entry.link  # URL of the article
            recent_articles.append(article_url)  # Save the URL to the list

    return recent_articles


def extract_urls_from_rss(rss_urls: list, nb_days: int=30) -> list:
    """
    Extracts the URLs from the RSS feed of a list of websites.
        Args:
            rss_urls (list): List of URLs of the RSS feeds.
            nb_days (int, optional): Number of days to look back. Defaults to 30.
        Returns:
            list: List of URLs.
    """
    recent_articles = []
    for rss_url in rss_urls:
        recent_articles.extend(extract_url_from_rss(rss_url, nb_days))
    
    return recent_articles

def create_article_from_url(url: str) -> News:
    """
    Creates a News object from the URL of an article.
        Args:
            url (str): URL of the article.
        Returns:
            News: News object.
    """
    try:
        article = Article(url)
        article.download()
        article.parse()

        news = News(
            title=article.title,
            url=article.url,
            source_type="newsfeed",
            content=article.text,
            publishedAt=article.publish_date,
        )
        return news
    except Exception as e:
        raise e

def create_articles_from_urls(urls: list) -> "list[News]":
    """
    Creates a list of News objects from a list of URLs.
        Args:
            urls (list): List of URLs.
        Returns:
            list: List of News objects.
    """
    news_list = []
    for url in urls:
        try:
            news_list.append(create_article_from_url(url))
        except Exception as e:
            print(e)
            pass
    return news_list

def create_news_rss_feeds(
        rss_urls: "list[str]"=feed_urls, 
        nb_days: int=30
) -> "list[News]":
    """
    Creates a list of News objects from a list of RSS feeds.
        Args:
            rss_urls (list, optional): List of URLs of the RSS feeds. Defaults to feed_urls.
            nb_days (int, optional): Number of days to look back. Defaults to 30.
        Returns:
            list: List of News objects.
    """
    urls = extract_urls_from_rss(rss_urls, nb_days)
    news_list = create_articles_from_urls(urls)

    return news_list

#%%
# TWITTER EXTRACTOR:


#%%
# YOUTUBE EXTRACTOR:

#%%
# TIKTOK EXTRACTOR:


#%%
# INSTAGRAM EXTRACTOR:


#%%
# GENERAL EXTRACTOR:

def extractor(nb_days: int=30) -> "list[News]":
    """
    Extract data from the web and create a list of News objects.
        Args:
            nb_days (int, optional): Number of days to look back. Defaults to 30.
        Returns:
            list: List of News objects.
    """
    news_list = []
    news_list.extend(create_news_rss_feeds(nb_days=nb_days))
    # news_list.extend(create_news_twitter(nb_days=nb_days))
    # news_list.extend(create_news_youtube(nb_days=nb_days))
    # news_list.extend(create_news_tiktok(nb_days=nb_days))
    # news_list.extend(create_news_instagram(nb_days=nb_days))
    
    return news_list

#%%