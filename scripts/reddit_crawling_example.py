from src.crawler.services.reddit_scraper import create_client, RedditScraper
from src.crawler.services.submission_processing import process_text_submissions
from src.utils.env import init_env
import os

init_env('../.env')

scraper = RedditScraper()
posts = scraper.crawl_subreddit('python', 5)

posts = process_text_submissions(posts, 5)

for post in posts:
    print(post)
