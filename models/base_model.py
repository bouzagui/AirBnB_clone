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
        """basemodel initialization"""
        if kwargs and len(kwargs) != 0:
            if '__class__' in kwargs:
                del kwargs['__class__']
            kwargs['created_at'] = datetime.fromisoformat(kwargs['created_at'])
            kwargs['updated_at'] = datetime.fromisoformat(kwargs['updated_at'])
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid4())
            now = datetime.now()
            self.created_at = now
            self.updated_at = now

    def __str__(self):
        """Returns the string representation of an instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """update the public instance updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns the dictionary
        representation of the instance"""
        to_dict = dict(self.__dict__)
        to_dict["__class__"] = self.__class__.__name__
        to_dict["created_at"] = to_dict["created_at"].isoformat()
        to_dict["updated_at"] = to_dict["updated_at"].isoformat()
        return to_dict
