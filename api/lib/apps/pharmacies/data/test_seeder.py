import unittest
import pathlib
import csv

from ....database import connect_to_mongo_service, disconnect_from_mongo_service
from .seeder import parse_pharmacies_from_csv, seed_pharmacies
from ..models import Pharmacy


class TestPharmacySeeder(unittest.TestCase):

    def setUp(self):
        """set up test database connection"""
        connect_to_mongo_service("mongomock://localhost")
        # assuming file is in the same directory as this file
        module_path = pathlib.Path(__file__).parent.absolute()
        self.pharmacy_data = parse_pharmacies_from_csv(
            f"{module_path}/pharmacies.csv")

    def tearDown(self):
        """disconnect test database"""
        del self.pharmacy_data
        disconnect_from_mongo_service()

    def test_parse_pharmacies_from_csv(self):
        """successfully parses csv provided in code challenge"""
        for pharmacy in self.pharmacy_data:
            self.assertIsNotNone(pharmacy["name"])
            self.assertIsNotNone(pharmacy["address"])
            self.assertIsNotNone(pharmacy["city"])
            self.assertIsNotNone(pharmacy["state"])
            self.assertIsNotNone(pharmacy["zip_code"])
            self.assertIsNotNone(pharmacy["latitude"])
            self.assertIsNotNone(pharmacy["longitude"])

    def test_seed_pharmacies(self):
        """successfully saves parsed pharmacy data"""
        # will raise vailidation error if pharmacy has invalid shape
        seed_pharmacies(self.pharmacy_data)
        self.assertGreater(len(Pharmacy.objects), 1)

        