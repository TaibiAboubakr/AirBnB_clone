#!/usr/bin/python3
"""importing BsaeModel"""
from uuid import uuid4
from datetime import datetime
import models
from models.base_model import BaseModel


class City(BaseModel):
    """a city class that inherits from BaseModel"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance.
            Args:
                id (str(uuid)): id of the new instance
        """
        super().__init__()
