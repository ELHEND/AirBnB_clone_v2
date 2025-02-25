#!/usr/bin/python3
"""my state test cases """

from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """state function test """

    def __init__(self, *args, **kwargs):
        """my init """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """my test name3 func """
        new = self.value()
        self.assertEqual(type(new.name), str)
