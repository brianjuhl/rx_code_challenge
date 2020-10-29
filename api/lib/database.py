import os
import sys
import mongomock
from mongoengine import connect, disconnect, errors, get_connection, connection

class MongoURIError(Exception):
    pass

def connect_to_mongo_service(mongo_uri=None):
    """ 
    Connect to mongo uri explicitly provided or by default, 
    the URI exposed by docker network
    """

    if not mongo_uri:
        try: 
            mongo_uri = os.environ["MONGO_URI"]
        except KeyError:
            raise MongoURIError("mongo_uri not provided")

    connect("rx_code_challenge_pharmacies", host=mongo_uri)


def disconnect_from_mongo_service():
    """Disconnect from mongo service"""
    disconnect()


def is_mongo_service_connected():
    """
    Use ismaster command to test db connection
    pymongo no longer raises an exception when connecting
    """
    try:
        conn = get_connection()
        return True
    except connection.ConnectionFailure:
        return False
