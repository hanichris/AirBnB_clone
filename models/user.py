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
    email = str()
    password = str()
    first_name = str()
    last_name = str()
