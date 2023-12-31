#!/usr/bin/python3
"""
Console Module
"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it, and prints the id.
        """
        if not args:
            print("** class name missing **")
            return

        try:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the class name and id.
        """
        args_list = shlex.split(args)

        if not args_list:
            print("** class name missing **")
            return

        class_name = args_list[0]

        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        instance_id = args_list[1]
        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id.
        """
        args_list = shlex.split(args)

        if not args_list:
            print("** class name missing **")
            return

        class_name = args_list[0]

        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        instance_id = args_list[1]
        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, args):
        """
        Prints all string representation of all instances based or not on the class name.
        """
        args_list = shlex.split(args)
        objects = storage.all()

        if args_list and args_list[0] not in storage.classes():
            print("** class doesn't exist **")
            return

        if args_list:
            class_name = args_list[0]
            objects = {k: v for k, v in objects.items() if k.startswith(class_name)}

        print([str(obj) for obj in objects.values()])

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        """
        args_list = shlex.split(args)

        if not args_list:
            print("** class name missing **")
            return

        class_name = args_list[0]

        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        instance_id = args_list[1]
        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args_list) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args_list[2]

        if len(args_list) < 4:
            print("** value missing **")
            return

        value_str = args_list[3]
        value = None

        try:
            value = int(value_str)
        except ValueError:
            try:
                value = float(value_str)
            except ValueError:
                if value_str[0] == value_str[-1] == '"':
                    value = value_str[1:-1]

        if value is None:
            print("** invalid value **")
            return

        setattr(storage.all()[key], attribute_name, value)
        storage.all()[key].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

