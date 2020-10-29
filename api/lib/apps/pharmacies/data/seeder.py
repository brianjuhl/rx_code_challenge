import pathlib
import csv

from mongoengine import errors

from ..models import Pharmacy
from ....database import connect_to_mongo_service, disconnect_from_mongo_service


def parse_pharmacies_from_csv(file_path):
    """Parse csv provided in code challenge"""

    data = []

    # Open a csv reader
    with open(file_path, encoding="utf-8") as csvf:
        csv_reader = csv.DictReader(csvf)

        # Convert each row into a dict and add to data
        for row in csv_reader:
            data.append(row)

    return data


def seed_pharmacies(pharmacy_data):
    """seed database with parsed pharmacy data"""
    for pharmacy in pharmacy_data:
        try:
            new_pharmacy = Pharmacy(**pharmacy)
            new_pharmacy.save()
        except errors.ValidationError:
            print("Invalid pharmacy shape provided")
            pass


if __name__ == "__main__":
    # connect to mongo service
    connect_to_mongo_service()
    # assuming file is in the same directory as this file
    module_path = pathlib.Path(__file__).parent.absolute()
    pharmacy_data = parse_pharmacies_from_csv(f"{module_path}/pharmacies.csv")
    seed_pharmacies(pharmacy_data)
    # close connection to mongo service
    disconnect_from_mongo_service()
