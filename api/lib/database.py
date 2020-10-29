import os
from mongoengine import connect, disconnect, errors


def connect_to_mongo_service():
    """Connect to mongo service by URI exposed by docker network"""
    mongo_uri = os.environ["MONGO_URI"]
    connect("rx_code_challenge_pharmacies", host=mongo_uri)


def disconnect_from_mongo_service():
    """Disconnect from mongo service"""
    disconnect()
