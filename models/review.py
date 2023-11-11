#!/usr/bin/python3
"""importing BaseModel"""
from uuid import uuid4
from datetime import datetime
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """a review class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance.
            Args:
                id (str(uuid)): id of the new instance
        """
        super().__init__()
