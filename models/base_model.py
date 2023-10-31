#!/usr/bin/python3


"""
This module will define the BaseModel class, with 
common attributes/methods for other classes
"""


import datetime
import uuid
import json


class BaseModel:
    """
    This class will be the base for a series of subclasses
    """
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
    def __str__(self):
        """
        Returns print format [<class name>] (<self.id>) <self.__dict__>
        """
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        Updates the public instance attribute updated_at
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance
        """
        dicti = vars(self)
        dicti["__class__"] = self.__class__.__name__
        dicti['created_at'] = self.created_at.isoformat()
        dicti['updated_at'] = self.updated_at.isoformat()
        return dictionary
