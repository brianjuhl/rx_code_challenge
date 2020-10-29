import unittest

import pymongo
import mongomock
from mongoengine import get_connection, connect
from pymongo.errors import ConnectionFailure
from .database import connect_to_mongo_service, disconnect_from_mongo_service, is_mongo_service_connected, MongoURIError


class TestPharmacyModels(unittest.TestCase):

    def tearDown(self):
        """disconnect test database"""
        disconnect_from_mongo_service()

    def test_connect_to_mongo_service(self):
        """successfully connects to database"""
        connect_to_mongo_service("mongomock://localhost")
        self.assertEqual(is_mongo_service_connected(), True)

    def test_disconnect_from_mongo_service(self):
        """successfully disconnects from database"""
        connect_to_mongo_service("mongomock://localhost")
        disconnect_from_mongo_service()
        self.assertEqual(is_mongo_service_connected(), False)

    def test_excepts_if_uri_not_provided(self):
        """raises exception if mongo_uri not set and env variable not found"""
        try:
            connect_to_mongo_service()
        except Exception as e:
            self.assertIsInstance(e, MongoURIError)
