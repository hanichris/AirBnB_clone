#!/usr/bin/python3
""" Module to define a city instances """
from models.base_model import BaseModel


class City(BaseModel):
    """ Class definition for a city

    Attributes:
        name (str): name of the city
        state_id (str): unique id of the state

    """
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """ Constructor method to initialize city instances

        Args:
            args: list of arguments
            kwargs: key/value dictionary of arguments

        """
        super().__init__(args, kwargs)
