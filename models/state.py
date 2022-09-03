#!/usr/bin/python3
""" Module to define a state instances """
from models.base_model import BaseModel


class State(BaseModel):
    """ Class definition for a state

    Attributes:
        name (str): name of the state

    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Constructor method to initialize state instances

        Args:
            args: list of arguments
            kwargs: key/value dictionary of arguments

        """
        super().__init__(args, kwargs)
