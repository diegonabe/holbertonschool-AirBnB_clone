#!/usr/bin/python3
import json
import os

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
        all_objs = FileStorage.__objects
        obj_dict = {}
        
        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()
            
            with open(FileStorage.__file_path, "w", encoding="utf-8") as a_file:
                json.dump(obj_dict, a_file)

    def reload(self):
        """

        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as a_file:
                try:
                    obj_dict = json.load(file)
                    for key. value in obj_dict.items():
                        class_name. obj_id = key.split('.')

                        cls = eval(class_name)
                        instance = cls(**values)
                        FileStorage.__objects[key] = instance
                except Exception as e:
                        pass                
