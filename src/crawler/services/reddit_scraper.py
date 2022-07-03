import datetime
import logging
import os
from typing import List

from praw import Reddit

logger = logging.getLogger(__name__)


def create_client():
    """
    Creates a Reddit client from environment variables
    """
    client_id: str = os.getenv('clientId')
    client_secret: str = os.getenv('clientSecret')
    user_agent: str = os.getenv('userAgent')
    username: str = os.getenv('username')

    return Reddit(client_id=client_id,
                  client_secret=client_secret,
                  user_agent=user_agent,
                  username=username)


class RedditScraper:

    def __init__(self):
        self._client = create_client()

    def crawl_subreddit(self, subreddit: str, posts_per_category=250):
        logger.debug(f'Crawling subreddit {subreddit}')
        subreddit = self._client.subreddit(subreddit)

        # Get all the categories
        top_posts = list(subreddit.top(limit=posts_per_category))
        hot_posts = subreddit.hot(limit=posts_per_category)
        new_posts = subreddit.new(limit=posts_per_category)
        controversial_posts = subreddit.controversial(limit=posts_per_category)
        rising_posts = subreddit.rising(limit=posts_per_category)

        result = {}
        for posts in [top_posts, hot_posts, new_posts, controversial_posts, rising_posts]:
            for post in posts:
                result[post.id] = post

        return result

    def crawl_subreddits(self, subreddits: List[str], posts_per_category=250):
        result = {}
        for subreddit in subreddits:
            result[subreddit] = self.crawl_subreddit(subreddit, posts_per_category)

        return result
