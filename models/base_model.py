#!/usr/bin/python3
""" import necessary modules """

from uuid import uuid4
from datetime import datetime
import models
""" BaseModel calss """


class BaseModel:
    """ BaseModel class """

    def __init__(self, *args, **kwargs):
        """Initialize a new instance.
            Args:
                id (str(uuid)): id of the new instance
        """
        if args is not None and len(args) > 0:
            pass
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)

    def __str__(self):
        """ returns [<class name>] (<self.id>) <self.__dict__> """
        ClassName = self.__class__.__name__
        return f"[{ClassName}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the public instance attribute updated_at
            with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        Dict = {'__class__': self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                value = value.isoformat()
            Dict[key] = value
        return Dict
