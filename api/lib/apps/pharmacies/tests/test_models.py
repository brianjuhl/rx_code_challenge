import unittest
from mongoengine import connect, disconnect, get_connection, errors

from ..models import Pharmacy


class TestPharmacyModels(unittest.TestCase):

    # test pharmacy data which will pass validation
    valid_pharmacy_data = {
        "name": "WALGREENS",
        "address": "3696 SW TOPEKA BLVD",
        "city": "TOPEKA",
        "state": "KS",
        "zip_code": 66611,
        "latitude": 39.001423,
        "longitude": -95.68695
    }

    def setUp(self):
        """set up test database connection"""
        connect("testdb", host="mongomock://localhost")

    def tearDown(self):
        """disconnect test database"""
        disconnect()

    def test_valid_pharmacy(self):
        """pharmacy with valid shape is created successfully"""
        pharmacy = Pharmacy(**self.valid_pharmacy_data)
        # will throw a mongoengine.errors.ValidationError if invalid shape
        pharmacy.save()

    def test_calculate_distance_from(self):
        """correctly calculates distance from provided location"""
        # create Pharmacy instance with valid shape
        pharmacy = Pharmacy(**self.valid_pharmacy_data)

        # create a test location
        location = (39.127040, -94.840450)

        # calculate pharamacies distance from test location
        distance_from_pharmacy = pharmacy.distance_from(*location)

        # assert distance (rounded to two decimal places) is 46.23
        self.assertEqual(round(distance_from_pharmacy, 2), 46.23)
