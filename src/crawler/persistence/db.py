import os

from pymongo import MongoClient

_database = None


def get_database():
    """
    Returns a MongoDB database object
    :return:
    """
    global _database
    if _database is None:
        _database = MongoClient(os.getenv('mongoConnectionString'))[os.getenv('mongoDatabaseName')]
    return _database
