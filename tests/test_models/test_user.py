#!/usr/bin/python3
"""my user testcase """

from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """my test user """

    def __init__(self, *args, **kwargs):
        """my function init """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """my first name function test """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """my last name function test """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """my email func test """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """my password function """
        new = self.value()
        self.assertEqual(type(new.password), str)
