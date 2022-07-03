from dataclasses import dataclass
from typing import List

from src.crawler.persistence.base_model import BaseModel
from src.crawler.persistence.models.comment import Comment

POSTS_COLLECTION = 'Posts'


@dataclass
class Post(BaseModel):
    """
    A Reddit post
    """
    _id: str
    title: str  # post title
    text: str  # post text
    comments: List[Comment]  # list of comments
    num_upvotes: int  # post upvotes

    def __str__(self):
        return f""" Post:
            _id: {self._id}
            title: {self.title}
            text: {self.text}
            comments: {self.comments}
            num_upvotes: {self.num_upvotes}
        """
