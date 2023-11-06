#!/usr/bin/python3


"""
This module will define the user state, with 
BaseModel implementation
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """
    Implementation of BaseModel class
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ()

    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
