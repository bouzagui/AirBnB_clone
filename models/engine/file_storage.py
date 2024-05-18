#!/usr/bin/python3
<<<<<<< HEAD
"""a module of a class"""
import json
from datetime import datetime
from models.base_model import BaseModel


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances"""

    def __init__(self):
        """initializes the class"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """returns the dict"""
        return self.__objects
    
    def new(self, obj):
        """sets the obj"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
    
    def save(self):
        """serialises self"""
        with open(self.__file_path, 'w') as file:
            obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(obj_dict, file)
    
    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_data in data.items():
                    class_name = key.split('.')[0]
                    obj_instance = globals()[class_name](**obj_data)
                    self.__objects[key] = obj_instance

        except FileNotFoundError:
            pass
=======
""" recreate a BaseModel """
import cmd

class FileStorage:
    def __init__(self, *args, **kwargs):
        __file_path = kwargs.('file_path')
>>>>>>> 9e8c9dbbadb07f328dd3603e542cd626e0e6462c
