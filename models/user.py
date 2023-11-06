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
    def __init__(self, *args, **kwargs):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
