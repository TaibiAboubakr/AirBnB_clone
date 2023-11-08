#!/usr/bin/python3
"""importing BaseModel"""
from uuid import uuid4
from datetime import datetime
import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    """a amenity class that inherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance.
            Args:
                id (str(uuid)): id of the new instance
        """
        super().__init__()
