#!/usr/bin/python3
"""testing the BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestingBaseModel(unittest.TestCase):
    """
    testing the class BaseModel if it exists
    with its attributes and checking its type
    """

    def test_BaseModel(self):
        theBaseModel = BaseModel()
        self.assertTrue(hasattr(theBaseModel, "name"))
        self.assertTrue(hasattr(theBaseModel, "id"))
        self.assertTrue(hasattr(theBaseModel, "state_id"))
        self.assertTrue(hasattr(theBaseModel, "created_at"))
        self.assertTrue(hasattr(theBaseModel, "updated_at"))

        self.assertIsInstance(theBaseModel.name, str)
        self.assertIsInstance(theBaseModel.id, str)
        self.assertIsInstance(theBaseModel.state_id, str)
        self.assertIsInstance(theBaseModel.created_at, datetime)
        self.assertIsInstance(theBaseModel.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
