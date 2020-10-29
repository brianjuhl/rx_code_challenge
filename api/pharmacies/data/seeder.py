import os

from mongoengine import connect
from ..models import Pharmacy


if __name__ == "__main__":
    mongo_uri = os.environ["MONGO_URI"]
    
    connect("rx_code_challenge", host=mongo_uri)

    pharmacy_data = {
        "name": "WALGREENS",
        "address": "3696 SW TOPEKA BLVD",
        "city": "TOPEKA",
        "state": "KS",
        "zip_code": 66611,
        "latitude": 39.001423,
        "longitude": -95.68695
    }

    pharmacy = Pharmacy(**pharmacy_data)
    pharmacy.save()
