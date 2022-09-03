#!/usr/bin/env python3
""" Module to define amenity instances """


from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class definition for an amenity

    Attributes:
        name (str): name of the amenity

    """
    name = str()

    def __init__(self, *args, **kwargs):
        """ Constructor method to initialize amenity instances

        Args:
            args: list of arguments
            kwargs: key/value dictionary of arguments

        """
        super().__init__(args, kwargs)
