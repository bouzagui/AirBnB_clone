#!/usr/bin/python3
""" base module for all functions """
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    class BaseModel that defines all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initialization of BaseModel Class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    self.__dict__[key] = value

    def __str__(self) -> str:
        """Returns the string representation of an instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """update the public instance updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """returns the dictionary
        representation of the instance"""
        to_dict = dict(self.__dict__)
        to_dict["__class__"] = self.__class__.__name__
        to_dict["created_at"] = to_dict["created_at"].isoformat()
        to_dict["updated_at"] = to_dict["updated_at"].isoformat()
        return to_dict
