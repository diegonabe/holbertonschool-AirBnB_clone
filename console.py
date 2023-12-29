#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
