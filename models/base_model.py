#!/usr/bin/python3

from datetime import datetime
import uuid
#import models

"""
Se crea la clase BaseModel
"""
class BaseModel:
    """
    Clase BaseModel para todas las subclases en el proyecto de AirBnb clone.
    """
    
    def __init__(self, *args, **kwargs):
        """
        Método constructor de la clase BaseModel
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created.at = datetime.now()
            self.updated.at = datetime.now()
            #models.storage.new(self)
        else:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    date_format = "%Y-%m-%dT%H:%M:%S.%f"
                    val = datetime.strptime(kwargs[key], date_format)
                if key != "__class__":
                    setattr(self, key, val)
    
    def __str__(self):
        """
        Método para representar la cadena de un objeto
        """
        name_class = self.__class__.__name__
        return "[{}] ({}) {}".format(name_class, self.id, self.__dict__)
    
    def save(self):
        """
        Método para guardar
        """
        self.updated_at = datetime.now()
        #models.storage.save()
    
    def to_dict(self):
        """
        Método para crear un directorio
        """
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        formatTime = "%Y-%m-%dT %H:%M:%S.%f"
        new_dict["created_at"] = self.created_at.strftime(formatTime)
        new_dict["updated_at"] = self.updated_at.strftime(formatTime)
        return new_dict
