#!/usr/bin/python3
""" Module to define base class """
from copy import deepcopy
from uuid import uuid4
from datetime import datetime
import models


class BaseModel(object):
    """ Base class model for all other classes."""

    def __init__(self, *args, **kwargs):
        """ Constructor method to initialize class instances

        Args:
            args: list of arguments
            kwargs: key/value dictionary of arguments

        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.fromisoformat(value)
                elif key == "updated_at":
                    self.updated_at = datetime.fromisoformat(value)
                else:
                    if key != "__class__":
                        setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """ Returns printable string for class instance """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Method to update instance attribute 'updated_at'
            with the current datetime

        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary of all keys/values
            in '__dict__' attribute of the instance

        """
        new_dict = deepcopy(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
