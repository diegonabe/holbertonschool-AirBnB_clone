#!/usr/bin/python3
import json


"""This is a class filestore to serialize instance to JSON file and Deserialize Json file to instance"""


class FileStorage:
    """

    """
    __file_path = "file.json"
    __objects= {}

    def new(self, obj):
        """

        """
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj.cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """
        
        """
        return FileStorage.__objects

    def save(self):
        """

        """
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}     
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """

        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                  obj_dict = json.load(file)
                  for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)
                    instance = cls(**value)
                    FileStorage.__objects[key] = instance
        except FileNotFoundError:
            pass
        except Exception as e:
            print("Error reloading:", e)                
