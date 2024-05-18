#!/usr/bin/python3
"""the console 'main' part of the project"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """command interpreter"""

    prompt = "(hbnb) "
    classes = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    do_EOF = do_quit

    def do_create(self, line):
        """Creates a new instance of a given class, saves it \
        (to the JSON file) and prints the id."""
        if line == '':
            print('** class name missing **')
        elif line not in HBNBCommand.classes:
            print('** class doesn\'t exist **')
        else:
            obj = BaseModel()
            storage.save()
            print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance \
        based on the class name and id."""
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.classes:
            print('** class doesn\'t exist **')
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            obj = storage.all().get(key)
            if obj is None:
                print('** no instance found **')
            else:
                print(obj)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
