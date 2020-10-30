import json
from scipy import spatial

from .models import Pharmacy
from ...database import DatabaseEmptyError


def locate_nearest_pharmacy(latitude, longitude):
    """
    query database for nearest pharmacy and return 
    pharmacy data and distance from pharmacy in a dict
    that will pass schema validation
    """

    # simplest way to get nearest pharmacy location, but unsupported by mongomock
    # nearest_pharmacy = Pharmacy.objects(coordinates__near=[latitude, longitude])[0]

    # using KD Tree instead
    # query database for all pharmacies
    pharmacies = Pharmacy.objects.only('coordinates')

    # raise exception if no pharmacies (database not seeded)
    if len(pharmacies) == 0:
        raise DatabaseEmptyError("No pharmacies in database")

    # set empty location array
    locations = []

    # append each pharmacy's coordinates to locations array
    for pharmacy in pharmacies:
        locations.append(pharmacy.coordinates)

    # create a KD Tree from locations array
    tree = spatial.KDTree(locations)

    # find nearest neighbor from coordinate args
    nearest_neighbor_index = tree.query((latitude, longitude), 1)[1]

    # grab nearest coordinates and convert to list
    nearest_coordinates = list(tree.data[nearest_neighbor_index])

    # query database with coordinates
    nearest_pharmacy_object = Pharmacy.objects(
        coordinates=nearest_coordinates).exclude('id')[0]

    # get distance from coordinate args in miles
    nearest_pharmacy_distance = nearest_pharmacy_object.distance_from(
        latitude, longitude)

    # create json string from pharmacy object
    nearest_pharmacy = nearest_pharmacy_object.to_json()

    # create dict that will pass schema validation from json
    nearest_pharmacy = json.loads(nearest_pharmacy)

    # add distance from pharmacy to dict
    nearest_pharmacy["distance"] = nearest_pharmacy_distance

    return nearest_pharmacy
