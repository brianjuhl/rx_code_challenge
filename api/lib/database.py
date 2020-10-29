import os
from mongoengine import connect, disconnect, errors


def connect_to_mongo_service(mongo_uri):
    """ 
    Connect to mongo uri explicitly provided or by default, 
    the URI exposed by docker network
    """
    connect("rx_code_challenge_pharmacies", host=mongo_uri)


def disconnect_from_mongo_service():
    """Disconnect from mongo service"""
    disconnect()
