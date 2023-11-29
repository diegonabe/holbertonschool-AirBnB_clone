#!/usr/bin/python3
import models
from uuid import uuid4
from datetime import datetime

"""Defining a class BaseModel of our project"""


def __init__(self, *args, **kwargs):
    """Initilization of our new Basemodel Constructor

        Arg:
            *args: it takes non keywords arguments.
            *kwargs: it takes keywords arguments.

            Attributes
            id(str)create an identity user and handle in string.
            created_at: current datetime:
            updated_at: updates current datetime:

            Methods:
            __str__(self): output the class name, the id and create dictionaties.
            save(self): save the instance attribute with the current time.
            to_dict(self): return the  dictionary with all values and keys.

        """

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            model.storage.new(self)





