#!/usr/bin/env python3
""" Module to define base class """


import uuid
from datetime import datetime


class BaseModel(object):
    """ Base class model for all other classes

    Attributes:
        id (str): unique identifier of the instance
        created_at (datetime): when the instance was created
        updated_at (datetime): when the instance was updated with new values

    """
    def __init__(self, *args, **kwargs):
        """ Constructor method to initialize class instances

        Args:
            args: list of arguments
            kwargs: key/value dictionary of arguments

        """
        if kwargs is None or kwargs.get('id') is None:
            self.id = str(uuid.uuid4())
        if kwargs is None or kwargs.get('created_at') is None:
            self.created_at = datetime.now()
        if kwargs is None or kwargs.get('updated_at') is None:
            self.updated_at = datetime.now()
        if kwargs is not None:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = str(v)
                elif k == "created_at":
                    if isinstance(v, int):
                        self.created_at = datetime(v)
                    elif isinstance(v, datetime):
                        self.created_at = v
                    else:
                        self.created_at = datetime.fromisoformat(v)
                elif k == "updated_at":
                    if isinstance(v, int):
                        self.updated_at = datetime(v)
                    elif isinstance(v, datetime):
                        self.updated_at = v
                    else:
                        self.updated_at = datetime.fromisoformat(v)
                elif k != "__class__":
                    self.__setattr__(k, v)

    def __str__(self):
        """ Returns printable string for class instance """
        return("[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__))

    def save(self):
        """ Method to update instance attribute 'updated_at'
            with the current datetime

        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary of all keys/values
            in '__dict__' attribute of the instance

        """
        d = dict()
        d = self.__dict__
        if '__class__' not in d:
            d.update({'__class__': self.__class__.__name__})
            d.update({'created_at': d.get('created_at').isoformat
                     (timespec="microseconds")})
            d.update({'updated_at': d.get('updated_at').isoformat
                     (timespec="microseconds")})
        return d
