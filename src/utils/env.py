from os import path
from dotenv import load_dotenv

_ENV_FILEPATH = path.join('..', '.env')


def init_env():
    """
    Loads .env file to the app
    :return: None
    """
    load_dotenv(_ENV_FILEPATH)
