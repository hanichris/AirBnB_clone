#!/usr/bin/env python3
""" Module to define a user instances """


from models.base_model import BaseModel


class User(BaseModel):
    """ Class definition for a user

    Attributes:
        email (str): email address
        password (str): passcode
        first_name (str): first name
        last_name (str): last name

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Constructor method to initialize user instances

        Args:
            args: list of arguments
            kwargs: key/value dictionary of arguments

        """
        super().__init__(args, kwargs)
