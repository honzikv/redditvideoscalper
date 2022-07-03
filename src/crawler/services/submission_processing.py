from datetime import datetime
from typing import Dict, Iterable

import praw.models

from src.crawler.persistence.models.comment import Comment
from src.crawler.persistence.models.post import Post
from src.utils.markdown import convert_markdown_text_to_plaintext

MAX_COMMENTS_PER_SUBMISSION = 250


def map_comments(comments: Iterable, max_comments=MAX_COMMENTS_PER_SUBMISSION, fetch_more_comments=False):
    """
    Maps a list of comments from PRAW to a list of Comment objects
    :param max_comments: max number of comments to map
    :param comments:
    :return:
    """
    mapped_comments = []  # list of all mapped comments
    for comment in comments:
        if isinstance(comment, praw.models.MoreComments):
            if fetch_more_comments:
                comment.comments(comment.count)
            else:
                continue

        if comment.author is None:
            continue

        mapped_comments.append(
            Comment(
                _id=comment.id,
                text=convert_markdown_text_to_plaintext(comment.body),  # text is stored in markdown so remove all tags
                author=comment.author.name,
                # convert from unix timestamp to python datetime
                datetime_created=datetime.fromtimestamp(comment.created_utc),
                num_upvotes=comment.score,
                # children are mapped recursively, this could be done more efficiently but it will suffice for now
                children=map_comments(comment.replies)
            )
        )

        if len(mapped_comments) >= max_comments:
            return mapped_comments

    # Return the mapped list
    return mapped_comments


def process_text_submissions(submission: Dict[str, praw.models.Submission],
                             max_comments_per_submission=MAX_COMMENTS_PER_SUBMISSION):
    """
    Processes a submission from PRAW and returns a Post object that can be persisted in the database
    :param max_comments_per_submission: max comments per submission that are extracted
    :param submission:
    :return:
    """
    result = []
    for submission in submission.values():
        # Filter out non-text posts
        if not submission.is_self or submission.selftext is None:
            continue

        result.append(
            Post(
                _id=submission.id,
                title=submission.title,
                text=submission.selftext,
                num_upvotes=submission.score,
                comments=map_comments(submission.comments)
            )
        )

    return result
