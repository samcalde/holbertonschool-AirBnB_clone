#!/usr/bin/python3


"""
This module will define the FileStorage class, that serializes
instances to a JSON file and deserializes JSON files to instances
"""


import json


class FileStorage:
    """
    Class used to save object instances and reload them from a JSON file
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the dictionary of current instances
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary self.__objects
        """
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """
        Saves self.__objects into a JSON file
        """
        ser_obj = {k: o.to_dict() for k, o in FileStorage.__objects.items()}
        with open(f'{self.__file_path}', 'w') as file:
            json.dump(ser_obj, file, default=str)

    def reload(self):
        """
        Loads a JSON file into self.__objects
        """
        BaseModel, User, State, City, Amenity, Place, Review = self.import_modules()
        try:
            with open(f'{self.__file_path}', 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    instance_key = key.split(".")
                    class_name = instance_key[0]
                    obj = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj
        except Exception as e:
            pass
    
    def import_modules(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        return(BaseModel, User, State, City, Amenity, Place, Review)
