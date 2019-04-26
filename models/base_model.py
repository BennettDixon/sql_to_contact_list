#!/usr/bin/python3
"""This module is the base model for use in all other models
"""


import datetime
import models
import uuid


class BaseModel():
    """base model parent class for all other classes
       used in project
    """

    def __init__(self, *args, **kwargs):
        """init method for base class used in instantiation
        """
        if len(kwargs) >= 1:
            print("setting from dict")
            self.set_from_dict(**kwargs)
        self.id = str(uuid.uuid4())
        models.storage.new(self)
        print('created base_model inherited inst')

    def __str__(self):
        """custom str method for str and print
        """
        builder = "["
        builder += str(self.__class__.__name__) + '] ('
        builder += str(self.id) + ') ' + str(self.__dict__)
        return builder

    def save(self):
        """save method used for updating class so updated_at changes
        """
        models.storage.save()

    def to_dict(self):
        """
        returns the dictionary of our instance
        """
        temp_d = self.__dict__.copy()
        temp_d['__class__'] = self.__class__.__name__
        return temp_d

    def set_from_dict(self, **kwargs):
        """sets attributes from dictionary
        """
        for (k, v) in kwargs.items():
            if k in ('created_at', 'updated_at'):
                self.__dict__[k] = datetime.datetime\
                                           .strptime(v,
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.__dict__[k] = v
