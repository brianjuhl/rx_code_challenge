import unittest
import pathlib
import csv

from ....database import connect_to_mongo_service, disconnect_from_mongo_service
from .seeder import parse_pharmacies_from_csv


class TestPharmacySeeder(unittest.TestCase):

    def setUp(self):
        """set up test database connection"""
        connect_to_mongo_service("mongomock://localhost")

    def tearDown(self):
        """disconnect test database"""
        disconnect_from_mongo_service()

    def parse_pharmacies_from_csv(self):
        """successfully parses csv provided in code challenge"""
        # assuming file is in the same directory as this file
        module_path = pathlib.Path(__file__).parent.absolute()
        test_pharmacy = parse_pharmacies_from_csv(f"{module_path}/pharmacies.csv")[0]
        self.assertIsInstance(test_pharmacy["name"], str)
        self.assertIsInstance(test_pharmacy["address"], str)
        self.assertIsInstance(test_pharmacy["city"], str)
        self.assertIsInstance(test_pharmacy["state"], str)
        self.assertIsInstance(test_pharmacy["zip_code"], int)
        self.assertIsInstance(test_pharmacy["latitude"], float)
        self.assertIsInstance(test_pharmacy["longitude"], float)

