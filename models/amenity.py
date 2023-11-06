#!/usr/bin/python3


"""
This module will define the user state, with 
BaseModel implementation
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Implementation of BaseModel class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
