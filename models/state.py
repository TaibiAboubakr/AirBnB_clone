#!/usr/bin/python3
"""importing BaseModel"""
from uuid import uuid4
from datetime import datetime
import models
from models.base_model import BaseModel


class State(BaseModel):
    """ a state class that inehrits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance.
            Args:
                id (str(uuid)): id of the new instance
        """
        super().__init__()
