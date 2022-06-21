from src.crawler.reddit.reddit_crawler import create_client
from src.utils.env import init_env
import os

init_env()

subreddit = 'leagueoflegends'
client = create_client()


hot100 = client.subreddit(subreddit).hot(100)

for hot in hot100:
    print(hot)
