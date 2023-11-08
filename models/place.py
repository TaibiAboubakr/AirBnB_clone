#!/usr/bin/python3
"""importing BaseModel"""
from uuid import uuid4
from datetime import datetime
import models
from models.base_model import BaseModel


class Place(BaseModel):
    """a place class that inherits from BaseModel"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longtitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialize a new instance.
            Args:
                id (str(uuid)): id of the new instance
        """
        super().__init__()
