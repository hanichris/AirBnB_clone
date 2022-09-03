#!/usr/bin/python3
""" Module to define review instances """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class definition for a review

    Attributes:
        place_id (str): unique id for the place
        user_id (str): unique id of the user
        text (str): short information

    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Constructor method to initialize review instances

        Args:
            args: list of arguments
            kwargs: key/value dictionary of arguments

        """
        super().__init__(args, kwargs)
