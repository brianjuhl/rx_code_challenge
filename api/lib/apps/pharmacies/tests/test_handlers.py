import unittest

from ....database import connect_to_mongo_service, disconnect_from_mongo_service
from ..models import Pharmacy
from ..handlers import locate_nearest_pharmacy


class TestPharmacyHandlers(unittest.TestCase):

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
        },
        {
            "name": "CONTINENTAL PHARMACY LLC",
            "address": "821 SW 6TH AVE",
            "city": "TOPEKA",
            "state": "KS",
            "zip_code": 66603,
            "latitude": 39.05433,
            "longitude": -95.68453
        },
        {
            "name": "WALGREENS",
            "address": "9300 E GREGORY BLVD",
            "city": "RAYTOWN",
            "state": "MO",
            "zip_code": 64133,
            "latitude": 38.995342,
            "longitude": -94.4734
        }
    ]

    def setUp(self):
        """set up test database connection"""
        connect_to_mongo_service("mongomock://localhost")
        # fill mock database with test pharmacies
        for pharmacy in self.test_pharmacies:
            new_pharmacy = Pharmacy(**pharmacy)
            new_pharmacy.save()

    def tearDown(self):
        """disconnect test database"""
        disconnect_from_mongo_service()

    def test_locate_nearest_pharmacy(self):
        """successfully returns the nearest pharmacy"""
        # create a test location
        location = (39.127040, -94.840450)
        nearest_pharmacy = locate_nearest_pharmacy(*location)
        self.assertEqual(nearest_pharmacy["state"], "MO")
