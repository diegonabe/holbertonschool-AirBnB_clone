#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
import models
from models.base_model import BaseModel
from shlex import split

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing on empty line + ENTER"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def help_quit(self):
        """Print help message for quit"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Print help message for EOF"""
        print("EOF command to exit the program")

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) > 1:
                obj_id = args[1]
                key = class_name + "." + obj_id
                objects = models.storage.all()
                if key in objects:
                    print(objects[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) > 1:
                obj_id = args[1]
                key = class_name + "." + obj_id
                objects = models.storage.all()
                if key in objects:
                    del objects[key]
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = split(arg)
        objects = models.storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                class_name = args[0]
                if class_name not in models.class_dict:
                    print("** class doesn't exist **")
                else:
                    print([str(obj) for key, obj in objects.items() if key.startswith(class_name)])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in models.class_dict:
                print("** class doesn't exist **")
            elif len(args) > 1:
                obj_id = args[1]
                key = class_name + "." + obj_id
                objects = models.storage.all()
                if key in objects:
                    if len(args) > 2:
                        attribute = args[2]
                        if len(args) > 3:
                            value = args[3]
                            setattr(objects[key], attribute, eval(value))
                            models.storage.save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

