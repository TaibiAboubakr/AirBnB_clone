#!/usr/bin/python3
"""testing the FileStorage class"""

import unittest
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestingFileStorage(unittest.TestCase):
    """
    testing the class FileStorage if it exists
    with its attributes and checking its type
    """

    def test_FileStorage(self):
        theFileStorage = FileStorage()
        self.assertTrue(hasattr(theFileStorage, "all"))
        self.assertTrue(hasattr(theFileStorage, "new"))
        self.assertTrue(hasattr(theFileStorage, "save"))
        self.assertTrue(hasattr(theFileStorage, "reload"))

    def test_FileStorage_objects(self):
        fs = FileStorage()
        file_path = FileStorage._FileStorage__file_path
        
        self.assertIsInstance(file_path, str)
        self.assertTrue(hasattr(fs, '_FileStorage__file_path'))



if __name__ == "__main__":
    unittest.main()
