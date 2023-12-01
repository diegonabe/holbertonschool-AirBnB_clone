#!/usr/bin/python3

from datetime import datetime
import uuid

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
        time_format = "%Y-%m-%dT %H:%M:%S.%f"
            if key == "__class__":
                continue
            elif key == "created_at" or key == "updated_at":
                setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
    else: 
         self.id = str(uuid.uuid4())
        
         self.created_at = datetime.utcnow()
         self.updated_at = datetime.utcnow()

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
        self.updated_at = datetime.now()
            
    def to_dict(self):
        """
        Método para crear un directorio
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict



my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))


print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
