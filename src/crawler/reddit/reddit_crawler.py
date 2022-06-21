import os

import praw

_CLIENT_ID = 'clientId'
_CLIENT_SECRET = 'clientSecret'
_USER_AGENT = 'userAgent'


def create_client(
        client_id: str = os.getenv(_CLIENT_ID),
        client_secret: str = os.getenv(_CLIENT_SECRET),
        user_agent: str = os.getenv(_USER_AGENT)
):
    """
    Creates a reddit client. By default all necessary values are loaded from .env file
    :param client_id: client id
    :param client_secret: client secret
    :param user_agent: user agent
    :return:
    """
    return praw.Reddit(client_id, client_secret, user_agent)
