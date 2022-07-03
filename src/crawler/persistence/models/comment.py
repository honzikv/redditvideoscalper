from dataclasses import dataclass
from datetime import datetime
from typing import List

from src.crawler.persistence.base_model import BaseModel

COMMENTS_COLLECTION = 'Comments'


@dataclass
class Comment(BaseModel):
    """
    Comment under a Reddit post
    """
    _id: str
    text: str  # comment text
    author: str  # comment author
    datetime_created: datetime  # comment date created
    num_upvotes: int  # comment upvotes
    children: List  # list of comments under this comment

    def __str__(self):
        return f""" Comment:
            _id: {self._id}
            text: {self.text}
            author: {self.author}
            date_created: {self.datetime_created}
            num_upvotes: {self.num_upvotes}
            children: {self.children}
            """
