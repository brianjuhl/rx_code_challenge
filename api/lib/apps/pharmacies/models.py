from mongoengine import Document, StringField, IntField, FloatField, GeoPointField
from geopy.distance import great_circle


class Pharmacy(Document):
    name = StringField(required=True)
    address = StringField(required=True)
    city = StringField(required=True)
    state = StringField(required=True)
    zip_code = IntField(required=True)
    latitude = FloatField(required=True)
    longitude = FloatField(required=True)
    coordinates = GeoPointField(required=True)

    def clean(self):
        # set GeoPointField from latitude and longitude
        self.coordinates = [self.latitude, self.longitude]

    def distance_from(self, latitude, longitude):
        """calculate distance between the current pharamacy's location and provided location"""
        distance = great_circle([latitude, longitude], (self.latitude, self.longitude))
        # return distance in miles
        return distance.mi
