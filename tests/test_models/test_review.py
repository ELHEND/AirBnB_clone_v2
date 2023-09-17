#!/usr/bin/python3
"""my review test """

from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """my review function test """

    def __init__(self, *args, **kwargs):
        """mu init fun """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """my place id function """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """user id func test """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """test test func """
        new = self.value()
        self.assertEqual(type(new.text), str)
