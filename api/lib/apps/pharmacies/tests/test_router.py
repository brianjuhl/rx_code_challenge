import unittest
import json

from unittest.mock import patch
from fastapi.testclient import TestClient

from ....database import connect_to_mongo_service, is_mongo_service_connected, disconnect_from_mongo_service
from .....main import app
from ..router import mongo_service
from ..models import Pharmacy


def seed_test_database():
    test_pharmacies = [
        {
            "name": "WALGREENS",
            "address": "3696 SW TOPEKA BLVD",
            "city": "TOPEKA",
            "state": "KS",
            "zip_code": 66611,
            "latitude": 39.001423,
            "longitude": -95.68695
        },
        {
            "name": "KMART PHARMACY",
            "address": "1740 SW WANAMAKER ROAD",
            "city": "TOPEKA",
            "state": "KS",
            "zip_code": 66604,
            "latitude": 39.03504,
            "longitude": -95.7587
        }
    ]

    for pharmacy in test_pharmacies:
        Pharmacy(**pharmacy).save()


async def mongo_service_mock():
    connect_to_mongo_service("mongomock://localhost")
    # seed test database
    seed_test_database()
    try:
        yield is_mongo_service_connected()
    finally:
        # close db connection after response
        disconnect_from_mongo_service()

app.dependency_overrides[mongo_service] = mongo_service_mock

class TestRouter(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def tearDown(self):
        """disconnect test database"""
        disconnect_from_mongo_service()

    def test_post_pharmacies(self):
        """
        post request to /pharmacies route with 
        valid data responds with status 200
        """

        location = {
            "latitude": 0,
            "longitude": 0
        }

        location_string = json.dumps(location)

        response = self.client.post("/pharmacies/", location_string)
        self.assertEqual(response.status_code, 200)

    def test_get_pharmacies(self):
        """get request to /pharmacies responds with status 405"""
        response = self.client.get("/pharmacies")
        self.assertEqual(response.status_code, 405)
