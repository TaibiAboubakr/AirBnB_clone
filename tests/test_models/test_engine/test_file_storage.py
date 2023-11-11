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


if __name__ == "__main__":
    unittest.main()
