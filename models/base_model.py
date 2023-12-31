#!/usr/bin/python3

from datetime import datetime
import uuid
import models
from models import storage
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
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else: 
             self.id = str(uuid.uuid4())
             self.created_at = datetime.utcnow()
             self.updated_at = datetime.utcnow()
            
             self.cls_name = self.__class__.__name__
             storage.new(self)

    def __str__(self):
        """
        Método para representar la cadena de un objeto
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
    
    def save(self):
        """
        Método para guardar
        """
        storage.save()    

    def to_dict(self):
        """
        Método para crear un directorio
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict

