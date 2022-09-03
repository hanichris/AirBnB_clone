#!/usr/bin/env python3
""" Module to define amenity instances """


from models.base_model import BaseModel


class Place(BaseModel):
    """ Class definition for an amenity

    Attributes:
        name (str): name of the amenity
        city_id (str): unique id for the city
        user_id (str): unique id for the user
        description (str): short description
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): maximum number of guests
        price_by_night (int): cost price for the night
        latitide (float): latitude gps point
        longitude (float): longitude gps point
        amenity_ids (list): list of all unique ids of the places


    """
    name = str()
    city_id = str()
    user_id = str()
    description = str()
    number_rooms = int(0)
    number_bathrooms = int(0)
    max_guest = int(0)
    price_by_night = int(0)
    latitide = float(0.0)
    longitude = float(0.0)
    amenity_ids = list()

    def __init__(self, *args, **kwargs):
        """ Constructor method to initialize place instances

        Args:
            args: list of arguments
            kwargs: key/value dictionary of arguments

        """
        super().__init__(args, kwargs)
