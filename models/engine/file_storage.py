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
    def __init__(self):
        self.__file_path = './file.json'
        self.__objects = {}
    
    def all(self):
        """
        Returns the dictionary of current instances
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary self.__objects
        """
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj.to_dict()
    
    def save(self):
        """
        Saves self.__objects into a JSON file
        """
        with open(f'{self.__file_path}', 'w') as file:
            json.dump(self.__objects, file)
    
    def reload(self):
        """
        Loads a JSON file into self.__objects
        """
        try:
            with open(f'{self.__file_path}', 'r') as file:
                self.__objects = json.load(file)
        except:
            pass
