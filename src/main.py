from dotenv import load_dotenv
from os import path

_ENV_FILEPATH = path.join('..', '.env')


def main():

    # Load .env file
    load_dotenv(_ENV_FILEPATH)

