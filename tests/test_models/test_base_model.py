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
    def test_BaseModel(self):
        theBaseModel = BaseModel()
        self.assertTrue(hasattr(theBaseModel, "__init__"))
        self.assertTrue(hasattr(theBaseModel, "__str__"))
        self.assertTrue(hasattr(theBaseModel, "save"))
        self.assertTrue(hasattr(theBaseModel, "to_dict"))

    def test_BaseModel_attributes(self):
        bm1 = BaseModel()
        self.assertTrue(hasattr(bm1, "id"))
        self.assertTrue(hasattr(bm1, "created_at"))
        self.assertTrue(hasattr(bm1, "updated_at"))

    def test_BaseModel_types(self):
        bm3 = BaseModel()
        self.assertIsInstance(bm3.id, str)
        self.assertIsInstance(bm3.created_at, datetime)
        self.assertIsInstance(bm3.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
