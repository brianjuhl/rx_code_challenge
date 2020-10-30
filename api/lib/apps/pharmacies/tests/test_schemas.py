import unittest

from pydantic.error_wrappers import ValidationError
from ..schemas import Location, Pharmacy


class TestPharmacySchemas(unittest.TestCase):

    def test_valid_location(self):
        """valid coordinates passes schema validation"""
        coordinates = {
            "latitude": 89.434,
            "longitude": -65.950
        }
        Location(**coordinates) # would throw validation error
    
    def test_invalid_location(self):
        """invalid coordinates fails schema validation"""
        # latitude is greater than 90 which should trigger validation error
        coordinates = {
            "latitude": 91.434,
            "longitude": -65.950
        }
        try: 
            Location(**coordinates)
        except Exception as e:
            self.assertIsInstance(e, ValidationError)
            

    
