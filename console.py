#!/usr/bin/python3
"""the console 'main' part of the project"""
import cmd


class HBNBCommand(cmd.Cmd):
    """command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    do_EOF = do_quit


if name == '__main__':
    HBNBCommand().cmdloop()
