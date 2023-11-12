#!/usr/bin/python3
"""testing the class BasseModel"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestingBaseModel(unittest.TestCase):
    """
    testing the class BaseModel if it exists with its
    methods, attributes and checking its types
    """
    def test_BaseModel_methods(self):
        theBaseModel = BaseModel()
        self.assertTrue(hasattr(theBaseModel, "__init__"))
        self.assertTrue(hasattr(theBaseModel, "__str__"))
        self.assertTrue(hasattr(theBaseModel, "save"))
        self.assertTrue(hasattr(theBaseModel, "to_dict"))

        self.assertTrue(hasattr(theBaseModel, "id"))
        self.assertTrue(hasattr(theBaseModel, "created_at"))
        self.assertTrue(hasattr(theBaseModel, "updated_at"))

    def test_BaseModel_types(self):
        theBaseModel = BaseModel()
        self.assertIsInstance(theBaseModel.id, str)
        self.assertIsInstance(theBaseModel.created_at, datetime)
        self.assertIsInstance(theBaseModel.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
