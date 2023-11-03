#!/usr/bin/python3


"""
This module will define the BaseModel class, with 
common attributes/methods for other classes
"""


from datetime import datetime
from models.__init__ import storage
import uuid


class BaseModel:
    """
    This class will be the base for a series of subclasses.
    It will save attributes as id, creation and last update time,
    as well as being able to convert into or being created from a
    dictionary
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            self.create_from_dic(**kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
    
    def __str__(self):
        """
        Returns print format [<class name>] (<self.id>) <self.__dict__>
        """
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        Updates the public instance attribute updated_at
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance
        """
        dicti = {key: value for key, value in vars(self).items()}
        dicti["__class__"] = self.__class__.__name__
        dicti['created_at'] = self.created_at.isoformat()
        dicti['updated_at'] = self.updated_at.isoformat()
        return dicti

    def create_from_dic(self, **kwargs):
        """
        Creates an instance from a dictionary
        """
        kwargs['created_at'] = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
        kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        for key, value in kwargs.items():
            if key != '__class__':
                setattr(self, key, value)
