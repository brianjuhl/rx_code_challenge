import os
from mongoengine import connect, disconnect, errors


def connect_to_mongo_service(mongo_uri=os.environ["MONGO_URI"]):
    """ 
    Connect to mongo uri explicitly provided or by default, 
    the URI exposed by docker network
    """
    return connect("rx_code_challenge_pharmacies", host=mongo_uri)


def disconnect_from_mongo_service():
    """Disconnect from mongo service"""
    disconnect()
