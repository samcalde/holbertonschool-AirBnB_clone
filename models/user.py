#!/usr/bin/python3


"""
This module will define the user class, with 
BaseModel implementation
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    This class implements BaseModel, and adds
    several attributes, such as email, password, 
    first and last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
