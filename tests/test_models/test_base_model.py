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

        self.assertTrue(hasattr(theBaseModel, "id"))
        self.assertTrue(hasattr(theBaseModel, "created_at"))
        self.assertTrue(hasattr(theBaseModel, "updated_at"))

        self.assertIsInstance(theBaseModel.id, str)
        self.assertIsInstance(theBaseModel.created_at, datetime)
        self.assertIsInstance(theBaseModel.updated_at, datetime)

    def test_str(self):
        dt = datetime.now()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "1"
        bm.created_at = bm.updated_at = dt
        bmstring = bm.__str__()
        self.assertIn("[BaseModel] (1)", bmstring)
        self.assertIn("'id': '1'", bmstring)
        self.assertIn("'created_at': " + dt_repr, bmstring)
        self.assertIn("'updated_at': " + dt_repr, bmstring)

if __name__ == "__main__":
    unittest.main()
