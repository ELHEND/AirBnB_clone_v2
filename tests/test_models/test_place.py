#!/usr/bin/python3
"""my place file test """

from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """my test place function """

    def __init__(self, *args, **kwargs):
        """my init function """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """my city id function """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """my test user id function """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """my name test """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """my description function test """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """my number room function test """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """my number bathrooms """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """my max guest"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """self price night """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """latitude test function """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """my longitude test function """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """my amenity ids function """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
